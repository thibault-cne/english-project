<script lang="ts">
	import LessonFooter from '$lib/components/LessonFooter.svelte';
</script>

<svelte:head>
	<title>Lesson - 01</title>
</svelte:head>

<h1 class="text-[48px] font-bold p-4">Lesson 1: What is a Noun</h1>

<p class="text-[16px]">
	<span class="underline italic font-semibold">Definition:</span> A noun is a word that names a person,
	place, thing, or idea.
</p>

<p class="mt-4">
	Concrete nouns name people, places, or things that you can touch, see, hear, smell, or taste.
</p>

<div class="p-4">
	<table class="table table-compact">
		<thead>
			<tr>
				<th>Person</th>
				<th>Place</th>
				<th>Thing</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>man</td>
				<td>river</td>
				<td>dog</td>
			</tr>
			<tr>
				<td>Mrs. Jones</td>
				<td>Paris</td>
				<td>Book</td>
			</tr>
			<tr>
				<td>doctor</td>
				<td>mountains</td>
				<td>sports car</td>
			</tr>
			<tr>
				<td>Maddie</td>
				<td>home</td>
				<td>Ferrari</td>
			</tr></tbody
		>
	</table>
</div>

<p class="text-[16px] mt-4">
	Abstract nouns name ideas, concepts, or emotions. These nouns are intangible, which means you
	cannot touch, see, hear, smell, or taste them using your five senses.
</p>

<div class="p-4">
	<table class="table table-compact">
		<thead>
			<tr>
				<th>Idea</th>
				<th>Emotion</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>love</td>
				<td>happiness</td>
			</tr>
			<tr>
				<td>intelligence</td>
				<td>anger</td>
			</tr>
			<tr>
				<td>justice</td>
				<td>excitement</td>
			</tr>
			<tr>
				<td>religion</td>
				<td>fear</td>
			</tr>
			<tr>
				<td>time</td>
				<td>surprise</td>
			</tr>
		</tbody>
	</table>
</div>

<p class="mt-4 text-[16px]">
	<span class="font-semibold italic underline">Hint:</span> Remember, pronouns are not nouns.
</p>

<LessonFooter previous="/lessons/01" next="/lessons/02" />
