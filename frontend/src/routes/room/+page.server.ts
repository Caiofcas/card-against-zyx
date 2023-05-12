import { fail } from '@sveltejs/kit';

import { CardSetsAPI } from '$lib/api/card_sets';
import { MatchesAPI } from '$lib/api/matches';
import type { ICreateMatchError } from '$lib/api/matches';
import { isAxiosError } from '$lib/utils.js';

export const load = async () => {
	try {
		const sets = await CardSetsAPI.list();
		return { sets };
	} catch (error: unknown) {
		if (isAxiosError<ICreateMatchError>(error)) {
			return fail(400, { errors: error.response?.data });
		}
		return { error };
	}
};

export const actions = {
	default: async ({ request }) => {
		const data = await request.formData();
		console.log(data);
		const treated_data = {
			winning_score: parseInt(data.get('winning_score')?.toString() || ''),
			available_sets: Array.from(data.entries())
				.filter(([key, val]) => key.startsWith('set-') && val == 'on')
				.map(([key, _]) => parseInt(key.split('-')[1]))
		};
		console.log(treated_data);

		if (treated_data.available_sets.length == 0) {
			return fail(400, {
				error: 'Must select at least one card set'
			});
		}

		try {
			const match = await MatchesAPI.create(treated_data);
			console.log(match);
			return {
				success: true,
				room: match
			};
		} catch (error: unknown) {
			if (isAxiosError<ICreateMatchError>(error)) {
				// console.log(error.message);
				// console.log(error.response?.data);
				// console.log(error.cause);
				return fail(400, { errors: error.response?.data });
			}
			return { error };
		}
	}
};
