import { error } from '@sveltejs/kit';
import { concerts } from '../../data.js';

export function load({ params }) {
    const { slug, tier } = params;

    // Find concert
    const concert = concerts.find((concert) => concert.slug === slug);
    if (!concert) {
        throw error(404, {
            message: 'Concert not found'
        });
    }

    const pricing = concert.pricing.find((price) => price.tier === tier);
    if (!pricing) {
        throw error(404, {
            message: 'Pricing tier not found'
        });
    }

    return {
        concert,
        pricing
    };
}