import { writable } from 'svelte/store';

// types
export interface INotificationCreate {
	text: string;
	is_error?: boolean;
}

export interface INotification extends INotificationCreate {
	hash: number;
}

// store
export const notification_store = writable<INotification[]>([]);

// functions
function hashString(s: string) {
	return s.split('').reduce(function (a, b) {
		a = (a << 5) - a + b.charCodeAt(0);
		return a & a;
	}, 0);
}

export function addNotification(notification: INotificationCreate) {
	notification_store.update((current) => [
		...current,
		{ ...notification, hash: hashString(notification.text) }
	]);
}

export function removeNotification(notification: INotification) {
	notification_store.update((current) => current.filter((not) => not.hash != notification.hash));
}
