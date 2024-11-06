<script>
    export let data;
  </script>
  
  <div class="content">
    <h1>concert</h1>
    <ul>
      {#each data.summaries as { slug, title }}
        <li><a href="/concert/{slug}">{title}</a></li>
      {/each}
    </ul>
  </div>
  
