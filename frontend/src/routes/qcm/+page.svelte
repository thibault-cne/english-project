<script lang="ts">
	import { onMount } from 'svelte';
	import { env } from '$lib/env';
	import { Toast, toastStore, type ToastSettings } from '@skeletonlabs/skeleton';
	import Tts from '$lib/components/TTS.svelte';

	let guess: string;
	let words: [string, string, string, string];
	let page_loading = true;
	let loading = false;

	onMount(async () => {
		await init();
		await new Promise((resolve) => setTimeout(resolve, 1000));
		page_loading = false;
	});

	async function init() {
		const url = `${env.backendUrl}/QCM`;

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
			`${env.backendUrl}/verif_QCM?` +
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
			.then((data) => {
				const t: ToastSettings = {
					message: data.status === 'won' ? 'Correct!' : 'Incorrect',
					classes: 'toast-center toast-bottom w-64 mb-10',
					background: data.status === 'won' ? 'bg-success-700' : 'bg-error-700',
					timeout: 3000
				};
				toastStore.trigger(t);

				setTimeout(() => {
					init();
					loading = false;
					page_loading = false;
				}, 3000);
			});
	}
</script>

<svelte:head>
	<title>QCM</title>
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
{:else}
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
{/if}

<Toast />
