<template>
  <nav class="navbar">
    <div class="logo">🌱 CarbonWealth</div>

    <div class="nav-links">
      <router-link v-if="!isLoggedIn" to="/login">Login</router-link>
      <router-link v-if="!isLoggedIn" to="/register">Register</router-link>

      <router-link v-if="isLoggedIn" to="/dashboard">Dashboard</router-link>

      <button v-if="isLoggedIn" @click="logout">Logout</button>
    </div>
  </nav>
</template>

<script>
export default {
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem("token");
    },
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/login");
    },
  },
};
</script>

<style scoped>
.navbar {
  height: 60px;
  background: #2f80ed;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 24px;
}

.logo {
  font-size: 20px;
  font-weight: bold;
}

.nav-links {
  display: flex;
  gap: 16px;
  align-items: center;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-weight: 500;
}

.nav-links a.router-link-active {
  text-decoration: underline;
}

button {
  background: transparent;
  border: 1px solid white;
  color: white;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background: white;
  color: #2f80ed;
}
</style>
