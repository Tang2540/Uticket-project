<script>
  export let selectedZone;
  let selectedSeats = [];

  export let concert

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
  <div class="seat-map-container">
  <div class="zone-col">
    <div style="height:40px" class="text-box">A</div>
    <div style="height:40px" class="text-box">B</div>
    <div style="height:40px" class="text-box">C</div>
    <div style="height:40px" class="text-box">D</div>
  </div>
  <div class="seats-grid">
    {#each concert.seats as seat}
      <button
        class="seat-button"
        class:seat-selected={selectedSeats.includes(seat.id + 1)}
        on:click={() => toggleSeat(seat.id + 1)}
        disabled={selectedSeats.length >= 4 &&
          !selectedSeats.includes(seat.id + 1)}
      >
        {seat.No}
      </button>
    {/each}
  </div>
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

  .seat-map-container {
    display: flex;
  }
  .seats-grid {
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    gap: 0.45rem; /* Reduced gap for closer seats */
    margin-top: 1rem;
    flex-grow: 1;
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
    background-color: #920eff; 
  }

  .zone-col {
    display: flex;
    flex-direction: column;
    margin-top: 1rem;
    margin-right: 1rem;
    justify-content: center;
    align-items: start;
    height: 100%;
    gap: 0.45rem;
  }

  .text-box {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
</style>
