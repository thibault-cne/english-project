<script lang="ts">
	import VerbRow from '$lib/components/VerbRow.svelte';
	import { verbs } from '$lib/constants/verbs';

	const variants = {
		visible: { opacity: 1, x: 0 },
		hidden: { opacity: 0, x: -500 }
	};
</script>

<svelte:head>
	<title>Irregular verbs</title>
</svelte:head>

<h1 class="font-bold text-[48px] p-4">Irregural verbs</h1>

<div class="p-4">
	<table class="table">
		<thead>
			<tr>
				<th>Base verbale</th>
				<th>Preterit</th>
				<th>Participe passé</th>
				<th>Traduction</th>
			</tr>
		</thead>
		<tbody>
			{#each verbs as verb}
				<VerbRow {verb} {variants} />
			{/each}
		</tbody>
	</table>
</div>
