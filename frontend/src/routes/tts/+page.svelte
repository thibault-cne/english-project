<script lang="ts">
	import { env } from '$lib/env';

	const url = 'https://large-text-to-speech.p.rapidapi.com/tts';

	const options = {
		method: 'POST',
		headers: {
			'content-type': 'application/json',
			'X-RapidAPI-Key': env.rapidApiKey,
			'X-RapidAPI-Host': 'large-text-to-speech.p.rapidapi.com'
		},
		body: '{"text":"Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away."}'
	};

	fetch(url, options)
		.then((res) => res.json())
		.then((json) => console.log(json))
		.catch((err) => console.error('error:' + err));
</script>
