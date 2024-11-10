<script>
  
  export let pricing;
  export let zoneTier;
  export let date;
  export let seats

  // Subscribe to dateStore to get the current selected date
</script>

<div class="info-container">
  <div class="has-background-white p-4 info-box">
    <div class="info-list"><span>Round:</span>  {date}</div>
    <div class="info-list"><span>Zone:</span>  {pricing.zone}</div>
    <div class="info-list"><span>Seat No:</span>  {seats}</div>
    <div class="info-list"><span>Quantity:</span>  {seats.length}</div>
    <div class="info-list"><span>Unit Price:</span>  {zoneTier.price}</div>
    <div class="info-list"><span>Total Price:  {zoneTier.price*seats.length}</span></div>
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
</style>
