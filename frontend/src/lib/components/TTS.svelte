<script lang="ts">
	import { env } from '$lib/env';
	import { onMount } from 'svelte';

	export let text: string;

	let url = '';
	let loaded = false;

	const submit_url = 'https://large-text-to-speech.p.rapidapi.com/tts';

	const submit_options = {
		method: 'POST',
		headers: {
			'content-type': 'application/json',
			'X-RapidAPI-Key': env.rapidApiKey,
			'X-RapidAPI-Host': 'large-text-to-speech.p.rapidapi.com'
		},
		body: JSON.stringify({
			text: text
		})
	};

	const status_url = 'https://large-text-to-speech.p.rapidapi.com/tts?';

	const status_options = {
		method: 'GET',
		headers: {
			'X-RapidAPI-Key': env.rapidApiKey,
			'X-RapidAPI-Host': 'large-text-to-speech.p.rapidapi.com'
		}
	};

	async function load() {
		let id: string;

		let rep = await fetch(submit_url, submit_options);
		let json = await rep.json();
		id = json.id;

		while (!loaded && id !== undefined) {
			await new Promise((resolve) => setTimeout(resolve, 3000));

			let rep = await fetch(status_url + new URLSearchParams({ id: id }), status_options);
			let json = await rep.json();

			if (json.status === 'success') {
				url = json.url;
				loaded = true;
			} else if (json.status === 'fail') {
				return;
			}
		}
	}

	onMount(async () => {
		// await load();
	});

	function play() {
		const audio = new Audio(url);
		audio.play();
	}
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
{#if loaded}
	<span on:click={play} class="cursor-pointer">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			viewBox="0 0 640 512"
			class="fill-white"
			fill="currentColor"
		>
			><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
				d="M533.6 32.5C598.5 85.3 640 165.8 640 256s-41.5 170.8-106.4 223.5c-10.3 8.4-25.4 6.8-33.8-3.5s-6.8-25.4 3.5-33.8C557.5 398.2 592 331.2 592 256s-34.5-142.2-88.7-186.3c-10.3-8.4-11.8-23.5-3.5-33.8s23.5-11.8 33.8-3.5zM473.1 107c43.2 35.2 70.9 88.9 70.9 149s-27.7 113.8-70.9 149c-10.3 8.4-25.4 6.8-33.8-3.5s-6.8-25.4 3.5-33.8C475.3 341.3 496 301.1 496 256s-20.7-85.3-53.2-111.8c-10.3-8.4-11.8-23.5-3.5-33.8s23.5-11.8 33.8-3.5zm-60.5 74.5C434.1 199.1 448 225.9 448 256s-13.9 56.9-35.4 74.5c-10.3 8.4-25.4 6.8-33.8-3.5s-6.8-25.4 3.5-33.8C393.1 284.4 400 271 400 256s-6.9-28.4-17.7-37.3c-10.3-8.4-11.8-23.5-3.5-33.8s23.5-11.8 33.8-3.5zM301.1 34.8C312.6 40 320 51.4 320 64V448c0 12.6-7.4 24-18.9 29.2s-25 3.1-34.4-5.3L131.8 352H64c-35.3 0-64-28.7-64-64V224c0-35.3 28.7-64 64-64h67.8L266.7 40.1c9.4-8.4 22.9-10.4 34.4-5.3z"
			/></svg
		>
	</span>
{/if}
{#if !loaded}
	<span class="cursor-pointer disabled">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			viewBox="0 0 640 512"
			class="fill-slate-500"
			fill="currentColor"
		>
			><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
				d="M533.6 32.5C598.5 85.3 640 165.8 640 256s-41.5 170.8-106.4 223.5c-10.3 8.4-25.4 6.8-33.8-3.5s-6.8-25.4 3.5-33.8C557.5 398.2 592 331.2 592 256s-34.5-142.2-88.7-186.3c-10.3-8.4-11.8-23.5-3.5-33.8s23.5-11.8 33.8-3.5zM473.1 107c43.2 35.2 70.9 88.9 70.9 149s-27.7 113.8-70.9 149c-10.3 8.4-25.4 6.8-33.8-3.5s-6.8-25.4 3.5-33.8C475.3 341.3 496 301.1 496 256s-20.7-85.3-53.2-111.8c-10.3-8.4-11.8-23.5-3.5-33.8s23.5-11.8 33.8-3.5zm-60.5 74.5C434.1 199.1 448 225.9 448 256s-13.9 56.9-35.4 74.5c-10.3 8.4-25.4 6.8-33.8-3.5s-6.8-25.4 3.5-33.8C393.1 284.4 400 271 400 256s-6.9-28.4-17.7-37.3c-10.3-8.4-11.8-23.5-3.5-33.8s23.5-11.8 33.8-3.5zM301.1 34.8C312.6 40 320 51.4 320 64V448c0 12.6-7.4 24-18.9 29.2s-25 3.1-34.4-5.3L131.8 352H64c-35.3 0-64-28.7-64-64V224c0-35.3 28.7-64 64-64h67.8L266.7 40.1c9.4-8.4 22.9-10.4 34.4-5.3z"
			/></svg
		>
	</span>
{/if}
