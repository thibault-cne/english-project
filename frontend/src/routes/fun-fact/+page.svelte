<script lang="ts">
	let funfact = 'This is a funfact';
</script>

<svelte:head>
	<title>Fun fact</title>
</svelte:head>

<div class="p-10">
	<h1 class="p-4 font-bold text-[48px]">Here is an english fun fact:</h1>

	<span class="text-[16px] mt-4">{funfact}</span>
</div>
