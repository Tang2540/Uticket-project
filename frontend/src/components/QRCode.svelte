<script>
    import QRCode from 'qrcode';
    import { onMount } from 'svelte';
   
    export let accountNumber;
    export let amount;
    let qrCanvas;
   
    onMount(async () => {
      try {
        
        const promptPayData = `promptpay://${accountNumber}/${amount}`;
        await QRCode.toCanvas(qrCanvas, promptPayData, {
          width: 300,
          margin: 2,
          color: {
            dark: '#000000',
            light: '#ffffff'
          }
        });
      } catch (err) {
        console.error('Error generating QR code:', err);
      }
    });
  </script>
   
  <canvas bind:this={qrCanvas}></canvas>