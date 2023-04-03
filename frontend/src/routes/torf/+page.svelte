<script lang="ts">
	import { onMount } from 'svelte';
	import { env } from '$lib/env';
	import { Toast, toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';

	let words = {
		eng: '',
		french: ''
	};

	onMount(() => {
		refresh();
	});

	function refresh() {
		fetch(`${env.backendUrl}/TORF`)
			.then((res) => res.json())
			.then((data) => {
				words.eng = data.en_word;
				words.french = data.fr_word;
			});
	}

	function post(type: string) {
		const url = `${env.backendUrl}/TORF_${type}`;

		fetch(url, {
			method: 'GET',
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
					timeout: 5000
				};
				toastStore.trigger(t);

				setTimeout(() => {
					refresh();
				}, 5000);
			});
	}
</script>

<svelte:head>
	<title>True or false</title>
</svelte:head>

<div class="flex flex-col">
	<h1 class="text-[24px]">Does the word {words.eng} is the english of {words.french} ?</h1>

	<div class="flex self-center w-full justify-evenly mt-10 p-4">
		<button
			class="btn bg-primary-500 btn-lg"
			on:click={() => {
				post('True');
			}}>True</button
		>
		<button
			class="btn bg-primary-500 btn-lg"
			on:click={() => {
				post('False');
			}}>False</button
		>
	</div>
</div>

<Toast position="b" />
