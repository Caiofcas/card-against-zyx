<script lang="ts">
	import WhiteCard from '$lib/WhiteCard.svelte';
	import type { IHandCard } from '$lib/utils';

	export let hand: IHandCard[];
	export let max_selected = 1;

	let current_selected = 0;

	function handleClick(i: number) {
		if (!hand[i].selected) {
			if (current_selected >= max_selected) {
				return;
			} else {
				current_selected += 1;
			}
		} else {
			current_selected -= 1;
		}
		hand[i].selected = !hand[i].selected;
	}
</script>

<div class="hand">
	{#each hand as card, i}
		<div on:click={() => handleClick(i)} on:keypress={() => handleClick(i)}>
			<WhiteCard text={card.text} selected={card.selected} />
		</div>
	{/each}
</div>

<style>
	.hand {
		display: flex;
		flex-direction: row;
	}
</style>
