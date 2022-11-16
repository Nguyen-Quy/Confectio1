<template>
  <div class="Shop" :class="{ loading: loading }">
    <Search />
    <Breadcrumb />
    <!-- Product Section Begin -->
    <section class="product spad">
      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-5">
            <div class="sidebar">
              <Category />
              <LatestProduct />
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

import Category from "@/components/Category";
import Breadcrumb from "@/components/Breadcrumb";
import Search from "@/views/Search";
import AllProduct from "@/components/AllProduct";
import LatestProduct from "@/components/LatestProduct";

export default {
  name: "ProductByCategory",
  components: {
    AllProduct,
    LatestProduct,
    Search,
    Category,
    Breadcrumb,
  },
  data() {
    return {
      category: {
        products: [],
      },
      currentPage: 1,
    };
  },
  mounted() {
    this.getProductByCategory();
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
