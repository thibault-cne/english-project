<script lang="ts">
	import { onMount } from 'svelte';
	import { env } from '$lib/env';
	import { Toast, toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';
	import Tts from '$lib/components/TTS.svelte';

	let words = {
		eng: '',
		french: '',
		order: false
	};
	let end = false;
	let loading = false;
	let page_loading = true;
	let score = {
		won: 0,
		lost: 0
	};

	onMount(async () => {
		await init();
		await new Promise((resolve) => setTimeout(resolve, 1000));
		page_loading = false;
	});

	async function init() {
		let rep = await fetch(`${env.backendUrl}/TORF_EXAM`, {
			credentials: 'include'
		});
		let json = await rep.json();
		words.eng = json.en_word;
		words.french = json.fr_word;
		words.order = json.e === 0 ? true : false;
	}

	function post(type: string) {
		const url = `${env.backendUrl}/TORF_EXAM_${type}`;
		loading = true;

		fetch(url, {
			method: 'GET',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then((res) => res.json())
			.then((data) => {
				const t: ToastSettings = {
					message: 'Next question',
					classes: 'toast-center toast-bottom w-64 mb-10',
					background: 'bg-success-700',
					timeout: 3000
				};
				toastStore.trigger(t);

				setTimeout(() => {
					if (data.status === 'end') {
						end = true;
						score.won = data.score;
						score.lost = data.total - data.score;
					} else {
						words.eng = data.en_word;
						words.french = data.fr_word;
						words.order = data.e === 0 ? true : false;
					}
					loading = false;
				}, 3000);
			});
	}
</script>

<svelte:head>
	<title>True or false</title>
</svelte:head>

{#if page_loading}
	<section class="flex flex-col justify-center w-full h-full">
		<div class="placeholder animate-pulse py-4" />
		<div class="grid grid-cols-2 gap-4 place-content-evenly place-items-center mt-10">
			<div class="placeholder w-28 animate-pulse py-8" />
			<div class="placeholder w-28 animate-pulse py-8" />
		</div>
	</section>
{:else}
	{#if !end}
		<div class="flex flex-col w-full h-full justify-center items-center">
			{#if words.order}
				<h1 class="text-[24px]">
					Does the word <span class="text-primary-600 lowercase relative mr-5"
						>{words.eng}<span class="absolute w-5 h-5 top-2"><Tts text={words.eng} /></span></span
					>
					is the english of {words.french}
					?
				</h1>
			{:else}
				<h1 class="text-[24px]">
					Does the word {words.french} is the french of
					<span class="text-primary-600 lowercase relative mr-5"
						>{words.eng}<span class="absolute w-5 h-5 top-2"><Tts text={words.eng} /></span></span
					> ?
				</h1>
			{/if}

			<div class="flex self-center w-full justify-evenly mt-10 p-4">
				<button
					class="btn bg-primary-500 btn-lg"
					disabled={loading}
					on:click={() => {
						post('True');
					}}>True</button
				>
				<button
					class="btn bg-primary-500 btn-lg"
					disabled={loading}
					on:click={() => {
						post('False');
					}}>False</button
				>
			</div>
		</div>
	{/if}
	{#if end}
		<div class="flex flex-col w-full h-full justify-center items-center">
			<h1 class="text-[24px]">You finished the exam!</h1>
			<h2 class="text-[16px] mt-4 ml-4">You won {score.won} and lost {score.lost} rounds</h2>
		</div>

		<button
			class="btn bg-primary-500 btn-lg"
			on:click={() => {
				init();
				end = false;
			}}>Restart</button
		>
	{/if}
{/if}

<Toast position="b" />
