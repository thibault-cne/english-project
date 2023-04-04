<script lang="ts">
	import LessonFooter from '$lib/components/LessonFooter.svelte';
</script>

<svelte:head>
	<title>Lesson - 02</title>
</svelte:head>

<h1 class="p-4 text-[48px] font-bold">Lesson 2 : Common and Proper Nouns</h1>

<p class="mt-4 text-[16px]">
	<span class="font-semibold underline italic">Definition:</span> Common nouns name any person, place,
	thing, or idea. They are not capitalized unless they come at the beginning of a sentence. Proper nouns
	are the names of specific people, places, things, or ideas. Proper nouns should always be capitalized.
</p>

<div class="p-4">
	<table class="table table-compact">
		<thead>
			<tr>
				<th>Common</th>
				<th>Proper</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>boy</td>
				<td>James</td>
			</tr>
			<tr>
				<td>river</td>
				<td>Mississippi River</td>
			</tr>
			<tr>
				<td>car</td>
				<td>Ford</td>
			</tr>
			<tr>
				<td>doctor</td>
				<td>Doctor Jefferson</td>
			</tr>
			<tr>
				<td>town</td>
				<td>Rockledge</td>
			</tr>
			<tr>
				<td>candy bar</td>
				<td>Baby Ruth</td>
			</tr>
		</tbody>
	</table>
</div>

<p class="text-[16px] mt-4">
	<span class="font-semibold underline italic">Hint:</span>
	Don't forget to capitalize all parts of proper nouns. Many people forget to capitalize words like river
	and county in proper nouns like Yellow River and Orange County.
</p>

<LessonFooter previous="/lessons/01" next="/lessons/03" />
