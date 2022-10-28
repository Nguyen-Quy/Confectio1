<template>
  <div class="Home">
    <section class="hero">
      <div class="container">
        <div class="hero__search">
          <div class="hero__search__form">
            <form method="get" action="/search">
              <input type="text" placeholder="What do yo u need?" />
              <button type="submit" class="site-btn">SEARCH</button>
            </form>
          </div>
        </div>
      </div>
    </section>
    <section class="featured spad">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="section-title">
              <h2>Featured Product</h2>
            </div>
            <div class="featured__controls">
              <ul>
                <li class="active mixitup-control-active">
                  <a href="/">All</a>
                </li>
                <li data-filter=".banh" class="">Bánh</li>
                <li data-filter=".keo" class="">Kẹo</li>
                <li data-filter=".nuoc" class="">Đồ uống</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="row featured__filter" id="MixItUp556786" style="">
          <FeaturedProduct
            v-for="product in allProducts"
            :key="product.id"
            :product="product"
          />
        </div>
      </div>
    </section>
    <section class="section">
      <router-view/>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import FeaturedProduct from "@/components/FeaturedProduct";

export default {
  name: "Home",
  data() {
    return {
      allProducts: [],
    };
  },
  components: {
    FeaturedProduct,
  },
  mounted() {
    this.getAllProducts();

    document.title = "Home";
  },
  methods: {
    async getAllProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/shop/')
        .then(response => {
          this.allProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    },
  },

};
</script>
