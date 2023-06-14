import axios from 'axios';
import axios_config from './axios_config';

const api = axios.create({
	...axios_config,
	baseURL: axios_config.baseURL + 'accounts/'
});

export const AccountsAPI = {
	login: async (username: string, password: string) => {
		const resp = await api.post('login/', {
			username,
			password
		});
		console.log(resp.status);
		console.log(resp.data);
		return resp.data;
	}
};
