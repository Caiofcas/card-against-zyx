<script lang="ts">
	import type { PageData } from './$types';
	export let data: PageData;
    $: {
        console.log(data);
    }
	let { card_sets } = data;
	$: ({ card_sets } = data);
</script>

<ul>
	{#each card_sets as set}
		<li>{set.name}</li>
	{/each}
</ul>
