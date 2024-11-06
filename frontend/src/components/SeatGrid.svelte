<script lang="ts">
  import SeatSelection from "./SeatSelection.svelte";

    let selectedZone: string | null = null;
    let selectedSeat: string | null = null;
    function handleSeatSelection(event: CustomEvent<{ seatId: string }>) {
    selectedSeat = event.detail.seatId;
    }
   </script>
   <SeatSelection
    {selectedZone}
    {selectedSeat}
    on:seatSelect={handleSeatSelection}
   />