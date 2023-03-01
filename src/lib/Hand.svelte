<script lang="ts">
	import WhiteCard from '$lib/WhiteCard.svelte';

	export let my_hand = [
		{ text: 'asdad', selected: false },
		{ text: 'asdad', selected: false },
		{ text: 'asdad', selected: false },
		{ text: 'asdadada', selected: false },
		{ text: 'saadasds', selected: false }
	];

	export let max_selected = 1;
	let current_selected = 0;

	function handleClick(i: number) {
		if (!my_hand[i].selected) {
			if (current_selected >= max_selected) {
				return;
			} else {
				current_selected += 1;
			}
		} else {
			current_selected -= 1;
		}
		my_hand[i].selected = !my_hand[i].selected;
	}
</script>

<div class="hand">
	{#each my_hand as card, i}
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
