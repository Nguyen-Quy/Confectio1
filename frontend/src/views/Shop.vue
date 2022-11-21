<template>
  <div class="Shop">
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
                    <h6>
                      <span>{{ allProducts.length }}</span> Products found
                    </h6>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <AllProduct
                v-for="product in allProducts"
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
  <router-view />
</template>

<script>
import axios from "axios";

import Category from "@/components/Category";
import Breadcrumb from "@/components/Breadcrumb";
import Search from "@/views/Search";
import AllProduct from "@/components/AllProduct";
import LatestProduct from "@/components/LatestProduct";

export default {
  name: "ShopPage",
  data() {
    return {
      allProducts: [],
      currentPage: 1,
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
    async getAllProducts() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get(`/api/v1/products/allproducts/?page=${this.currentPage}`)
        .then((response) => {
          this.allProducts = response.data;
          this.showPrevButton = response.data.previous;
          this.showNextButton = response.data.next;
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
