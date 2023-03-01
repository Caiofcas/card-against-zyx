import { createClient } from '@supabase/supabase-js';
import { config } from 'dotenv';
import fs from 'fs';
import path from 'path';

config();

const args = process.argv;

if (args.length < 3) {
	console.log('Must provide json file path as argument');
	process.exit(1);
}

// Create a single supabase client for interacting with your database
const supabase = createClient(
	process.env.VITE_SUPABASE_URL || '',
	process.env.VITE_SUPABASE_TOKEN || ''
);

interface Card {
	text: string;
	pack: number;
}

interface BlackCard extends Card {
	pick: number;
}

interface Pack {
	name: string;
	official: boolean;
	white: Card[];
	black: BlackCard[];
}

const cards_fn = args[2];

const packs: Pack[] = JSON.parse(fs.readFileSync(cards_fn).toString());

function removeDuplicates<T extends { text: string }>(cards: T[]): T[] {
	let set = new Set();
	let filteredCards: typeof cards = [];

	cards.forEach((cur_card) => {
		if (set.has(cur_card.text)) {
			return filteredCards;
		}
		set.add(cur_card.text);
		filteredCards.push(cur_card);
	});

	return filteredCards;
}

const updateDB = async (packs: Pack[]) => {
	for (let index = 0; index < packs.length; index++) {
		const pack = packs[index];

		console.log(`> Updating Pack: ${pack.name}`);

		pack.white = removeDuplicates(pack.white);
		pack.black = removeDuplicates(pack.black);

		await supabase.from('CardSet').upsert({ name: pack.name }, { onConflict: 'name' }).select();

		await supabase
			.from('Card')
			.upsert(
				pack.white.map((card) => {
					return {
						set: pack.name,
						text: card.text,
						color: 'WHITE'
					};
				}),
				{
					onConflict: 'text, color'
				}
			)
			.select();

		console.log('>>> Inserted White Cards');

		const { error } = await supabase
			.from('Card')
			.upsert(
				pack.black.map((card) => {
					return {
						set: pack.name,
						text: card.text,
						color: 'BLACK',
						slots: card.pick
					};
				}),
				{
					onConflict: 'text'
				}
			)
			.select();

		if (error) {
			console.error(error);
		}

		console.log('>>> Inserted Black Cards');
	}
};

updateDB(packs).finally(() => {
	process.exit();
});
