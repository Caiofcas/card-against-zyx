import { writable } from 'svelte/store';

interface IUser {
	username: string;
}

export const user_store = writable<IUser | null>(null);
