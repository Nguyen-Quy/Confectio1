<template>
  <div class="Home">
    <section class="hero">
      <div class="container">
        <div class="hero__search">
          <div class="hero__search__form">
            <form method="get" action="/search">
              <input type="text" placeholder="What do you need?" name="query" />
              <button type="submit" class="site-btn">SEARCH</button>
            </form>
          </div>
        </div>
      </div>
    </section>
    <!-- <section class="hero">
      <div class="container">
        <div class="row">
          <div class="col-lg-3">
            <div class="hero__categories">
              <div class="hero__categories__all">
                <span>All departments</span>
              </div>
              <ul
                v-for="category in categories"
                :key="category.id"
                :category="category"
              >
                <li>
                  <router-link :to="`/shop${category.get_absolute_url}`">{{
                    category.name
                  }}</router-link>
                </li>
              </ul>
            </div>
          </div>
          <div class="col-lg-9">
            <div class="hero__search">
              <div class="hero__search__form">
                <form action="#">
                  <input type="text" placeholder="What do yo u need?" />
                  <button type="submit" class="site-btn">SEARCH</button>
                </form>
              </div>
            </div>
            <div class="hero__item set-bg" data-setbg="img/hero/banner.jpg"
                  style='background-image: url("img/hero/banner.jpg");'>
              <div class="hero__text">
                <span>FRUIT FRESH</span>
                <h2>Vegetable <br />100% Organic</h2>
                <p>Free Pickup and Delivery Available</p>
                <a href="#" class="primary-btn">SHOP NOW</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section> -->
    <section class="featured spad">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="section-title">
              <h2>Lastest Product</h2>
            </div>
          </div>
        </div>
        <div class="row featured__filter" id="MixItUp556786" style="">
          <FeaturedProduct
            v-for="product in lastestProducts"
            :key="product.id"
            :product="product"
          />
        </div>
      </div>
    </section>
    <section class="section">
      <router-view />
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
      lastestProducts: [],
      categories: [],
    };
  },
  components: {
    FeaturedProduct,
  },
  mounted() {
    this.getLastestProducts();
    this.getloadCategories();

    document.title = "Home";
  },
  methods: {
    async getLastestProducts() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/v1/latest-products/")
        .then((response) => {
          this.lastestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
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
