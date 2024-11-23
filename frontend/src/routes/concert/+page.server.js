export const load = async ({fetch, params}) => {
  const res = await fetch('http://127.0.0.1:8000/event');
  const summaries = await res.json();

  return {
    summaries: summaries
  }
}