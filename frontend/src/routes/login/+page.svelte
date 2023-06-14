<!-- TODO: Page is broken -->
<script lang="ts">
	import type { ActionData, PageServerData } from './$types';
	import { user_store } from '$lib/auth';
	import { addNotification } from '$lib/notifications';
	export let form: ActionData;

	if (form?.error && form.error.message) {
		addNotification({ text: form.error.message, is_error: true });
	}

	let username = '';
	let password = '';
	let error = '';
</script>

{#if $user_store != null}
	Logged in as {$user_store.username}
{:else}
	Not logged in
{/if}
<br />
<br />

<form method="POST">
	<div>
		<label for="username">
			Username
			<input type="text" name="username" bind:value={username} />
		</label>
	</div>

	<div>
		<label for="password">
			Password
			<input type="password" name="password" bind:value={password} />
		</label>
	</div>

	<input class="submit-button" type="submit" value="Login" />
	<div id="error_message">
		<small>{error}</small>
	</div>
</form>

<style>
</style>
