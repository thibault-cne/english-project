<script lang="ts">
	import { thib, aurelien } from '$lib/constants/image';
</script>

<svelte:head>
	<title>Hero</title>
</svelte:head>

<div class="flex w-full h-full justify-evenly items-center">
	<div class="flex flex-col justify-center items-center">
		<img src={aurelien} alt="Aurelien" class="rounded-full w-52" />
		<span class="mt-4 font-bold text-lg">Aurélien T.</span>
	</div>
	<div class="flex flex-col justify-center items-center">
		<img src={thib} alt="Thib" class="rounded-full w-52" />
		<span class="mt-4 font-bold text-lg">Thibault C.</span>
	</div>
</div>
