<template>
  <div class="column is-12">
    <button @click="logout()" class="btn-logout btn btn-primary">Log out</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LogOut",
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("uid");

      axios.post("/api/v1/token/logout/");

      this.$store.commit("removeToken");
      this.$router.push("/");
    },
  },
};
</script>
