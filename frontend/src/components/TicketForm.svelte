<script>
  export let pricing;
  export let zoneTier;
  export let date;
  export let seats;

  // Confirm and Cancel handlers
  function confirmSelection() {
    alert(`You confirmed the seats: ${seats.join(', ')} in ${pricing.zone}.`);
    // Add logic for proceeding with confirmation (e.g., reserve seats via API)
  }

  function cancelSelection() {
    alert("You canceled your seat selection.");
    // Add logic for canceling the selection (e.g., reset selected seats)
  }
</script>

<div class="info-container">
  <div class="has-background-white p-4 info-box">
    <div class="info-list"><span>Round:</span> {date}</div>
    <div class="info-list"><span>Zone:</span> {pricing.zone}</div>
    <div class="info-list"><span>Seat No:</span> {seats}</div>
    <div class="info-list"><span>Quantity:</span> {seats.length}</div>
    <div class="info-list"><span>Unit Price:</span> {zoneTier.price}</div>
    <div class="info-list"><span>Total Price:</span> {zoneTier.price * seats.length}</div>
    <div class="buttons-container">
      <button class="button is-danger" on:click={cancelSelection}>Cancel</button>
      <button class="button is-success" on:click={confirmSelection}>Confirm</button>
    </div>
  </div>
</div>

<style>
  .info-container {
    display: flex;
    justify-content: center;
    color: black;
  }

  .info-box {
    border-radius: 20px;
    width: 70%;
  }

  .info-list {
    border-bottom: 0.5px solid black;
    padding: 8px;
  }

  .info-list span {
    font-weight: bold;
  }

  .info-list:nth-child(6) {
    border-bottom: none;
  }

  .buttons-container {
    margin-top: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .button {
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 10px;
    cursor: pointer;
  }

  .button.is-success {
    background-color: #48c774;
    color: white;
    border: none;
  }

  .button.is-success:hover {
    background-color: #3ea562;
  }

  .button.is-danger {
    background-color: #f14668;
    color: white;
    border: none;
  }

  .button.is-danger:hover {
    background-color: #d73f5c;
  }
</style>
