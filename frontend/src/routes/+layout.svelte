<!-- src/routes/+layout.svelte -->
<script>
    import 'bulma/css/bulma.min.css';
    import Navbar from '../components/Navbar.svelte';
   </script>
   <svelte:head>
    <link 
    rel="stylesheet" 
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    >
   </svelte:head>
   <Navbar/>
   <slot />
   <style>
    :global(html) {
    overflow-y: auto;
    }
   </style>