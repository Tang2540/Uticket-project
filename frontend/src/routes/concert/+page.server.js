<<<<<<< HEAD
export const load = async ({ fetch, params }) => {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  
  return {
    summaries: concerts.map((concert) => ({ slug: concert.slug, title: concert.title, venue: concert.venue, status: concert.status, cardImg: concert.cardImg, date: concert.date }))
  };
};
=======
export const load = async ({fetch, params}) => {
  const res = await fetch('http://127.0.0.1:8000/event');
  const summaries = await res.json();
>>>>>>> dd7dc1e3226b4807b63fb967d42b739507f69aa0

  return {
    summaries: summaries
  }
}