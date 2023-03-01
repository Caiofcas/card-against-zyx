<script lang="ts">
	import DisabledCard from "./DisabledCard.svelte";

	export let hand_size = 6;
</script>

<div class="hand">
	{#each Array(hand_size) as _, i}
		<div>
			<DisabledCard />
		</div>
	{/each}
</div>

<style>
	.hand {
		display: flex;
		flex-direction: row;
	}
</style>
