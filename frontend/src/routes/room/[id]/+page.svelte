<script lang="ts">
	import '../../styles.css';
	import BlackCard from '$lib/BlackCard.svelte';
	import Hand from '$lib/Hand.svelte';
	import DisabledHand from '$lib/DisabledHand.svelte';
	import { getHand } from '$lib/utils';
	import type { PageData } from './$types';

	export let data: PageData;

	let user = {
		is_czar: false
	};

	let hand = getHand(user);
	let max_selected = 2;
</script>

<svelte:head>
	<title>Room {data.room_number}</title>
</svelte:head>

<h1>Room {data.room_number}</h1>

{#if user.is_czar}
	<div class="czar_text">
		<span> You are the czar, select one of the cards choosen by the other players: </span>
	</div>
	<div class="czar_row">
		<BlackCard />
		<div class="czar_text">
			<span> <i> Players are still selecting. </i> </span>
		</div>
	</div>
	<DisabledHand />
{:else}
	<BlackCard />
	<br />
	<Hand {hand} {max_selected} />
{/if}

<style>
	.czar_row {
		display: flex;
		flex-direction: row;
		height: auto;
		/* border: solid 3px black; */
	}

	.czar_text {
		font-weight: 600;
		font-size: x-large;
		width: 100%;
		display: flex;
		justify-content: center;
		margin: auto;
	}
</style>
