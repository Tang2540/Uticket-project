<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    // Props
    export let selectedZone: string | null;
    export let selectedSeat: string | null;
    // Types
    type SeatStatus = 'available' | 'selected' | 'taken';
    
    interface Seat {
    id: string;
    row: string;
    number: number;
    status: SeatStatus;
    }
    // Event dispatcher
    const dispatch = createEventDispatcher<{
    seatSelect: { seatId: string; row: string; number: number };
    }>();
    // Constants
    const ROWS = ['A', 'B', 'C', 'D', 'E', 'F'];
    const SEATS_PER_ROW = 12;
    // Generate seats with random availability
    const generateSeats = (zone: string): Seat[][] => {
    return ROWS.map(row => 
    Array.from({ length: SEATS_PER_ROW }, (_, i) => {
    const seatNumber = i + 1;
    const seatId = `${row}${seatNumber}`;
    return {
    id: seatId,
    row,
    number: seatNumber,
    status: Math.random() > 0.3 ? 'available' : 'taken'
    };
    })
    );
    };
    // Reactive statements
    $: seats = selectedZone ? generateSeats(selectedZone) : [];
    $: seatMap = new Map(
    seats.flat().map(seat => [seat.id, seat])
    );
    // Update seat status when selection changes
    $: if (selectedSeat && seatMap.has(selectedSeat)) {
    seatMap.get(selectedSeat)!.status = 'selected';
    }
    // Handle seat click
    function handleSeatClick(seat: Seat) {
    if (seat.status === 'taken') return;
    
    // Deselect previous seat if exists
    if (selectedSeat && seatMap.has(selectedSeat)) {
    seatMap.get(selectedSeat)!.status = 'available';
    }
    // Select new seat
    seat.status = 'selected';
    dispatch('seatSelect', {
    seatId: seat.id,
    row: seat.row,
    number: seat.number
    });
    }
    // Get CSS classes for seat
    function getSeatClasses(seat: Seat): string {
    const classes = ['is-small'];
    
    switch (seat.status) {
    case 'selected':
    classes.push('is-primary','has-background-primary');
    break;
    case 'taken':
    classes.push('is-light', 'is-disabled');
    break;
    case 'available':
    classes.push('is-outlined','has-background-danger');
    break;
    }
    
    return classes.join(' ');
    }
   </script>
   <div class="box">
    <div class="seat-selection">
    <!-- Stage indicator -->
    <div class="stage-indicator mb-6">
    <div class="has-text-centered p-4 has-background-light">
    <h3 class="title is-5 mb-0">STAGE</h3>
    </div>
    </div>
    {#if selectedZone}
    <!-- Seat legend -->
    <div class="seat-legend mb-4">
    <div class="columns is-mobile is-centered">
    <div class="column is-narrow">
    <button class="button is-small is-outlined" disabled>Available</button>
    </div>
    <div class="column is-narrow">
    <button class="button is-small is-primary" disabled>Selected</button>
    </div>
    <div class="column is-narrow">
    <button class="button is-small is-light" disabled>Taken</button>
    </div>
    </div>
    </div>
    <!-- Seat grid -->
    <div class="seat-grid">
    {#each seats as rowSeats, rowIndex}
    <div class="seat-row columns is-mobile is-centered mb-1">
    <!-- Row label left -->
    <div class="column is-narrow row-label">
    <span class="tag is-medium">{ROWS[rowIndex]}</span>
    </div>
    <!-- Seats -->
    <div class="column">
    <div class="columns is-mobile is-centered">
    {#each rowSeats as seat}
    <div class="column is-narrow px-1 is-rounded">
    <button
    class={getSeatClasses(seat)}
    disabled={seat.status === 'taken'}
    on:click={() => handleSeatClick(seat)}
    aria-label="Seat {seat.id}"
    >
    {seat.number}
    </button>
    </div>
    {/each}
    </div>
    </div>
    <!-- Row label right -->
    <div class="column is-narrow row-label">
    <span class="tag is-medium">{ROWS[rowIndex]}</span>
    </div>
    </div>
    {/each}
    </div>
    <!-- Selected seat info -->
    {#if selectedSeat}
    <div class="selected-seat-info has-text-centered mt-4">
    <p class="has-text-weight-bold">
    Selected Seat: {selectedSeat}
    </p>
    </div>
    {/if}
    {:else}
    <div class="has-text-centered">
    <p>Please select a zone first</p>
    </div>
    {/if}
    </div>
   </div>
   
   <style>
    .seat-selection {
    max-width: 900px;
    margin: 0 auto;
    }
    .stage-indicator {
    width: 60%;
    margin: 0 auto;
    }
    .seat-grid {
    max-width: 100%;
    overflow-x: auto;
    }
    .seat-row {
    align-items: center;
    }
    .row-label {
    width: 50px;
    text-align: center;
    }
    button.button.is-small {
    width: 2rem;
    height: 2rem;
    padding: 0;
    margin: 0.1rem;
    font-size: 0.75rem;
    }
    .seat-legend button {
    cursor: default;
    }
    /* Make the grid scrollable on mobile */
    @media screen and (max-width: 768px) {
    .seat-grid {
    overflow-x: scroll;
    padding: 1rem;
    }
    
    .seat-row {
    min-width: 600px;
    }
    }
   </style>