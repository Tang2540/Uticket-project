<script>
  import Seat from "../../../../components/Seat.svelte";
  import TicketForm from "../../../../components/TicketForm.svelte";
  export let data;
  const { concert, pricing, zoneTier } = data;
</script>

<h1>{pricing.tier}</h1>
<div class="container p-4">
  <Seat selectedZone={pricing.zone} {concert} />
  <TicketForm {pricing} {zoneTier}/>
</div>
