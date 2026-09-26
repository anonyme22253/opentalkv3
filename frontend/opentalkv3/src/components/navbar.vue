<template>
  <nav class="navbar">

    <div class="logo">
      OpenTalk
    </div>

    <div class="search-container">
      <input
        type="text"
        placeholder="@username"
        id="usernameField"
      />

      <button class="search-button">
        Search

        <div class="star-1">
          <svg viewBox="0 0 784.11 815.53">
            <path
              class="fil0"
              d="M392.05 0c-20.9 210.08-184.06 378.41-392.05 407.78 207.96 29.37 371.12 197.68 392.05 407.74 20.93-210.06 184.09-378.37 392.05-407.74-207.98-29.38-371.16-197.69-392.06-407.78z"
            />
          </svg>
        </div>

        <div class="star-2">
          <svg viewBox="0 0 784.11 815.53">
            <path
              class="fil0"
              d="M392.05 0c-20.9 210.08-184.06 378.41-392.05 407.78 207.96 29.37 371.12 197.68 392.05 407.74 20.93-210.06 184.09-378.37 392.05-407.74-207.98-29.38-371.16-197.69-392.06-407.78z"
            />
          </svg>
        </div>

        <div class="star-3">
          <svg viewBox="0 0 784.11 815.53">
            <path
              class="fil0"
              d="M392.05 0c-20.9 210.08-184.06 378.41-392.05 407.78 207.96 29.37 371.12 197.68 392.05 407.74 20.93-210.06 184.09-378.37 392.05-407.74-207.98-29.38-371.16-197.69-392.06-407.78z"
            />
          </svg>
        </div>

        <div class="star-4">
          <svg viewBox="0 0 784.11 815.53">
            <path
              class="fil0"
              d="M392.05 0c-20.9 210.08-184.06 378.41-392.05 407.78 207.96 29.37 371.12 197.68 392.05 407.74 20.93-210.06 184.09-378.37 392.05-407.74-207.98-29.38-371.16-197.69-392.06-407.78z"
            />
          </svg>
        </div>

        <div class="star-5">
          <svg viewBox="0 0 784.11 815.53">
            <path
              class="fil0"
              d="M392.05 0c-20.9 210.08-184.06 378.41-392.05 407.78 207.96 29.37 371.12 197.68 392.05 407.74 20.93-210.06 184.09-378.37 392.05-407.74-207.98-29.38-371.16-197.69-392.06-407.78z"
            />
          </svg>
        </div>

        <div class="star-6">
          <svg viewBox="0 0 784.11 815.53">
            <path
              class="fil0"
              d="M392.05 0c-20.9 210.08-184.06 378.41-392.05 407.78 207.96 29.37 371.12 197.68 392.05 407.74 20.93-210.06 184.09-378.37 392.05-407.74-207.98-29.38-371.16-197.69-392.06-407.78z"
            />
          </svg>
        </div>

      </button>
    </div>

  </nav>
</template>

<style scoped>
.navbar {
  width: 100%;
  height: 70px;
  background: #0b0f14;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 30px;
  box-sizing: border-box;
  border-bottom: 1px solid #1d2630;
}

.logo {
  color: #2196f3;
  font-size: 28px;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.search-container {
  display: flex;
  align-items: center;
  gap: 12px;
}

#usernameField {
  width: 220px;
  height: 40px;
  background: #151b22;
  border-radius: 25px;
  border: 2px solid #26313d;
  padding: 0 15px;
  outline: none;
  color: #e5e7eb;
  font-size: 13px;
  transition: 0.2s;
}

#usernameField::placeholder {
  color: #687585;
}

#usernameField:focus {
  border-color: #2196f3;
  box-shadow: 0 0 8px rgba(33, 150, 243, 0.2);
}

.search-button {
  position: relative;
  padding: 10px 28px;
  background: #2196f3;
  font-size: 15px;
  font-weight: 600;
  color: white;
  border: 2px solid #2196f3;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.search-button:hover {
  background: transparent;
  color: #2196f3;
  box-shadow: 0 0 20px rgba(33, 150, 243, 0.4);
}

.star-1,
.star-2,
.star-3,
.star-4,
.star-5,
.star-6 {
  position: absolute;
  height: auto;
  z-index: -1;
  transition: all 0.8s ease;
}

.star-1 {
  top: 20%;
  left: 20%;
  width: 25px;
}

.star-2 {
  top: 45%;
  left: 45%;
  width: 15px;
}

.star-3 {
  top: 40%;
  left: 40%;
  width: 5px;
}

.star-4 {
  top: 20%;
  left: 40%;
  width: 8px;
}

.star-5 {
  top: 25%;
  left: 45%;
  width: 15px;
}

.star-6 {
  top: 5%;
  left: 50%;
  width: 5px;
}

.search-button:hover .star-1 {
  top: -80%;
  left: -30%;
  z-index: 2;
}

.search-button:hover .star-2 {
  top: -25%;
  left: 10%;
  z-index: 2;
}

.search-button:hover .star-3 {
  top: 55%;
  left: 25%;
  z-index: 2;
}

.search-button:hover .star-4 {
  top: 30%;
  left: 80%;
  z-index: 2;
}

.search-button:hover .star-5 {
  top: 25%;
  left: 115%;
  z-index: 2;
}

.search-button:hover .star-6 {
  top: 5%;
  left: 60%;
  z-index: 2;
}

.fil0 {
  fill: #2196f3;
}
</style>