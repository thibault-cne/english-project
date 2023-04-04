<script lang="ts">
	import { onMount } from 'svelte';
	import { env } from '$lib/env';
	import { Toast, toastStore, type ToastSettings } from '@skeletonlabs/skeleton';

	let guess: string;
	let words: [string, string, string, string];
	let page_loading = true;
	let loading = false;

	onMount(() => {
		init();
	});

	function init() {
		const url = `${env.backendUrl}/QCM`;

		fetch(url, {
			credentials: 'include',
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then((res) => res.json())
			.then((data) => {
				words = data.fr_list;
				guess = data.en_word;
				page_loading = false;
			});
	}

	function guess_word(word: string) {
		let url =
			`${env.backendUrl}/verif_QCM?` +
			new URLSearchParams({
				word: word
			});
		loading = true;

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
				}, 3000);
			});
	}
</script>

<svelte:head>
	<title>QCM</title>
</svelte:head>

{#if !page_loading}
	<div class="flex flex-col w-full h-full justify-center items-center">
		<h1 class="text-[24px]">
			What is the french of <span class="text-primary-600 lowercase">{guess}</span> ?
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
