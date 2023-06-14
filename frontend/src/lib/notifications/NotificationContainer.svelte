<script lang="ts">
	import { notification_store } from './index';
	import Notification from './Notification.svelte';
</script>

<div class="alerts-container" id="alerts-container">
	{#each $notification_store as notification}
		<Notification {notification} />
	{/each}
</div>

<style>
	.alerts-container {
		/* Fix position on right side of screen */
		position: fixed;
		right: 0px;
		top: 24px;
		margin-right: 0.5em;
		margin-left: auto;
		z-index: 1010;

		/* Flexbox */
		display: flex;
		flex-direction: column;

		/* Other */
		font-size: smaller;

		width: 10em;
	}
</style>
