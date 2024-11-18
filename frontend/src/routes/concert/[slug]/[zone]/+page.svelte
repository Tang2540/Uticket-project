<script>
  import { dateStore, seatStore } from "../../../store";
  import Seat from "../../../../components/Seat.svelte";
  import TicketForm from "../../../../components/TicketForm.svelte";
  export let data;
  const { concert, pricing, zoneTier } = data;
  $: date = $dateStore;
  $: seats = $seatStore;
</script>

<h1>{pricing.tier}</h1>
<div class="container p-4">
  <Seat selectedZone={pricing.zone} {concert} />
  <TicketForm {pricing} {zoneTier} {date} {seats}/>
</div>
