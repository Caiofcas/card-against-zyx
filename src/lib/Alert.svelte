<!-- Shamelessly stolen from https://www.ryanfiller.com/blog/building-an-alert-component-in-svelte -->
<script lang="ts">
	import type { IHTMLElement } from '$lib/utils';

	export let show: boolean;
	export let close: () => void = () => {};
	export let title: string;

	const id = title;

	const elements = ['a', 'button', 'input', 'textarea', 'select', 'details', '[tabindex]'];

	function focusTrap(element: IHTMLElement) {
		element.focus();
		const focusableElements = [
			...element.querySelectorAll<IHTMLElement>(elements.join(', '))
		].filter((element) => !(element.hasAttribute('disabled') || element.tabIndex === -1));

		element.addEventListener('keydown', (event: any) => {
			if (event.key === 'Tab' || event.keyCode === 9) {
				const activeElement = document.activeElement;

				if (activeElement) {
					const currentElementIndex = focusableElements.findIndex((value) => {
						return (value.id = activeElement.id);
					});
					event.preventDefault();

					if (event.shiftKey) {
						currentElementIndex === 0
							? focusableElements[focusableElements.length - 1].focus()
							: focusableElements[currentElementIndex - 1].focus();
					} else {
						currentElementIndex === focusableElements.length - 1
							? focusableElements[0].focus()
							: focusableElements[currentElementIndex + 1].focus();
					}
				}
			}
		});
	}
</script>

<svelte:window
	on:keydown={(event) => {
		event.key === 'Escape' ? close() : null;
	}}
/>

{#if show}
	<dialog
		open
		on:click={close}
		on:keypress={close}
		aria-labelledby={`${id}-title`}
		aria-describedby={`${id}-content`}
		tabindex="-1"
		use:focusTrap
	>
		<section>
			<header id={`${id}-title`}>
				<strong>
					{title}
				</strong>
				<button on:click={close}> Close </button>
			</header>

			<div id={`${id}-content`}>
				<slot />
			</div>
		</section>
	</dialog>
{/if}

<style>
	dialog {
		position: fixed;
		top: 0;
		right: 0;
		left: 0;
		bottom: 0;
		z-index: 9999;
		height: 100%;
		width: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		background: transparent;
	}

	dialog::after {
		content: '';
		display: block;
		position: absolute;
		top: 0;
		right: 0;
		bottom: 0;
		left: 0;
		background: black;
		opacity: 0.5;
		z-index: -1;
		pointer-events: none;
	}

	section {
		width: 100%;
		max-width: 50rem;
		background: white;
	}
</style>
