<script>
  
    let lang = 'eng';
    let isModalOpen = false;
  
    const openModal = () => {
      isModalOpen = true;
    };
  
    const closeModal = () => {
      isModalOpen = false;
    };
  </script>
  
  <nav>
    <div class="container">
      <div class="nav-content">
        <a href="/">
          <img class="logo" src="/uticketlogo.png" alt="uticket-logo" />
        </a>
  
        <div class="nav-actions">
          <div class="search-icon" on:click={openModal}>
            <img src="/search.svg" alt="search-logo"/>
          </div>
          <div class="language-switch">
            <div
              class:active={lang === 'eng'}
              class="language-btn"
              on:click={() => {
                lang = 'eng';
              }}
            >
              EN
            </div>
            <div class="divider"></div>
            <div
              class:active={lang === 'th'}
              class="language-btn"
              on:click={() => {
                lang = 'th';
              }}
            >
              TH
            </div>
          </div>
          <div class="signin-btn">Sign in / Log in</div>
        </div>
      </div>
    </div>
  
    <div class="modal" class:is-active={isModalOpen}>
      <div class="modal-background"></div>
      <div class="modal-content">
        <!-- Any other Bulma elements you want -->
      </div>
      <button class="modal-close is-large" aria-label="close" on:click={closeModal}></button>
    </div>
  </nav>
  
  <style>
    nav {
      background-color: black;
      color: #fff;
      padding: 0.5rem 0;
    }
  
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 1rem;
    }
  
    .nav-content {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
  
    .logo {
      height: 80px;
      width: auto;
    }
  
    .nav-actions {
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }
  
    .search-icon {
      cursor: pointer;
      height: 32px;
      width: 32px;
    }
  
    .search-icon img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }
  
    .language-switch {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
  
    .language-btn {
      cursor: pointer;
    }
  
    .language-btn.active {
      font-weight: bold;
    }
  
    .divider {
      height: 23px;
      width: 2px;
      background-color: #fff;
    }
  
    .signin-btn {
      background-color: #ff69b4;
      color: #fff;
      padding: 0.5rem 1rem;
      border-radius: 4px;
      text-decoration: none;
    }
  </style>