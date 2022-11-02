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
                <h4>Price</h4>
                <div class="price-range-wrap">
                  <div
                    class="price-range ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content"
                    data-min="10"
                    data-max="540"
                  >
                    <div
                      class="ui-slider-range ui-corner-all ui-widget-header"
                    ></div>
                    <span
                      tabindex="0"
                      class="ui-slider-handle ui-corner-all ui-state-default"
                    ></span>
                    <span
                      tabindex="0"
                      class="ui-slider-handle ui-corner-all ui-state-default"
                    ></span>
                  </div>
                  <div class="range-slider">
                    <div class="price-input">
                      <input type="text" id="minamount" />
                      <input type="text" id="maxamount" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="sidebar__item">
                <div class="latest-product__text">
                  <h4>Latest Products</h4>
                  <LastestProduct
                    v-for="product in lastProducts"
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
                <div class="col-lg-4 col-md-5">
                  <div class="filter__sort">
                    <span>Sort By</span>
                    <select>
                      <option value="0">Default</option>
                      <option value="0">Default</option>
                    </select>
                  </div>
                </div>
                <div class="col-lg-4 col-md-4">
                  <div class="filter__found">
                    <h6><span>{{category.products.length}}</span> Products found</h6>
                  </div>
                </div>
                <div class="col-lg-4 col-md-3">
                  <div class="filter__option">
                    <span class="icon_grid-2x2"></span>
                    <span class="icon_ul"></span>
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
            <div class="product__pagination">
              <a href="#">1</a>
              <a href="#">2</a>
              <a href="#">3</a>
              <a href="#"><i class="fa fa-long-arrow-right"></i></a>
            </div>
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
import LastestProduct from "@/components/LastestProduct";

export default {
  name: "Category",
  components: {
    AllProduct,
    LastestProduct,
  },
  data() {
    return {
      category: {
        products: [],
      },
      allProducts: [],
      lastProducts: [],
      categories: [],
    };
  },
  mounted() {
    this.getCategory();
    this.getAllProducts();
    this.getLastProducts();
    this.getloadCategories();
  },
  watch: {
    $route(to, from) {
      if (to.name === "Category") {
        this.getCategory();
      }
    },
  },
  methods: {
    async getAllProducts() {
      this.$store.commit("setIsLoading", true);
      
      await axios
      .get(`/api/v1/products/`)
      .then((response) => {
        this.allProducts = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
      
      this.$store.commit("setIsLoading", false);
    },
    async getLastProducts() {
      this.$store.commit("setIsLoading", true);
      
      await axios
      .get("/api/v1/latest-products/")
      .then((response) => {
        this.lastProducts = response.data;
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
    async getCategory() {
      const categorySlug = this.$route.params.category_slug;

      this.$store.commit("setIsLoading", true);

      axios
        .get(`/api/v1/products/${categorySlug}/`)
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
