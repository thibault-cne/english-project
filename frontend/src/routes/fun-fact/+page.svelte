<script lang="ts">
	import { env } from '$lib/env';
	import { onMount } from 'svelte';

	let funfact = 'This is a funfact';

	onMount(() => {
		fetch(env.backendUrl + '/fun-fact', {
			headers: {
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': 'http://localhost:5173'
			}
		})
			.then((res) => res.json())
			.then((data) => {
				funfact = data.fun_fact;
			});
	});
</script>

<svelte:head>
	<title>Fun fact</title>
</svelte:head>

<div class="p-10">
	<h1 class="p-4 font-bold text-[48px]">Here is an english fun fact:</h1>

	<span class="text-[16px] mt-4">{funfact}</span>
</div>
