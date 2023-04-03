<script lang="ts">
	import '../app.css';

	let lessons = [
		{
			href: '/lessons/01',
			title: 'Lesson - 01'
		},
		{
			href: '/lessons/02',
			title: 'Lesson - 02'
		},
		{
			href: '/lessons/03',
			title: 'Lesson - 03'
		},
		{
			href: '/lessons/04',
			title: 'Lesson - 04'
		},
		{
			href: '/lessons/05',
			title: 'Lesson - 05'
		},
		{
			href: '/lessons/06',
			title: 'Lesson - 06'
		}
	];
</script>

<div class="navbar bg-base-100 z-10">
	<div class="flex-1">
		<a class="btn btn-ghost normal-case text-xl" href="/">EnglishEasy</a>
	</div>
	<div class="flex-none">
		<ul class="menu menu-horizontal px-1">
			<li><a href="/fun-fact">Fun fact</a></li>
			<li><a href="/torf">True or false</a></li>
			<li tabindex="-1">
				<span>
					Lessons
					<svg
						class="fill-current"
						xmlns="http://www.w3.org/2000/svg"
						width="20"
						height="20"
						viewBox="0 0 24 24"
						><path d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z" /></svg
					>
				</span>
				<ul class="p-2 bg-base-100 z-10">
					{#each lessons as lesson}
						<li class="z-10"><a href={lesson.href}>{lesson.title}</a></li>
					{/each}
				</ul>
			</li>
			<li><a href="/irregular-verbs">Irregular verbs</a></li>
		</ul>
	</div>
</div>
<div class="z-0">
	<slot />
</div>
