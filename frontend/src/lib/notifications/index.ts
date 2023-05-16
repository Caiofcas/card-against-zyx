import { writable } from 'svelte/store';

// types
export interface INotification {
	text: string;
	is_error?: boolean;
}

// store
export const notification_store = writable<INotification[]>([]);

// functions
export function addNotification(notification: INotification) {
	notification_store.update((current) => [...current, notification]);
}
