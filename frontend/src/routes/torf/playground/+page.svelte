<script lang="ts">
	import { onMount } from 'svelte';
	import { env } from '$lib/env';
	import { Toast, toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';
	import Tts from '$lib/components/TTS.svelte';

	let words = {
		eng: '',
		french: '',
		real: ''
	};
	let loading = true;

	onMount(async () => {
		await refresh();
		await new Promise((resolve) => setTimeout(resolve, 1000));

		loading = false;
	});

	async function refresh() {
		let rep = await fetch(`${env.backendUrl}/TORF`, {
			credentials: 'include'
		});
		let json = await rep.json();
		words.eng = json.en_word;
		words.french = json.fr_word;
		words.real = json.real_answer;
	}

	function post(type: string) {
		const url = `${env.backendUrl}/TORF_${type}`;
		loading = true;

		fetch(url, {
			method: 'GET',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then((res) => res.json())
			.then((json) => {
				const t: ToastSettings = {
					message:
						json.status === 'won'
							? 'You won!'
							: 'You lost, the real answer was : ' + words.real + '.',
					classes: 'toast-center toast-bottom w-72 mb-10',
					background: json.status === 'won' ? 'bg-success-700' : 'variant-filled-error',
					timeout: 3000
				};
				toastStore.trigger(t);

				setTimeout(async () => {
					await refresh();
					loading = false;
				}, 3000);
			});
	}
</script>

<svelte:head>
	<title>True or false - Playground</title>
</svelte:head>

{#if loading}
	<section class="flex flex-col justify-center w-full h-full">
		<div class="placeholder animate-pulse py-4" />
		<div class="grid grid-cols-2 gap-4 place-content-evenly place-items-center mt-10">
			<div class="placeholder w-28 animate-pulse py-8" />
			<div class="placeholder w-28 animate-pulse py-8" />
		</div>
	</section>
{:else}
	<div class="flex flex-col w-full h-full justify-center items-center">
		<h1 class="text-[24px]">
			The english word for {words.french} is
			<span class="text-primary-600 lowercase relative mr-5"
				>{words.eng}<span class="absolute w-5 h-5 top-2"><Tts text={words.eng} /></span></span
			>.
		</h1>

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

<Toast position="b" />
