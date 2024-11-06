<script>
    export let id;
    export let title;
    export let description;
    export let image;
  </script>
  
  <a href={`/item/${id}`} class="card-link">
    <div class="card">
      <img src={image} alt={title} />
      <div class="card-content">
        <div class="card-title">{title}</div>
        <p class="card-description">{description}</p>
      </div>
    </div>
  </a>
  
  <style>
    .card-link {
      display: block;
      text-decoration: none;
      color: inherit;
    }
  
    .card {
      max-width: 384px; /* equivalent to max-w-sm */
      border-radius: 0.25rem;
      overflow: hidden;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: box-shadow 0.3s ease-in-out;
    }
  
    .card:hover {
      box-shadow: 0 10px 15px rgba(0, 0, 0, 0.2);
    }
  
    .card img {
      width: 100%;
      display: block;
    }
  
    .card-content {
      padding: 1.5rem;
    }
  
    .card-title {
      font-weight: bold;
      font-size: 1.25rem;
      margin-bottom: 0.5rem;
    }
  
    .card-description {
      color: #4a5568; /* equivalent to text-gray-700 */
      font-size: 1rem;
    }
  </style>