<script lang="ts">
	import '../../styles.css';
	import BlackCard from '$lib/BlackCard.svelte';
	import Hand from '$lib/Hand.svelte';
	import type { PageData } from './$types';

	export let data: PageData;

	export let my_hand = [
		{ text: 'asdad', selected: false },
		{ text: 'asdad', selected: false },
		{ text: 'asdad', selected: false },
		{ text: 'asdadada', selected: false },
		{ text: 'saadasds', selected: false }
	];

	let max_selected = 2;
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

<svelte:head>
	<title>Room {data.room_number}</title>
</svelte:head>

<h1>Room {data.room_number}</h1>

<BlackCard />

<br />

<Hand />
