<script lang="ts">
	import { onMount } from 'svelte';
	import { env } from '$lib/env';
	import { Toast, toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';

	let words = {
		eng: '',
		french: '',
		order: false
	};
	let end = false;
	let score = {
		won: 0,
		lost: 0
	};

	onMount(() => {
		init();
	});

	function init() {
		fetch(`${env.backendUrl}/TORF_EXAM`, {
			credentials: 'include'
		})
			.then((res) => res.json())
			.then((data) => {
				words.eng = data.en_word;
				words.french = data.fr_word;
				words.order = data.e === 0 ? true : false;
			});
	}

	function post(type: string) {
		const url = `${env.backendUrl}/TORF_EXAM_${type}`;

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
					console.log(data);
					if (data.status === 'end') {
						end = true;
						score.won = data.score;
						score.lost = data.total - data.score;
					} else {
						words.eng = data.en_word;
						words.french = data.fr_word;
						words.order = data.e === 0 ? true : false;
					}
				}, 3000);
			});
	}
</script>

<svelte:head>
	<title>True or false</title>
</svelte:head>

{#if !end}
	<div class="flex flex-col">
		{#if words.order}
			<h1 class="text-[24px]">Does the word {words.eng} is the english of {words.french} ?</h1>
		{:else}
			<h1 class="text-[24px]">Does the word {words.french} is the french of {words.eng} ?</h1>
		{/if}

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
{/if}
{#if end}
	<div class="flex flex-col">
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

<Toast position="b" />
