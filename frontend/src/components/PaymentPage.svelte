<script>
    import { page } from '$app/stores';
  
    let pricing, zoneTier, date, seats;
  
    $: {
      const state = $page?.data?.state || {};
      pricing = state.pricing;
      zoneTier = state.zoneTier;
      date = state.date;
      seats = state.seats;
    }
  
    let timeLeft = 30 * 60; // 30 minutes in seconds
    let timer;
  
    function formatTime(seconds) {
      const minutes = Math.floor(seconds / 60);
      const remainingSeconds = seconds % 60;
      return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
    }
  
    onMount(() => {
      timer = setInterval(() => {
        if (timeLeft > 0) {
          timeLeft--;
        } else {
          clearInterval(timer);
          // Handle timeout logic
        }
      }, 1000);
    });
  
    onDestroy(() => {
      if (timer) clearInterval(timer);
    });
  
    $: formattedTime = formatTime(timeLeft);
    $: totalPrice = zoneTier.price * seats.length;
  </script>
  
  <div class="payment-container">
    <!-- Your PaymentPage content here -->
  </div>
  
  <style>
    /* Your existing styles */
  </style>
  