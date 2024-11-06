<script>
    import { onMount } from 'svelte';
	import { dateStore } from '../../../store.js';
    import Seat from "../../../../components/Seat.svelte";
    import TicketForm from "../../../../components/TicketForm.svelte";
    onMount(console.log(dateStore))
    export let data;
    const {concert,pricing} = data;
</script>
<h1>{pricing.tier}</h1>
<div class="container p-4">
<Seat selectedZone={pricing.tier} {concert}/>
<TicketForm/>
<h1>{$dateStore}</h1>
</div>