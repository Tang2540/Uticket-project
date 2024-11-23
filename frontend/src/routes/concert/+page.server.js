export const load = async ({ fetch, params }) => {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  
  return {
    summaries: concerts.map((concert) => ({ slug: concert.slug, title: concert.title, venue: concert.venue, status: concert.status, cardImg: concert.cardImg, date: concert.date }))
  };
};

export function load() {
  return {
    summaries: concerts.map((concert) => ({ slug: concert.slug, title: concert.title, venue: concert.venue, status: concert.status, cardImg: concert.cardImg, date: concert.date })),
  };
}