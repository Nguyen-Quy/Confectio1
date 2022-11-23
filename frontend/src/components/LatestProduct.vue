<template>
  <div class="sidebar__item">
    <div class="latest-product__text">
      <h4>Latest Products</h4>

      <div
        class="latest-product__slider owl-carousel"
        v-for="product in latestProducts"
        :key="product.id"
      >
        <div class="latest-prdouct__slider__item">
          <router-link
            :to="`/shop${product.get_absolute_url}`"
            class="latest-product__item"
          >
            <div class="latest-product__item__pic">
              <img :src="product.get_thumbnail" />
            </div>
            <div class="latest-product__item__text">
              <h6>{{ product.name }}</h6>
              <span>{{ product.price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".") }} VNĐ</span>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
  <router-view />
</template>

<script>
import axios from "axios";
export default {
  name: "LatProduct",
  data(){
    return{
      latestProducts: [],
    }
  },
  mounted(){
    this.getLatProducts();
  },
  methods: {
    async getLatProducts() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get(`/api/v1/products/latest/`)
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  }
};
</script>
