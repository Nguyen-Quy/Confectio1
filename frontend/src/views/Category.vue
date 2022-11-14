<template>
  <div class="Shop" :class="{ loading: loading }">
    <!-- Hero Section Begin -->
    <section class="hero hero-normal">
      <div class="container">
        <div class="hero__search">
          <div class="hero__search__form">
            <form method="get" action="/search">
              <input
                type="text"
                placeholder="What do yo u need?"
                name="query"
              />
              <button type="submit" class="site-btn">SEARCH</button>
            </form>
          </div>
        </div>
      </div>
    </section>
    <!-- Hero Section End -->
    <!-- Breadcrumb Section Begin -->
    <section class="breadcrumb-section set-bg" data-setbg="img/breadcrumb.jpg">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <div class="breadcrumb__text">
              <h2>Cửa hàng</h2>
              <div class="breadcrumb__option">
                <a href="/">Home</a>
                <span>Cửa hàng</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- Breadcrumb Section End -->
    <!-- Product Section Begin -->
    <section class="product spad">
      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-5">
            <div class="sidebar">
              <div class="sidebar__item">
                <h4>Categories</h4>
                <ul>
                    <li><router-link :to="`/shop`">All</router-link></li>
                </ul>
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
              <div class="sidebar__item">
                <div class="latest-product__text">
                  <h4>Latest Products</h4>
                  <LatestProduct
                    v-for="product in latProducts"
                    :key="product.id"
                    :product="product"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-9 col-md-7">
            <div class="filter__item">
              <div class="row">
                <div class="col-lg-4 col-md-4">
                  <div class="filter__found">
                    <h6><span>{{category.products.length}}</span> Products found</h6>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <AllProduct
                v-for="product in category.products"
                :key="product.id"
                :product="product"
              />
            </div>
            <ul class="pagination">
              <li>
                <button aria-label="Previous" @click="loadPrev()">
                  <i class="fa fa-long-arrow-left"></i>
                </button>
              </li>
              <li>
                <button aria-label="Next" @click="loadNext()">
                  <i class="fa fa-long-arrow-right"></i>
                </button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
    <!-- Product Section End -->
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

import AllProduct from "@/components/AllProduct";
import LatestProduct from "@/components/LatestProduct";

export default {
  name: "Category",
  components: {
    AllProduct,
    LatestProduct,
  },
  data() {
    return {
      category: {
        products: [],
      },
      latProducts: [],
      categories: [],

      currentPage: 1,
    };
  },
  mounted() {
    this.getProductByCategory();
    this.getLatProducts();
    this.getloadCategories();
  },
  watch: {
    $route(to, from) {
      if (to.name === "Category") {
        this.getProductByCategory();
      }
    },
  },
  methods: {
    loadNext() {
      const categorySlug = this.$route.params.category_slug;
      this.currentPage += 1;
      this.getProductByCategory();
      this.$router.push(`/shop/${categorySlug}/?page=${this.currentPage}`)
    },
    
    loadPrev() {
      const categorySlug = this.$route.params.category_slug;
      this.currentPage -= 1;
      this.getProductByCategory();
      this.$router.push(`/shop/${categorySlug}/?page=${this.currentPage}`)
    },
    async getLatProducts() {
      this.$store.commit("setIsLoading", true);
      
      await axios
      .get("/api/v1/products/latest/")
      .then((response) => {
        this.latProducts = response.data;
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
    async getProductByCategory() {
      const categorySlug = this.$route.params.category_slug;

      this.$store.commit("setIsLoading", true);

      axios
        .get(`/api/v1/categories/${categorySlug}/?page=${this.currentPage}`)
        .then((response) => {
          this.category = response.data;

          document.title = this.category.name + " | Djackets";
        })
        .catch((error) => {
          console.log(error);

          toast({
            message: "Something went wrong. Please try again.",
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
