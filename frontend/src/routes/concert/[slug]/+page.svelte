<script lang="ts">
  import { onMount } from 'svelte';
  import ConcertHeader from '../../../components/ConcertHeader.svelte';
  import DateSelector from '../../../components/DateSelector.svelte';
  import StageLayout from '../../../components/StageLayout.svelte';
  import { dateStore } from '../../store';
  
  
  export let data;
  const { concert } = data;
  $: date = $dateStore;
  
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
  {#if date}
  <StageLayout
  {concert}
  />
  {:else}
  <div></div>
  {/if}
 </div>