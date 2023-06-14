<script lang="ts">
	import type { INotification } from './index';
	import { removeNotification } from './index';
	export let notification: INotification;

	export let visible = true;

	function handleClose() {
		visible = false;
		removeNotification(notification);
	}
</script>

<div
	class="notification"
	class:notification-fail={notification.is_error || false}
	class:hidden={!visible}
>
	<span>{notification.text}</span>
	<img
		class="notification-close"
		src="/close_icon.svg"
		alt="close"
		on:click={handleClose}
		on:keydown={() => {}}
		on:keypress={() => {}}
	/>
</div>

<style>
	.notification {
		/* Sizes */
		max-width: 10em;
		min-width: 4em;
		padding: 1em 0.5em 1em 1em;
		margin-bottom: 0.2em;
		border-radius: 0.5em;
		border: 0px;

		/* Coloring */
		background-color: #fefefe;
		box-shadow: 0 3px 6px -4px #0000001f, 0 6px 16px #00000014, 0 9px 28px 8px #0000000d;

		/* Text */
		font-size: 14px;
	}

	.notification-close {
		width: 1em;
		height: 1em;
		float: right;
		margin-left: 15px;
	}

	.notification-fail {
		background-color: #ffdada;
		border: 0.15em solid red;
		border-radius: 0em;
	}

	.hidden {
		display: none;
	}
</style>
