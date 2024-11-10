<script>
  import { dateStore,seatStore } from "../routes/store.js";
  
  export let pricing;
  export let zoneTier;
  export let date;

  // Subscribe to dateStore to get the current selected date
  $: date = $dateStore;
  $: seats = $seatStore;
</script>

<div class="p-2 has-background-white">
  <div>
    <div><span>Round:</span> {date}</div>
    <div><span>Zone:</span> {pricing.zone}</div>
    <div><span>Seat No:</span> {seats}</div>
    <div><span>Quantity:</span> {seats.length}</div>
    <div><span>Unit Price:</span> {zoneTier.price}</div>
    <div><span>Total Price:</span> {zoneTier.price*seats.length}</div>
  </div>
</div>
