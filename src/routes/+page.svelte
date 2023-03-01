<script>
	import './styles.css';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section class="main">
	<div class="title">
		<h1>Cards Against ZYX</h1>
	</div>

	<div class="options">
		<button class="option-btn">Create New Room</button>
		<button class="option-btn">Join Existing Room</button>
	</div>
</section>

<style>
	.title {
		width: 100%;
		text-align: center;
	}

	.options {
		display: flex;
		justify-content: center;
		width: 80%;
		margin: auto;
	}

	.option-btn {
		flex: 1;
		max-width: 200px;
		height: 20vh;
		border: 0;
		border-radius: 16px;
		margin: 10px;
		background-color: var(--gray-2);
	}
</style>
