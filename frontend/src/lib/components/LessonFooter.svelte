<script lang="ts">
	export let next: string;
	export let previous: string;
</script>

<div class="flex justify-between mt-10">
	<a href={previous} class="btn bg-primary-700"><span>&larr;</span>&nbsp;Previous</a>
	<a href={next} class="btn bg-primary-700">Next&nbsp;<span>&rarr;</span></a>
</div>
