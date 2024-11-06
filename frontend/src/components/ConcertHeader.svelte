<script>
    export let title;
    export let venue;
    export let dates;
    export let img;
  </script>

  <div class="header-bckimg p-6" style:background-image="url('/{img}')">
    <div class="header-card">
      <div class="img-box">
          <img src="/{img}" alt={title} style="height:100%;width:100%"/>
      </div>
      <div class="has-background-black detail-card">
        <h1 class="title">{title}</h1>
        <div class="is-flex">
            <p class="subtitle">
                <span class="icon"><i class="fas fa-calendar"></i></span>
                {dates[0].date} - {dates[dates.length - 1].date}
              </p>
              <p class="subtitle ml-6">
                <span class="icon"><i class="fas fa-clock"></i></span>
                {dates[0].time}
              </p>
        </div>
        <p class="subtitle">
          <span class="icon"><i class="fas fa-map-marker-alt"></i></span>
          {venue}
        </p>
      </div>
    </div>
  </div>
  
  <style>

    .header-bckimg {
      position: relative;
      background-repeat: no-repeat;
      background-size: cover;
      height: 400px;
    }
  
    .header-bckimg::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: rgba(0, 0, 0, 0.8); /* Black overlay with 50% opacity */
      /* You can change the color and opacity by adjusting the rgba values */
    }
  
    .header-bckimg > * {
      position: relative;
      z-index: 1;
    }

    .header-card {
        display: flex;
        justify-content: center;
        height: 100%;
        width: 100%;
    }

    .img-box {
      height: 100%;
      width: 30%;
    }

    .detail-card {
        height: 100%;
        width: 70%;
        padding: 1rem;
    }
  </style>