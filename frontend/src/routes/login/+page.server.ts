import { fail } from '@sveltejs/kit';

import { AccountsAPI } from '$lib/api/accounts';
import type { ICreateMatchError } from '$lib/api/matches';
import { isAxiosError } from '$lib/utils.js';

export const actions = {
	default: async ({ request }) => {
		const data = await request.formData();
		console.log(data);
		const treated_data = {
			username: data.get('username')?.toString() || '',
			password: data.get('password')?.toString() || ''
		};
		console.log(treated_data);

		if (treated_data.username === '') {
			return fail(400, {
				error: { message: 'username must be entered' }
			});
		}

		if (treated_data.password === '') {
			return fail(400, {
				error: { message: 'password must be entered' }
			});
		}

		try {
			const user = await AccountsAPI.login(treated_data.username, treated_data.password);
			console.log(user);
			return {
				success: true,
				user
			};
		} catch (error: unknown) {
			if (isAxiosError<ICreateMatchError>(error)) {
				// console.log(error.message);
				// console.log(error.response?.data);
				// console.log(error.cause);
				return fail(400, { errors: error.response?.data });
			}
			return { error: { error, message: 'Unknown error' } };
		}
	}
};
