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
	let answers: { message: string; answer: boolean }[] = [];

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

		if (json.status === 'end') {
			end = true;
			score.won = json.score;
			score.lost = json.total - json.score;
		} else {
			words.eng = json.en_word;
			words.french = json.fr_word;
			words.order = json.e === 0 ? true : false;
		}
	}

	async function post(type: string) {
		const url = `${env.backendUrl}/TORF_EXAM_${type}`;
		loading = true;
		page_loading = true;

		let rep = await fetch(url, {
			method: 'GET',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json'
			}
		});
		let json = await rep.json();
		const t: ToastSettings = {
			message: 'Next question',
			classes: 'toast-center toast-bottom w-64 mb-10',
			background: 'bg-success-700',
			timeout: 3000
		};
		toastStore.trigger(t);

		let answer = json.answer === 'true' ? true : false;
		let message: string = '';

		if (words.order) {
			message = 'The english word for ' + words.french + ' is ' + words.eng + '.';
		} else {
			message = 'The french word for ' + words.eng + ' is ' + words.french + '.';
		}

		answers.push({ message, answer: answer });

		setTimeout(async () => {
			toastStore.clear();
			await init();
			loading = false;
			page_loading = false;
		}, 1000);
	}
</script>

<svelte:head>
	<title>True or false - Exam</title>
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
					The english word for {words.french} is
					<span class="text-primary-600 lowercase relative mr-5"
						>{words.eng}<span class="absolute w-5 h-5 top-2"><Tts text={words.eng} /></span></span
					>.
				</h1>
			{:else}
				<h1 class="text-[24px]">
					The french word for
					<span class="text-primary-600 lowercase relative mr-5"
						>{words.eng}<span class="absolute w-5 h-5 top-2"><Tts text={words.eng} /></span></span
					>
					is {words.french}.
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
			<h2 class="text-[16px] mt-4 ml-4">You won {score.won} rounds and lost {score.lost} rounds</h2>

			<div class="flex flex-col justify-start gap-4 my-8">
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
				class="btn bg-primary-500 btn-lg"
				on:click={() => {
					init();
					end = false;
				}}>Restart</button
			>
		</div>
	{/if}
{/if}

<Toast position="b" />
