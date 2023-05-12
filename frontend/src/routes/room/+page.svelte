<script lang="ts">
	import type { ActionData, PageServerData } from './$types';
	import Alert from '$lib/Alert.svelte';

	export let form: ActionData;
	export let data: PageServerData;

	let alert_title = '';
	const close = () => {
		alert_title = '';
	};

	if (form?.error && form.error.message) {
		alert_title = form.error.message;
	} else if (data?.error) {
		alert_title = 'Error retrieving card sets';
	} else if (form?.success) {
		alert_title = `Successfully created room ${form.room?.id}!`;
	}

	const card_sets = data.sets ?? [];
</script>

<svelte:head>
	<title>Create Room</title>
</svelte:head>

<!-- TODOs
	- add search for cardsets
	- style alerts
	- add positive and negative styles to alerts (do this on component)
-->

<Alert show={alert_title != ''} {close} title={alert_title} />

<div class="form-container">
	<h1>Create Room</h1>
	<form method="POST" class="form">
		<label>
			Winning Score:
			<input type="number" name="winning_score" min="1" max="20" value="7" />
		</label>
		<div class="card-set-selector">
			<strong>Select Card Sets</strong>
			<br />
			<div class="card-set-list">
				{#each card_sets as set}
					<div class="set-container">
						<label>
							<input type="checkbox" name="set-{set.id}" />
							{set.name}
						</label>
					</div>
				{/each}
			</div>
		</div>
		<input class="submit-button" type="submit" value="Create Room" />
	</form>
</div>

<br />

<style>
	.card-set-selector {
		margin-top: 15px;
	}
	.card-set-list {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		height: 50%;
		width: 95%;
		margin: auto;
	}
	.set-container {
		padding: 3px;
		margin-top: 5px;
		margin-right: 5px;
	}
	.set-container:hover {
		background-color: gainsboro;
	}
	.form-container {
		margin: auto;
		width: 50%;
		padding: 20px;
	}
	.form {
		display: flex;
		flex-direction: column;
	}
	.submit-button {
		max-width: 30%;
		margin: auto;
	}
</style>
