<script>
	import { dateStore } from "../../../store";
    import Seat from "../../../../components/Seat.svelte";
    import TicketForm from "../../../../components/TicketForm.svelte";

    export let data;
    const {pricing} = data;
</script>
<h1>{pricing.tier}</h1>
<div class="container p-4">
<Seat selectedZone={pricing.tier}/>
<TicketForm/>
<h1>{$dateStore}</h1>
</div>