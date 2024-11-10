<script>
  const concerts = [
    {
      id: 1,
      slug: "yoona_fan_meeting_tour",
      title: "YOONA FAN MEETING TOUR 'YOONITE' in Bangkok",
      location: "BITEC Event Hall 98",
      image: "yoona1.png",
      date: "24 February 2024",
      status: "BUY NOW",
      statusClass: "has-background-danger has-text-white"
    },
    {
      id: 2,
      slug: "ten_first_fan_con_bangkok",
      title: "2024 TEN FIRST FAN-CON [1001] IN BANGKOK",
      location: "Impact Arena, Muang Thong Thani",
      image: "ten.jpg",
      date: "2-3 March 2024",
      status: "Sold Out",
      statusClass: "has-background-grey-dark has-text-white"
    },
    {
      id: 3,
      slug: "park_shin_hye_asia_tour_bangkok",
      title: "2024 PARK SHIN HYE ASIA TOUR in BANGKOK",
      location: "Impact Arena, Muang Thong Thani",
      image: "parksinhye.jpg",
      date: "3 March 2024",
      status: "Coming Soon",
      statusClass: "has-background-transparent has-text-white has-border-white"
    },
    {
      id: 4,
      slug: "cha_eunwoo_2024_mystery",
      title: "CHA EUN-WOO 2024 Just One 10 Minute Mystery",
      location: "Impact Hall 5-6, IMPACT",
      image: "chaeunwoo.jpg",
      date: "9 March 2024",
      status: "BUY NOW",
      statusClass: "has-background-danger has-text-white"
    },
    {
      id: 5,
      slug: "super_junior_lss_the_show",
      title: "SUPER JUNIOR-L.S.S. THE SHOW: Three Guys in",
      location: "Impact Hall 5, Union Mall",
      image: "superjunior.jpg",
      date: "6 April 2024",
      status: "Coming Soon",
      statusClass: "has-background-transparent has-text-white has-border-white"
    }
  ];
</script>

<style>
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
      {#each concerts as concert}
        <div class="column is-3">
          <div class="card">
            <div class="card-image">
              <figure class="image is-4by3">
                <img src={concert.image} alt={concert.title} />
              </figure>
            </div>
            <div class="card-content has-text-centered">
              <p class="title is-6 has-text-white">{concert.title}</p>
              <p class="subtitle is-7 has-text-grey-light">{concert.location}</p>
              <p class="is-size-7 has-text-grey-light">{concert.date}</p>
              <!-- Update: Button with dynamic link to concert page -->
              <a href={`/concert/${concert.slug}`} class="button is-fullwidth is-small mt-3 {concert.statusClass}">{concert.status}</a>
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>
