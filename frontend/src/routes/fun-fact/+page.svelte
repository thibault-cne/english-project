<script lang="ts">
	import { env } from '$lib/env';
	import { onMount } from 'svelte';
	import { unionjack } from '$lib/constants/image';

	let funfact = '';
	let loaded = false;

	onMount(() => {
		fetch(env.backendUrl + '/fun-fact', {
			credentials: 'same-origin',
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then((res) => res.json())
			.then(async (data) => {
				funfact = data.fun_fact;

				await new Promise((resolve) => setTimeout(resolve, 1000));
				loaded = true;
			});
	});
</script>

<svelte:head>
	<title>Fun fact</title>
</svelte:head>

<div class="relative h-full w-full flex flex-col items-center">
	<h1 class="p-4 font-bold text-[48px]">Here is an english fun fact:</h1>

	{#if loaded}
		<span class="text-[16px] mt-4">{funfact}</span>
	{:else}
		<div class="placeholder animate-pulse w-1/2 mt-4" />
	{/if}

	<div class="flex w-full absolute bottom-0 justify-center">
		<img src={unionjack} alt="Union Jack" class="w-1/2" />
	</div>
</div>
