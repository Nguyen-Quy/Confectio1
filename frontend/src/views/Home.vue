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

    <vueper-slides
      autoplay
      fixed-height="300px"
      :slide-content-outside="bottom"
      :pause-on-hover="pauseOnHover"
      @autoplay-pause="internalAutoPlaying = false"
      @autoplay-resume="internalAutoPlaying = true"
    >
      <vueper-slide
        class="slider"
        v-for="product in lastestProducts"
        :key="product.id"
        :image="product.get_image"
        :content="product.name"
      />
    </vueper-slides>

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
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";

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
    VueperSlides,
    VueperSlide,
  },
  mounted() {
    this.getLastestProducts();
    this.getloadCategories();

    document.title = "Home | BK";
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
<style>
.image-height {
  max-height: 300px;
  width: 100%;
}
.vueperslide__content {
  position: absolute;
  top: 10px;
  left: 50%;
  -webkit-transform: translateX(-50%);
  transform: translateX(-50%);
  padding: 4px 25px;
  background: orange;
  color: #fff;
  font-size: 18px;
  box-shadow: 0 0 9px rgba(0, 0, 0, 0.2);
}

.vueperslide,
.vueperslide__image {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 100% 200%;
}
</style>
