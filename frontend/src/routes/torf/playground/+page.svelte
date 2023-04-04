<script lang="ts">
	import { onMount } from 'svelte';
	import { env } from '$lib/env';
	import { Toast, toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';

	let words = {
		eng: '',
		french: ''
	};
	let loading = false;

	onMount(() => {
		refresh();
	});

	function refresh() {
		fetch(`${env.backendUrl}/TORF`, {
			credentials: 'include'
		})
			.then((res) => res.json())
			.then((data) => {
				words.eng = data.en_word;
				words.french = data.fr_word;
			});
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
			.then((data) => {
				const t: ToastSettings = {
					message: data.status === 'won' ? 'You won!' : 'You lost!',
					classes: 'toast-center toast-bottom w-64 mb-10',
					background: data.status === 'won' ? 'bg-success-700' : 'variant-filled-error',
					timeout: 3000
				};
				toastStore.trigger(t);

				setTimeout(() => {
					refresh();
					loading = false;
				}, 3000);
			});
	}
</script>

<svelte:head>
	<title>True or false</title>
</svelte:head>

<div class="flex flex-col w-full h-full justify-center items-center">
	<h1 class="text-[24px]">
		Does the word <span class="text-primary-600 lowercase">{words.eng}</span> is the english of {words.french}
		?
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

<Toast position="b" />
