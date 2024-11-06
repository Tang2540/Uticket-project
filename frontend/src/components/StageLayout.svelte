<script>
  import { onMount } from "svelte";
  import { goto } from '$app/navigation';
  export let concert;

  let imageRef;
  let originalWidth = 1026; // Set this to your original image width
  let originalHeight = 1081; // Set this to your original image height
  let mapAreas = [];

  function updateCoords() {
    if (!imageRef) return;

    const scale = {
      x: imageRef.width / originalWidth,
      y: imageRef.height / originalHeight,
    };

    mapAreas = concert.pricing.map((zone) => {
      const coords = zone.coor.split(",").map((coord, index) => {
        // Scale even numbers (x coordinates) by x scale
        // Scale odd numbers (y coordinates) by y scale
        return Math.round(coord * (index % 2 === 0 ? scale.x : scale.y));
      });

      return {
        ...zone,
        scaledCoords: coords.join(","),
      };
    });
  }

  onMount(() => {
    // Initial update
    updateCoords();

    // Create ResizeObserver to watch for image size changes
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

  function handleAreaClick(zone, event) {
    event.preventDefault(); // Prevent default anchor behavior
    goto(`/concert/${concert.slug}/${zone.tier}`);
  }
</script>

<div class="stagelayout-container">
  <div class="image-container">
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
          alt={zone.tier}
          title={zone.tier}
          href="#"
          on:click={(e) => handleAreaClick(zone, e)}
          coords={zone.scaledCoords}
          shape={zone.shape}
        />
      {/each}
    </map>
  </div>

  <div class="price-container">
    <div class="price-card">
      <div style="color:black">PRICE</div>
      <div class="price-list">
        {#each concert.pricing as zone}
          <div style="background-color:{zone.color}" class="price-box">{zone.price} BAHT</div>
        {/each}
      </div>
    </div>
  </div>
</div>

<style>
  .image-container {
    width: 65%;
    height: 70%;
  }

  img {
    width: 100%;
    height: 100%;
    display: block;
  }

  .stagelayout-container {
    display: flex;
  }

  .price-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-grow: 1;
  }

  .price-card {
    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 2rem;
    gap: 2rem;
    border-radius: 20px;
  }

  .price-list {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .price-box {
    padding: 1rem 2rem;
    border: 1px solid black;
    border-radius: 20px;
    color: white;
  }
</style>
