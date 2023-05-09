import axios, { AxiosError } from 'axios';

export interface IHandCard {
	text: string;
	selected: boolean;
}

export interface IUser {
	is_czar: boolean;
}

export const getHand = (user: IUser): IHandCard[] => {
	return [
		{ text: 'asdad', selected: false },
		{ text: 'asdad', selected: false },
		{ text: 'asdad', selected: false },
		{ text: 'asdadada', selected: false },
		{ text: 'saadasds', selected: false },
		{ text: 'saadasds', selected: false }
	];
};

export interface IHTMLElement extends HTMLElement {
	tabIndex: number;
}

export function isAxiosError<ResponseType>(error: unknown): error is AxiosError<ResponseType> {
	return axios.isAxiosError(error);
}
