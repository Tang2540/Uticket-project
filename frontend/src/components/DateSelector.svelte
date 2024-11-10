<script>
  import { dateStore } from "../routes/store.js";

  export let dates;
  let selectedDate = null;

  function setUser(date) {
    console.log(date);
    if (selectedDate === date) {
      selectedDate = null;
      dateStore.set(null); 
    } else {
      selectedDate = date;
      dateStore.set(date); 
    }
    console.log($dateStore); 
  }
</script>

<div
  style="display:flex; flex-direction:column; gap:1rem; margin-top:2rem; margin-bottom:2rem"
>
  {#each dates as date}
    <button
      class:selected={selectedDate === date.date}
      on:click={() => setUser(date.date)}
      transition:fade
    >
      {date.date}
    </button>
  {/each}
</div>

<style>
  button {
    color: white;
    height: 3rem;
    border: 2px solid white;
    border-radius: 20px;
    transition: all 0.2s;
  }

  button:hover {
    border-width: 5px;
  }

  .selected {
    background-color: #FB2576;
  }
</style>
