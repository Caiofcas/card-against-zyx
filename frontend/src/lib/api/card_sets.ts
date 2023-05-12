import axios from 'axios';
import axios_config from './axios_config';

const api = axios.create({
	...axios_config,
	baseURL: axios_config.baseURL + 'card_sets/'
});

export interface ICardSet {
	id: number;
	name: string;
	official: boolean;
}

export const CardSetsAPI = {
	list: async () => {
		const resp = await api.get<ICardSet[]>('');
		return resp.data;
	}
};
