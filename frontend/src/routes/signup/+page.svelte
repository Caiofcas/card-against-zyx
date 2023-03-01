<script lang="ts">
	import { supabase } from '$lib/supabaseClient';
	import Alert from '$lib/Alert.svelte';

	async function onSubmit() {
		const data = await supabase.auth.signUp({
			email: 'caiofcastro@usp.br',
			password: 'senha123'
		});
	}

	let showAlert = false;

	function closeAlert() {
		showAlert = false;
	}

	function openAlert() {
		showAlert = true;
	}

</script>

<button on:click={openAlert}> Cria Usuário </button>

<Alert title="Caution!" show={showAlert} close={closeAlert}>
	<p>
		Some features in the section require JavaScript, might not work great on mobile, and may not
		have been thoroughly tested.
	</p>

	<button on:click={closeAlert}> That's okay. </button>
</Alert>
