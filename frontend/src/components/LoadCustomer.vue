<template>
  <h4 class="text-center">{{ user.username }}</h4>
</template>

<script>
import axios from "axios";

export default {
  name: "LoadCustomer",
  data() {
    return {
      user: [],
    };
  },
  mounted() {
    this.getUserMe();
  },
  methods: {
    async getUserMe() {
      await axios.get(`/api/v1/users/me/`).then((response) => {
        this.user = response.data;
      });
    },
  },
};
</script>
