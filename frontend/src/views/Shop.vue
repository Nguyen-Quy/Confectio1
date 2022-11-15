<template>
  <div class="Shop">
    <!-- Hero Section Begin -->
    <section class="hero hero-normal">
      <div class="container">
        <div class="hero__search">
          <div class="hero__search__form">
            <form method="get" action="/search">
              <input
                type="text"
                placeholder="What do yo u need?"
                name="query" />
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
                  :category="category">
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
                    data-max="540">
                    <div
                      class="ui-slider-range ui-corner-all ui-widget-header"></div>
                    <span
                      tabindex="0"
                      class="ui-slider-handle ui-corner-all ui-state-default"></span>
                    <span
                      tabindex="0"
                      class="ui-slider-handle ui-corner-all ui-state-default"></span>
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
                    v-for="product in latestProducts.slice(0, 6)"
                    :key="product.id"
                    :product="product" />
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-9 col-md-7" ref="top">
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
                    <h6>
                      <span>{{ allProducts.length }}</span> Products found
                    </h6>
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
                v-for="product in allProducts"
                :key="product.id"
                :product="product" />
            </div>
            <div class="d-flex justify-content-center">
              <template v-if="showPrevButton">
                <button
                  @click="
                    loadPrev();
                    scrollToElement();
                  "
                  class="mx-1">
                  <i class="fa fa-long-arrow-left mx-1 my-1"></i>
                </button>
              </template>
              <template v-if="showNextButton">
                <button
                  @click="
                    loadNext();
                    scrollToElement();
                  "
                  class="mx-1">
                  <i class="fa fa-long-arrow-right mx-1 my-1"></i>
                </button>
              </template>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- Product Section End -->
  </div>
  <router-view />
</template>

<script>
import axios from "axios";

import AllProduct from "@/components/AllProduct";
import LastestProduct from "@/components/LastestProduct";

export default {
  name: "ShopPage",
  data() {
    return {
      allProducts: [],
      latestProducts: [],
      categories: [],

      currentPage: 1,
      showNextButton: false,
      showPrevButton: false,
    };
  },
  components: {
    AllProduct,
    LastestProduct,
  },
  mounted() {
    this.getAllProducts();
    this.getLastProducts();
    this.getloadCategories();
    this.scrollToElement();
    document.title = "Shop | BK";
  },
  methods: {
    loadNext() {
      this.currentPage += 1;
      this.getAllProducts();
      this.$router.push(`/shop/?page=${this.currentPage}`);
      // window.scrollTo(0, 420);
    },
    loadPrev() {
      this.currentPage -= 1;
      this.getAllProducts();
      this.$router.push(`/shop/?page=${this.currentPage}`);
      // window.scrollTo(0, 420);
    },
    scrollToElement() {
      this.$refs["top"].scrollIntoView({ behavior: "smooth" });
    },
    async getAllProducts() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get(`/api/v1/products/?page=${this.currentPage}`)
        .then(response => {
          // if (response.data.previous) {
          //   this.showPrevButton = true;
          // }
          // if (response.data.next) {
          //   this.showNextButton = true;
          // }
          this.showPrevButton = response.data.previous;
          this.showNextButton = response.data.next;

          this.allProducts = response.data.results;
        })
        .catch(error => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    async getLastProducts() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get(`/api/v1/products/latest/`)
        .then(response => {
          this.latestProducts = response.data;
        })
        .catch(error => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    async getloadCategories() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get(`/api/v1/categories/`)
        .then(response => {
          this.categories = response.data;
        })
        .catch(error => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
<style>
.pagination-container {
  display: flex;
  column-gap: 10px;
}
.paginate-buttons {
  height: 40px;
  width: 40px;
  border-radius: 20px;
  cursor: pointer;
  background-color: rgb(242, 242, 242);
  border: 1px solid rgb(217, 217, 217);
  color: black;
}
.paginate-buttons:hover {
  background-color: #d8d8d8;
}
.active-page {
  background-color: #3498db;
  border: 1px solid #3498db;
  color: white;
}
.active-page:hover {
  background-color: #2988c8;
}
</style>
