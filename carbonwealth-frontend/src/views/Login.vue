<template>
  <div class="page">
    <div class="card">
      <h2>Login</h2>
      <input v-model="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Password" />
      <button @click="login">Login</button>
      <div class="link" @click="$router.push('/register')">
        New user? Register
      </div>
    </div>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  data() {
    return { email: "", password: "" };
  },
  methods: {
    async login() {
      const res = await api.post("/auth/login", {
        email: this.email,
        password: this.password,
      });
      localStorage.setItem("token", res.data.access_token);
      this.$router.push("/dashboard");
    },
  },
};
</script>
