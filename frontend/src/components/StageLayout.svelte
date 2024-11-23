<script>
  import { onMount, onDestroy } from "svelte";
  import { goto } from '$app/navigation';
 
  export let concert;
 
  let imageRef;
  let originalWidth = 1026;
  let originalHeight = 1081;
  let mapAreas = [];
  let zoneAvailability = [];
  let loading = true;
  let error = null;
  let websocket;
  const MAX_RETRIES = 3;
  const RETRY_DELAY = 2000;
 
  async function fetchZoneAvailability(retry = 0) {
    try {
      loading = true;
      error = null;
 
      const response = await fetch(`/api/concerts/${concert.id}/availability`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      zoneAvailability = data;
      updateCoords();
    } catch (err) {
      console.error('Error fetching zone availability:', err);
      error = {
        message: 'Failed to load seat availability',
        details: err.message,
        type: response?.status === 404 ? 'not-found' : 'fetch-error'
      };
 
      if (retry < MAX_RETRIES) {
        setTimeout(() => {
          fetchZoneAvailability(retry + 1);
        }, RETRY_DELAY * (retry + 1));
      }
    } finally {
      loading = false;
    }
  }
 
  function setupWebSocket() {
    try {
      websocket = new WebSocket(`ws://your-api/concerts/${concert.id}/availability`);
     
      websocket.onmessage = (event) => {
        const newData = JSON.parse(event.data);
        zoneAvailability = newData;
        updateCoords();
      };
 
      websocket.onerror = () => {
        retryWebSocket();
      };
 
      websocket.onclose = () => {
        retryWebSocket();
      };
    } catch (err) {
      console.error('WebSocket setup error:', err);
      retryWebSocket();
    }
  }
 
  function retryWebSocket() {
    setTimeout(() => {
      setupWebSocket();
    }, RETRY_DELAY);
  }
 
  function updateCoords() {
    if (!imageRef) return;
 
    const scale = {
      x: imageRef.width / originalWidth,
      y: imageRef.height / originalHeight,
    };
 
    mapAreas = concert.pricing.map((zone) => {
      const coords = zone.coor.split(",").map((coord, index) => {
        return Math.round(coord * (index % 2 === 0 ? scale.x : scale.y));
      });
 
      const availability = zoneAvailability.find(z => z.zone === zone.zone)?.available || 0;
 
      return {
        ...zone,
        scaledCoords: coords.join(","),
        available: availability
      };
    });
  }
 
  onMount(async () => {
    await fetchZoneAvailability();
    setupWebSocket();
 
    const resizeObserver = new ResizeObserver(() => {
      updateCoords();
    });
 
    if (imageRef) {
      resizeObserver.observe(imageRef);
    }
 
    return () => {
      resizeObserver.disconnect();
    };
  });
 
  onDestroy(() => {
    if (websocket) {
      websocket.close();
    }
  });
 
  function handleClick(zone, e) {
    e.preventDefault();
    goto(`/concert/${concert.slug}/${zone.zone}`);
  }
 
  function handleRetry() {
    fetchZoneAvailability();
  }
 
  $: sortedZones = mapAreas.sort((a, b) => a.zone.localeCompare(b.zone));
</script>
 
<div class="stagelayout-container">
  <div class="stage-section">
    <img
      bind:this={imageRef}
      src={concert.seatMap}
      usemap="#image-map"
      alt="image_map"
      on:load={updateCoords}
    />
 
    <map name="image-map">
      {#each mapAreas as zone}
        <area
          target=""
          alt={zone.zone}
          title={zone.zone}
          href="#"
          on:click={(e) => handleClick(zone, e)}
          coords={zone.scaledCoords}
          shape={zone.shape}
        />
      {/each}
    </map>
  </div>
 
  <div class="availability-section">
    <div class="availability-header">SEAT AVAILABLE</div>
   
    {#if loading && !error}
      <div class="status-message">
        <div class="loading-spinner"></div>
        <p>Loading seat availability...</p>
      </div>
    {:else if error}
      <div class="status-message error">
        <div class="error-icon">⚠️</div>
        <div class="error-content">
          <div class="error-title">
            {error.type === 'not-found' ? 'Concert not found' : error.message}
          </div>
          <div class="error-details">{error.details}</div>
          <button class="retry-button" on:click={handleRetry}>
            Try Again
          </button>
        </div>
      </div>
    {:else}
      <div class="availability-list">
        {#each sortedZones as zone (zone.zone)}
          <div class="zone-item">
            <div class="zone-name">{zone.zone}</div>
            <div class="zone-count {zone.available > 0 ? 'available' : 'unavailable'}">
              {zone.available}
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>
</div>
 
<style>
  .stagelayout-container {
    display: flex;
    gap: 2rem;
    height: 100%;
    padding: 1rem;
  }
 
  .stage-section {
    flex: 1;
    max-width: 65%;
  }
 
  .stage-section img {
    width: 100%;
    height: auto;
    display: block;
  }
 
  .availability-section {
    flex: 1;
    max-width: 35%;
    background: #1a2942;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    max-height: 500px;
  }
 
  .availability-header {
    padding: 1rem;
    background: #1a2942;
    color: white;
    font-weight: bold;
    border-bottom: 1px solid #2a3952;
    border-radius: 8px 8px 0 0;
  }
 
  .availability-list {
    padding: 0.5rem;
    overflow-y: auto;
  }
 
  .zone-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem;
    border-bottom: 1px solid #2a3952;
  }
 
  .zone-name {
    background: white;
    color: black;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    min-width: 60px;
    text-align: center;
  }
 
  .zone-count {
    padding: 0.5rem 1rem;
    border-radius: 4px;
    min-width: 60px;
    text-align: center;
    color: white;
    font-weight: bold;
  }
 
  .available {
    background-color: #4CAF50;
  }
 
  .unavailable {
    background-color: #f44336;
  }
 
  .status-message {
    padding: 2rem;
    color: white;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }
 
  .loading-spinner {
    width: 30px;
    height: 30px;
    border: 3px solid #f3f3f3;
    border-top: 3px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }
 
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
 
  .error-icon {
    font-size: 1.5rem;
  }
 
  .error-content {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
 
  .error-title {
    font-size: 1rem;
    font-weight: bold;
  }
 
  .error-details {
    font-size: 0.875rem;
    color: #888;
  }
 
  .retry-button {
    margin-top: 0.5rem;
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.2s;
  }
 
  .retry-button:hover {
    background-color: #2980b9;
  }
 
  /* Scrollbar styling */
  .availability-list::-webkit-scrollbar {
    width: 8px;
  }
 
  .availability-list::-webkit-scrollbar-track {
    background: #1a2942;
    border-radius: 4px;
  }
 
  .availability-list::-webkit-scrollbar-thumb {
    background: #2a3952;
    border-radius: 4px;
  }
 
  .availability-list::-webkit-scrollbar-thumb:hover {
    background: #34445e;
  }
 
  /* Animation for updates */
  .zone-item {
    transition: background-color 0.3s ease;
  }
 
  .zone-item:hover {
    background-color: #2a3952;
  }
 
  @keyframes highlight {
    0% { transform: scale(1); }
    50% { transform: scale(1.02); }
    100% { transform: scale(1); }
  }
 
  .zone-count {
    transition: all 0.3s ease;
  }
 
  .zone-count.updated {
    animation: highlight 0.3s ease;
  }
</style>