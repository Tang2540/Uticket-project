<script>
  export let selectedZone;
  let selectedSeats = [];

  function toggleSeat(seatNumber) {
    if (selectedSeats.includes(seatNumber)) {
      selectedSeats = selectedSeats.filter((seat) => seat !== seatNumber);
    } else if (selectedSeats.length < 4) {
      selectedSeats = [...selectedSeats, seatNumber];
    }
  }
  function resetSeatSelection() {
      selectedSeats = [];
    }
</script>

<div class="box seat-popup">
  <h2 class="title is-5">Select Seats in Zone {selectedZone}</h2>
  <div class="seats-grid">
    {#each Array(40) as _, index}
      <button
        class="seat-button"
        class:seat-selected={selectedSeats.includes(index + 1)}
        on:click={() => toggleSeat(index + 1)}
        disabled={selectedSeats.length >= 4 &&
          !selectedSeats.includes(index + 1)}
      >
        {index + 1}
      </button>
    {/each}
  </div>
  <button class="button is-danger mt-4" on:click={resetSeatSelection}
    >Close</button
  >
</div>

<style>
  .seat-popup {
    border: 2px solid #ff4eba;
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
  }
  .seats-grid {
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    gap: 0.45rem; /* Reduced gap for closer seats */
    margin-top: 1rem;
  }
  .seat-button {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #ff4eba;
    color: white;
    font-weight: bold;
    border: none;
    cursor: pointer;
  }
  .seat-selected {
    background-color: #920eff; /* Selected seat color */
  }
</style>
