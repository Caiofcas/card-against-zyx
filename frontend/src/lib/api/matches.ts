import axios from 'axios';
import axios_config from './axios_config';

const api = axios.create({
	...axios_config,
	baseURL: axios_config.baseURL + 'matches/'
});

export interface ICreateMatch {
	winning_score: number;
	available_sets: number[];
}

export interface ICreateMatchError {
	available_sets: string[];
}

export interface IMatch extends ICreateMatch {
	id: number;
}

export const MatchesAPI = {
	create: async (data: ICreateMatch) => {
		const resp = await api.post<IMatch>('', data);
		return resp.data;
	}
};
