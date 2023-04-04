<script lang="ts">
	import { onMount } from 'svelte';
	import { env } from '$lib/env';
	import { Toast, toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';

	let word: string;
	let guess: string = '';
	let loading = false;

	onMount(() => {
		refresh();
		addEventListener('keydown', listener);
	});

	function refresh() {
		const url = env.backendUrl + '/disorder';

		fetch(url, {
			credentials: 'include',
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then((res) => res.json())
			.then((data) => {
				word = data.permutated_word;
			});
	}

	function check() {
		const url = env.backendUrl + '/verif_word?' + new URLSearchParams({ word: guess });
		loading = true;

		// Add word as a query parameter
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
					message: data.status === 'won' ? 'Correct!' : 'Incorrect!',
					classes: 'toast-center toast-bottom w-64 mb-10',
					background: data.status === 'won' ? 'bg-success-700' : 'bg-error-700',
					timeout: 3000
				};
				toastStore.trigger(t);

				setTimeout(() => {
					refresh();
					guess = '';
					loading = false;
				}, 3000);
			});
	}

	function listener(e: KeyboardEvent) {
		if (guess.length < word.length && e.key.length === 1 && e.key.match(/[a-z]/i)) {
			guess += e.key;
		} else if (e.key === 'Backspace') {
			guess = guess.slice(0, -1);
		} else if (e.key === 'Enter' && guess.length === word.length && !loading) {
			check();
		}
	}
</script>

<!-- <svelte:head> -->
<svelte:head>
	<title>Scramble</title>
</svelte:head>

<div class="relative flex flex-col w-full h-full justify-center items-center">
	<h1 class="absolute p-4 font-bold text-[48px] top-0">Scramble</h1>

	{#if word != undefined}
		<div class="flex justify-center items-center gap-4 mt-10">
			{#each word as letter}
				<div class="w-24 h-24 bg-surface-700 rounded-lg flex justify-center items-center">
					<span class="text-xl capitalize">{letter}</span>
				</div>
			{/each}
		</div>
		<div class="flex justify-center items-center gap-4 mt-4">
			{#each guess as letter}
				<div class="w-24 h-24 bg-surface-700 rounded-lg flex justify-center items-center">
					<span class="text-xl capitalize">{letter}</span>
				</div>
			{/each}
			{#each Array(word.length - guess.length) as _, index (index)}
				<div class="w-24 h-24 bg-surface-700 rounded-lg flex justify-center items-center">
					<span class="text-xl capitalize">—</span>
				</div>
			{/each}
		</div>
	{/if}
</div>

<Toast />
