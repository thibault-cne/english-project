<script lang="ts">
	const url = 'https://large-text-to-speech.p.rapidapi.com/tts';

	const options = {
		method: 'POST',
		headers: {
			'content-type': 'application/json',
			'X-RapidAPI-Key': 'ef5f346a6amshe835ef743c94db9p10a9bfjsn401acd3872d0',
			'X-RapidAPI-Host': 'large-text-to-speech.p.rapidapi.com'
		},
		body: '{"text":"Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away."}'
	};

	fetch(url, options)
		.then((res) => res.json())
		.then((json) => console.log(json))
		.catch((err) => console.error('error:' + err));
</script>
