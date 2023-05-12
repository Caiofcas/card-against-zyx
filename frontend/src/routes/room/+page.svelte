<script lang="ts">
	import type { ActionData, PageServerData } from './$types';

	export let form: ActionData;
	export let data: PageServerData;

	const card_sets = data.sets ?? [];
</script>

<svelte:head>
	<title>Create Room</title>
</svelte:head>

{#if form?.error}
	<p class="error">{form.error}</p>
{/if}

{#if data?.error}
	<p class="error">{data.error}</p>
{/if}

<form method="POST">
	<label>
		Winning Score:
		<input type="number" name="winning_score" min="1" max="20" value="7" />
	</label>
	<div class="card_set_selector">
		{#each card_sets as set}
			<label>
				<input type="checkbox" name="set-{set.id}" />
				{set.name}
			</label>
		{/each}
	</div>
	<input type="submit" value="Create Room" />
</form>

<br />

{#if form?.success}
	<p>Successfully created room {form.room?.id}!</p>
{/if}

<style>
	.card_set_selector {
		display: flex;
		flex-direction: column;
	}
</style>
