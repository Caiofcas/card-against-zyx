import type { CreateAxiosDefaults } from 'axios';
const axios_config: CreateAxiosDefaults = {
	// TODO: get from env vars
	baseURL: 'http://django:8000/api/v1/',
	headers: {
		'Content-Type': 'application/json'
	}
};

export default axios_config;
