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
	let answers: { message: string; answer: boolean }[] = [];

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

		if (json.status === 'end') {
			score.won = json.score;
			score.lost = json.total - json.score;
			end = true;
		} else {
			words = json.fr_list;
			guess = json.en_word;
		}
	}

	async function guess_word(word: string) {
		let url =
			`${env.backendUrl}/verif_QCM_EXAM?` +
			new URLSearchParams({
				word: word
			});
		loading = true;
		page_loading = true;

		let rep = await fetch(url, {
			credentials: 'include',
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		});

		let json = await rep.json();
		let answer = json.answer === 'true' ? true : false;
		let message = 'The english word for ' + json.fr_word + ' is ' + json.en_word + '.';

		answers.push({
			message: message,
			answer: answer
		});

		const t: ToastSettings = {
			message: 'Next question',
			classes: 'toast-center toast-bottom w-64 mb-10',
			background: 'bg-success-700',
			timeout: 1500
		};
		toastStore.trigger(t);

		await init();

		await new Promise((resolve) => setTimeout(resolve, 1500));

		toastStore.clear();
		loading = false;
		page_loading = false;
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
			What is the french for <span class="text-primary-600 lowercase relative mr-5"
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
{:else}
	<div class="flex flex-col w-full h-full justify-center items-center">
		<h1 class="text-[24px]">You finished the exam!</h1>
		<h2 class="text-[16px] mt-4 ml-4">You won {score.won} and lost {score.lost} rounds</h2>

		<div class="flex flex-col justify-start gap-4 mt-4 mb-2">
			{#each answers as answer}
				<div class="flex">
					<span class="w-5 h-5 mr-5">
						{#if answer.answer}
							<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="fill-green-600"
								><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
									d="M438.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L160 338.7 393.4 105.4c12.5-12.5 32.8-12.5 45.3 0z"
								/></svg
							>
						{:else}
							<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" class="fill-red-600"
								><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
									d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"
								/></svg
							>
						{/if}
					</span>
					<span>
						{answer.message}
					</span>
				</div>
			{/each}
		</div>

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
