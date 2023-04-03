<script lang="ts">
	import { onMount } from 'svelte';
	import { env } from '$lib/env';

	let words = {
		eng: '',
		french: ''
	};
	let playing = true;
	let won = false;

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
				playing = false;
				won = data.status === 'won' ? true : false;
				setTimeout(() => {
					refresh();
					playing = true;
				}, 1000);
			});
	}
</script>

<svelte:head>
	<title>True or false</title>
</svelte:head>

<div class="p-10 flex flex-col">
	<h1 class="text-[32px]">Does the word {words.eng} is the english of {words.french} ?</h1>

	<div class="flex self-center w-full justify-evenly mt-10">
		<button
			class="btn btn-primary btn-wide"
			on:click={() => {
				post('True');
			}}>True</button
		>
		<button
			class="btn btn-primary btn-wide"
			on:click={() => {
				post('False');
			}}>False</button
		>
	</div>

	{#if !playing}
		{#if won}
			<div>Won!</div>
		{:else}
			<div>Lost!</div>
		{/if}
	{/if}
</div>
