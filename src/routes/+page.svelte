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
		<a href="/create_room" class="option-card">Create New Room</a>
		<a href="/join_room" class="option-card">Join Existing Room</a>
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

	.option-card {
		/* size */
		flex: 1;
		max-width: 200px;
		height: 20vh;

		border: 0;
		border-radius: 16px;
		margin: 10px;

		/* styling */
		background-color: var(--gray-2);
		line-height: 20vh;
		text-align: center;
		text-decoration: none;
		color: black;
	}
</style>
