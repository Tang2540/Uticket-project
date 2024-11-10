import { error } from '@sveltejs/kit';
import { concerts } from '../../data.js';

export function load({ params }) {
    const { slug, zone } = params;

    // Find concert
    const concert = concerts.find((concert) => concert.slug === slug);
    if (!concert) {
        throw error(404, {
            message: 'Concert not found'
        });
    }

    const pricing = concert.pricing.find((price) => price.zone === zone);
    if (!pricing) {
        throw error(404, {
            message: 'Pricing tier not found'
        });
    }

    const zoneTier = concert.zone_tier.find((zone) => zone.tier === pricing.zone_tier_id)
    if (!zoneTier) {
        throw error(404, {
            message: 'zone tier not found'
        });
    }

    return {
        concert,
        pricing,
        zoneTier
    };
}