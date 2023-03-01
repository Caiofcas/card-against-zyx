import { error } from '@sveltejs/kit';
import type { Load } from '@sveltejs/kit';

export const load: Load = ({ params }) => {
	if (params.id) {
		const room_number = parseInt(params.id);
		if (!Number.isNaN(room_number)) {
			return {
				room_number
			};
		}
	}

	throw error(404, 'Not Found');
};
