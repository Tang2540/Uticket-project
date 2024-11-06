<script lang="ts">
  import { onMount } from 'svelte';
  import ConcertHeader from '../../../components/ConcertHeader.svelte';
  import DateSelector from '../../../components/DateSelector.svelte';
  import StageLayout from '../../../components/StageLayout.svelte';
  import SeatSelection from '../../../components/SeatSelection.svelte';
  
  export let data;
  const { concert } = data;
  let quantity = 1;

  let selectedZone = null;
    let selectedSeat = null;
    function handleSeatSelection(event: CustomEvent<{ seatId: string }>) {
    selectedSeat = event.detail.seatId;
    }
  // Reactive statement for total price calculation
  $: totalPrice = selectedSeat ? selectedSeat.price * quantity : 0;
  async function handleDateChange(event) {
  const newDate = event.detail;
  // Reset seat selection when date changes
  selectedSeat = null;
  // Could trigger API call to fetch available seats for new date
  }
  async function handleSeatSelect(event) {
  const seat = event.detail;
  selectedSeat = seat;
  }
  async function handleBooking() {
  if (!selectedSeat) {
  alert('Please select a seat first');
  return;
  }
  try {
  // Simulate API call
  await new Promise(resolve => setTimeout(resolve, 1000));
  alert('Booking successful!');
  } catch (error) {
  alert('Booking failed. Please try again.');
  }
  }
 </script>
 
 <ConcertHeader 
  title={concert.title}
  venue={concert.venue}
  dates={concert.dates}
  img={concert.img}
  />
 <div class="container p-4">
  <DateSelector
  dates={concert.dates}
  />
  <StageLayout
  {concert}
  on:seatSelect={handleSeatSelect}
  />
 </div>