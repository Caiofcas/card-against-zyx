import { supabase } from '$lib/supabaseClient';

export async function load() {
	const { data } = await supabase.from('CardSet').select();
	return {
		card_sets: data ?? []
	};
}
