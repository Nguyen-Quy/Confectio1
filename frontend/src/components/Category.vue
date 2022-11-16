<template>
  <div class="sidebar__item">
    <h4>Categories</h4>
    <ul>
      <li><router-link :to="`/shop`">All</router-link></li>
    </ul>
    <ul v-for="category in categories" :key="category.id" :category="category">
      <li>
        <router-link :to="`/shop${category.get_absolute_url}`">{{
          category.name
        }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Category",
  data() {
    return {
      categories: [],
    };
  },
  mounted() {
    this.getloadCategories();
  },
  methods: {
    async getloadCategories() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get(`/api/v1/categories/`)
        .then((response) => {
          this.categories = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
