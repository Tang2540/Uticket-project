<script>
  import { dateStore } from "../routes/store.js";

  export let date;

  // Subscribe to dateStore to get the current selected date
  $: date = $dateStore;
</script>

<div class="p-2 has-background-white">
  <div>
    <div><span>Round:</span> {date}</div>
    <div><span>Zone</span></div>
    <div><span>Seat No.</span></div>
    <div><span>Quantity</span></div>
    <div><span>Unit Price</span></div>
    <div><span>Total Price</span></div>
  </div>
</div>
