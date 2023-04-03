<script lang="ts">
	import { Motion } from 'svelte-motion';
	import viewport from '$lib/viewport/viewport';

	type Verb = {
		bv: string;
		p: string;
		pp: string;
		t: string;
	};

	export let verb: Verb;
	export let variants: any;

	let v = ['hidden', 'visible'];
	let i = 0;
</script>

<Motion initial="hidden" animate={v[i]} {variants} let:motion>
	<tr use:motion use:viewport on:enterViewport={() => (i = 1)} on:exitViewport={() => (i = 0)}>
		<td>{verb.bv}</td>
		<td>{verb.p}</td>
		<td>{verb.pp}</td>
		<td>{verb.t}</td>
	</tr>
</Motion>
