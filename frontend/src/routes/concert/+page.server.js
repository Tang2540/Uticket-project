import { concerts } from "./data.js";

export function load() {
  return {
    summaries: concerts.map((concert) => ({ slug: concert.slug, title: concert.title })),
  };
}