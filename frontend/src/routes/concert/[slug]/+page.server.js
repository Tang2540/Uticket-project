import { error } from '@sveltejs/kit'
import { concerts } from '../data.js'
 
export function load({ params }) {
    const concert = concerts.find((concert) => concert.slug === params.slug)
    if (!concert) throw error(404)
    return {
        concert
    }
}
 
 