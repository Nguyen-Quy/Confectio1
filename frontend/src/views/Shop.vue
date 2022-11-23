<template>
  <div class="Shop">
    <Search />
    <Breadcrumb />
    <section class="product spad">
      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-5">
            <div class="sidebar">
              <Category />
              <LatestProduct />
            </div>
          </div>
          <div class="col-lg-9 col-md-7" ref="top">
            <div class="filter__item">
              <div class="row">
                <div class="col-lg-4 col-md-4">
                  <div class="filter__found">
                    <h6>
                      <span>{{ allProducts.results.length }}</span> Products found
                    </h6>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <AllProduct
                v-for="product in allProducts.results" :key="product.id" :product="product"
              />
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
  name: "ShopPage",
  data() {
    return {
      allProducts: {
        results: []
      },
      currentPage: 1,
      showNextButton: false,
      showPrevButton: false,
    };
  },
  components: {
    AllProduct,
    LatestProduct,
    Search,
    Category,
    Breadcrumb,
  },
  mounted() {
    this.getAllProducts();
    this.scrollToElement();
    (document.title = "Shop | BK");
  },
  methods: {
    loadNext() {
      this.currentPage += 1;
      this.getAllProducts();
      this.$router.push(`/shop/?page=${this.currentPage}`);
    },
    loadPrev() {
      this.currentPage -= 1;
      this.getAllProducts();
      this.$router.push(`/shop/?page=${this.currentPage}`);
    },
    scrollToElement() {
      this.$refs["top"].scrollIntoView({ behavior: "smooth" });
    },
    async getAllProducts() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get(`/api/v1/products/?page=${this.currentPage}`)
        .then((response) => {
          this.showPrevButton = response.data.previous;
          this.showNextButton = response.data.next;

          this.allProducts = response.data;
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
