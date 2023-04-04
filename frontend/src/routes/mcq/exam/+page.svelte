<script lang="ts">
	import { onMount } from 'svelte';
	import { env } from '$lib/env';
	import { Toast, toastStore, type ToastSettings } from '@skeletonlabs/skeleton';
	import Tts from '$lib/components/TTS.svelte';

	let guess: string;
	let words: [string, string, string, string];
	let page_loading = true;
	let loading = false;
	let score = {
		won: 0,
		lost: 0
	};
	let end = false;

	onMount(async () => {
		await init();
		await new Promise((resolve) => setTimeout(resolve, 1000));
		page_loading = false;
	});

	async function init() {
		const url = `${env.backendUrl}/QCM_EXAM`;

		let rep = await fetch(url, {
			credentials: 'include',
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		});
		let json = await rep.json();
		words = json.fr_list;
		guess = json.en_word;
	}

	function guess_word(word: string) {
		let url =
			`${env.backendUrl}/verif_QCM_EXAM?` +
			new URLSearchParams({
				word: word
			});
		loading = true;
		page_loading = true;

		fetch(url, {
			credentials: 'include',
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then((res) => res.json())
			.then(async (json) => {
				if (json.status === 'end') {
					score.won = json.score;
					score.lost = json.total - json.score;
					end = true;
				} else {
					words = json.fr_list;
					guess = json.en_word;
				}

				await new Promise((resolve) => setTimeout(resolve, 1000));
				loading = false;
				page_loading = false;
			});
	}
</script>

<svelte:head>
	<title>MCQ</title>
</svelte:head>

{#if page_loading}
	<section class="flex flex-col justify-center w-full h-full">
		<div class="placeholder animate-pulse py-6 w-1/2 self-center" />
		<div class="grid grid-cols-2 gap-4 place-content-evenly place-items-center mt-10">
			<div class="placeholder w-28 animate-pulse py-8" />
			<div class="placeholder w-28 animate-pulse py-8" />
			<div class="placeholder w-28 animate-pulse py-8" />
			<div class="placeholder w-28 animate-pulse py-8" />
		</div>
	</section>
{:else if !end}
	<div class="flex flex-col w-full h-full justify-center items-center">
		<h1 class="text-[24px]">
			What is the french of <span class="text-primary-600 lowercase relative mr-5"
				>{guess}<span class="absolute w-5 h-5 top-2"><Tts text={guess} /></span></span
			> ?
		</h1>
		<div class="grid grid-cols-2 mt-10 w-2/3 gap-y-6 gap-x-4 self-center">
			<button
				class="btn btn-lg variant-filled-primary"
				disabled={loading}
				on:click={() => {
					guess_word(words[0]);
				}}>{words[0]}</button
			>
			<button
				class="btn btn-lg variant-filled-primary"
				disabled={loading}
				on:click={() => {
					guess_word(words[1]);
				}}>{words[1]}</button
			>
			<button
				class="btn btn-lg variant-filled-primary"
				disabled={loading}
				on:click={() => {
					guess_word(words[2]);
				}}>{words[2]}</button
			>
			<button
				class="btn btn-lg variant-filled-primary"
				disabled={loading}
				on:click={() => {
					guess_word(words[3]);
				}}>{words[3]}</button
			>
		</div>
	</div>
{:else if end}
	<div class="flex flex-col w-full h-full justify-center items-center">
		<h1 class="text-[24px]">You finished the exam!</h1>
		<h2 class="text-[16px] mt-4 ml-4">You won {score.won} and lost {score.lost} rounds</h2>

		<button
			class="btn bg-primary-500 btn-lg mt-10"
			on:click={() => {
				init();
				end = false;
			}}>Restart</button
		>
	</div>
{/if}

<Toast />
