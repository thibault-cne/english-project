<script lang="ts">
	import '@skeletonlabs/skeleton/themes/theme-modern.css';

	import '@skeletonlabs/skeleton/styles/all.css';

	import '../app.postcss';

	import { AppShell } from '@skeletonlabs/skeleton';

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

<AppShell>
	<svelte:fragment slot="header"
		><div class="navbar bg-surface-700 z-10">
			<div class="flex-1">
				<a class="btn btn-ghost normal-case text-xl" href="/">EnglishEasy</a>
			</div>
			<div class="flex-none">
				<ul class="menu menu-horizontal px-1">
					<li><a href="/fun-fact" class="unstyled btn btn-ghost">Fun fact</a></li>
					<li><a href="/scramble" class="unstyled btn btn-ghost">Scramble</a></li>
					<li><a href="/qcm" class="unstyled btn btn-ghost">QCM</a></li>
					<li tabindex="-1" class="font-semibold">
						<span>
							True or false
							<svg
								class="fill-current"
								xmlns="http://www.w3.org/2000/svg"
								width="20"
								height="20"
								viewBox="0 0 24 24"
								><path d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z" /></svg
							>
						</span>
						<ul class="p-2 bg-surface-700 z-10">
							<li class="z-10">
								<a href="/torf/playground" class="unstyled btn btn-ghost">Playground</a>
							</li>
							<li class="z-10">
								<a href="/torf/exam" class="unstyled btn btn-ghost">Exam</a>
							</li>
						</ul>
					</li>
					<li tabindex="-1" class="font-semibold">
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
						<ul class="p-2 bg-surface-700 z-10">
							{#each lessons as lesson}
								<li class="z-10">
									<a href={lesson.href} class="unstyled btn btn-ghost">{lesson.title}</a>
								</li>
							{/each}
						</ul>
					</li>
					<li><a href="/irregular-verbs" class="unstyled btn btn-ghost">Irregular verbs</a></li>
				</ul>
			</div>
		</div>
	</svelte:fragment>
	<div class="z-0 p-10">
		<slot />
	</div>
</AppShell>

<style>
	.navbar {
		display: flex;
		align-items: center;
		padding: var(--navbar-padding, 0.5rem);
		min-height: 4rem /* 64px */;
		width: 100%;
	}
	:where(.navbar > *) {
		display: inline-flex;
		align-items: center;
	}

	.menu {
		display: flex;
		flex-direction: column;
		flex-wrap: wrap;
	}
	:where(.menu li) {
		position: relative;
		display: flex;
		flex-shrink: 0;
		flex-direction: column;
		flex-wrap: wrap;
		align-items: stretch;
	}
	.menu :where(li:not(.menu-title)) > :where(*:not(ul)) {
		display: flex;
	}
	.menu :where(li:not(.disabled):not(.menu-title)) > :where(*:not(ul)) {
		cursor: pointer;
		user-select: none;
		align-items: center;
		outline: 2px solid transparent;
		outline-offset: 2px;
	}
	.menu > :where(li > *:not(ul):focus) {
		outline: 2px solid transparent;
		outline-offset: 2px;
	}
	.menu > :where(li.disabled > *:not(ul):focus) {
		cursor: auto;
	}
	.menu > :where(li) :where(ul) {
		display: flex;
		flex-direction: column;
		align-items: stretch;
	}
	.menu > :where(li) > :where(ul) {
		position: absolute;
		display: none;
		top: initial;
		left: 100%;
		border-top-left-radius: inherit;
		border-top-right-radius: inherit;
		border-bottom-right-radius: inherit;
		border-bottom-left-radius: inherit;
	}
	.menu > :where(li:hover) > :where(ul) {
		display: flex;
	}
	.menu > :where(li:focus) > :where(ul) {
		display: flex;
	}
	.menu li > * {
		border-radius: var(--rounded-btn, 0.5rem);
	}
	.menu :where(li.bordered > *) {
		border-left-width: 4px;
		--tw-border-opacity: 1;
		border-color: rgb(var(--color-primary-500) / var(--tw-border-opacity));
	}
	.menu :where(li) > :where(*:not(ul)) {
		gap: 0.75rem /* 12px */;
		padding-left: 1rem /* 16px */;
		padding-right: 1rem /* 16px */;
		padding-top: 0.75rem /* 12px */;
		padding-bottom: 0.75rem /* 12px */;
		color: currentColor;
	}
	.menu :where(li:not(.menu-title):not(:empty)) > :where(*:not(ul):focus),
	.menu :where(li:not(.menu-title):not(:empty)) > :where(*:not(ul):hover) {
		background-color: rgb(var(--color-surface-100) / var(--tw-bg-opacity));
		--tw-bg-opacity: 0.1;
	}
	.menu :where(li:not(.menu-title):not(:empty)) > :where(*:not(ul):focus),
	.menu :where(li:not(.menu-title):not(:empty)) > :where(*:not(ul):hover) {
		background-color: rgb(var(--color-surface-100) / var(--tw-bg-opacity));
		--tw-bg-opacity: 0.1;
	}
	.menu :where(li:not(.menu-title):not(:empty)) > :where(:not(ul).active),
	.menu :where(li:not(.menu-title):not(:empty)) > :where(*:not(ul):active) {
		--tw-bg-opacity: 1;
		background-color: rgb(var(--color-primary-500) / var(--tw-bg-opacity));
		--tw-text-opacity: 1;
		color: rgb(var(--color-primary-100) / var(--tw-text-opacity));
	}
	.menu :where(li:not(.menu-title):not(:empty)) > :where(:not(ul).active),
	.menu :where(li:not(.menu-title):not(:empty)) > :where(*:not(ul):active) {
		--tw-bg-opacity: 1;
		background-color: rgb(var(--color-primary-500) / var(--tw-bg-opacity));
		--tw-text-opacity: 1;
		color: rgb(var(--theme-font-color-dark) / var(--tw-text-opacity));
	}
	.menu :where(li:empty) {
		margin-left: 1rem /* 16px */;
		margin-right: 1rem /* 16px */;
		margin-top: 0.5rem /* 8px */;
		margin-bottom: 0.5rem /* 8px */;
		height: 1px;
		background-color: rgb(var(--color-surface-100) / var(--tw-bg-opacity));
		--tw-bg-opacity: 0.1;
	}
	.menu :where(li:not(.disabled)) > :where(*:not(ul)) {
		outline: 2px solid transparent;
		outline-offset: 2px;
		transition-property: color, background-color, border-color, text-decoration-color, fill, stroke,
			opacity, box-shadow, transform, filter, backdrop-filter;
		transition-duration: 200ms;
		transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
	}
	.menu > :where(li:first-child) {
		border-top-left-radius: inherit;
		border-top-right-radius: inherit;
		border-bottom-right-radius: unset;
		border-bottom-left-radius: unset;
	}
	.menu > :where(li:first-child) > :where(:not(ul)) {
		border-top-left-radius: inherit;
		border-top-right-radius: inherit;
		border-bottom-right-radius: unset;
		border-bottom-left-radius: unset;
	}
	.menu > :where(li:last-child) {
		border-top-left-radius: unset;
		border-top-right-radius: unset;
		border-bottom-right-radius: inherit;
		border-bottom-left-radius: inherit;
	}
	.menu > :where(li:last-child) > :where(:not(ul)) {
		border-top-left-radius: unset;
		border-top-right-radius: unset;
		border-bottom-right-radius: inherit;
		border-bottom-left-radius: inherit;
	}
	.menu > :where(li) > :where(ul) :where(li) {
		width: 100%;
		white-space: nowrap;
	}
	.menu > :where(li) > :where(ul) :where(li) :where(ul) {
		padding-left: 1rem /* 16px */;
	}
	.menu > :where(li) > :where(ul) :where(li) > :where(:not(ul)) {
		width: 100%;
		white-space: nowrap;
	}
	.menu > :where(li) > :where(ul) > :where(li:first-child) {
		border-top-left-radius: inherit;
		border-top-right-radius: inherit;
		border-bottom-right-radius: unset;
		border-bottom-left-radius: unset;
	}
	.menu > :where(li) > :where(ul) > :where(li:first-child) > :where(:not(ul)) {
		border-top-left-radius: inherit;
		border-top-right-radius: inherit;
		border-bottom-right-radius: unset;
		border-bottom-left-radius: unset;
	}
	.menu > :where(li) > :where(ul) > :where(li:last-child) {
		border-top-left-radius: unset;
		border-top-right-radius: unset;
		border-bottom-right-radius: inherit;
		border-bottom-left-radius: inherit;
	}
	.menu > :where(li) > :where(ul) > :where(li:last-child) > :where(:not(ul)) {
		border-top-left-radius: unset;
		border-top-right-radius: unset;
		border-bottom-right-radius: inherit;
		border-bottom-left-radius: inherit;
	}

	.menu-horizontal {
		display: inline-flex;
		width: max-content;
		flex-direction: row;
	}
	.menu-horizontal :where(li) {
		flex-direction: row;
	}
	.menu-horizontal > :where(li) > :where(ul) {
		top: 100%;
		left: initial;
	}
	.menu-horizontal :where(li.bordered > *) {
		border-left-width: 0px;
		border-bottom-width: 4px;
	}
	.menu-horizontal > :where(li:first-child) {
		border-top-left-radius: inherit;
		border-top-right-radius: unset;
		border-bottom-right-radius: unset;
		border-bottom-left-radius: inherit;
	}
	.menu-horizontal > :where(li:first-child) > :where(*:not(ul)) {
		border-top-left-radius: inherit;
		border-top-right-radius: unset;
		border-bottom-right-radius: unset;
		border-bottom-left-radius: inherit;
	}
	.menu-horizontal > :where(li:last-child) {
		border-top-left-radius: unset;
		border-top-right-radius: inherit;
		border-bottom-right-radius: inherit;
		border-bottom-left-radius: unset;
	}
	.menu-horizontal > :where(li:last-child) > :where(*:not(ul)) {
		border-top-left-radius: unset;
		border-top-right-radius: inherit;
		border-bottom-right-radius: inherit;
		border-bottom-left-radius: unset;
	}
</style>
