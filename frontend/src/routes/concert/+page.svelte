<script>
  export let data;
  const {summaries} = data
</script>

<style>
  /* Updated class for fixed concert image size */
  .fixed-image {
    width: 600px;
    height: 500px;
    object-fit: cover; /* Keeps aspect ratio without distortion */
  }
  
  .dot-container {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
  }
  .dot {
    width: 10px;
    height: 10px;
    background-color: white;
    border-radius: 50%;
    opacity: 0.5;
    cursor: pointer;
  }
  .dot.active {
    background-color: pink;
    opacity: 1;
  }
  .writing-vertical-rl { 
    writing-mode: vertical-rl; 
    text-orientation: mixed; 
  }
  
  .body {
    background-color: black;
    color: white;
  }

  .arrow-button {
    position: absolute;
    top: 50%; 
    transform: translateY(-50%); 
    color: rgba(237,16,103,255);
    cursor: pointer;
    border: none;
    font-size: 1.5rem;
    padding: 0.5rem;
    z-index: 10;
  }

  .arrow-left {
    left: 1rem; 
  }

  .arrow-right {
    right: 1rem; 
  }

  button {
    border-radius: 20px;
  }
</style>

<!-- Popular Concerts Section -->
<section class="section">
  <div class="container">
    <h2 class="title is-4 has-text-white mb-4">Popular Concerts</h2>
    <div class="columns is-multiline">
      {#each summaries as {cardImg,title,venue,date,slug,status}}
        <div class="column is-3">
          <div class="card">
            <div class="card-image">
              <figure class="image">
                <img src={cardImg} alt={title} class="fixed-image" />
              </figure>
            </div>
            <div class="card-content has-text-centered">
              <p class="title is-6 has-text-white">{title}</p>
              <p class="subtitle is-7 has-text-grey-light">{venue}</p>
              <p class="is-size-7 has-text-grey-light">{date}</p>
              <a href={`/concert/${slug}`} class={`button is-fullwidth is-small mt-3 ${status==="BUY NOW"?"has-background-danger has-text-white":status==="Sold Out"?"has-background-grey-dark has-text-white":"has-background-transparent has-text-white has-border-white"}`}>{status}</a>
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>
