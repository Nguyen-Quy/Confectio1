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
              <h3>Price</h3>
              <div class="wrapper">
                <div class="price-input">
                  <div class="field">
                    <span>Min</span>
                    <input type="number" class="input-min input1" value="10000">
                  </div>
                  <div class="separator">-</div>
                  <div class="field">
                    <span>Max</span>
                    <input type="number" class="input-max input1" value="1500000">
                  </div>
                </div>
                <div class="slider">
                  <div class="progress"></div>
                </div>
                <div class="range-input">
                  <input type="range" class="range-min input1" min="0" max="1500000" value="10000" step="5000">
                  <input type="range" class="range-max input1" min="0" max="1500000" value="1500000" step="5000">
                </div>
              </div>
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
    this.getSlider();
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
    async getSlider(){
      const rangeInput = document.querySelectorAll(".range-input input"),
      priceInput = document.querySelectorAll(".price-input input"),
      progress = document.querySelector(".slider .progress");
      let priceGap = 1000;
      priceInput.forEach(input =>{
        input.addEventListener("input", e => {
          let minVal = parseInt(priceInput[0].value),
          maxVal = parseInt(priceInput[1].value);
          if((maxVal - minVal >= priceGap) && maxVal <=10000){
          
            if(e.target.className === "input-min"){
              rangeInput[0].value = minVal;
              progress.style.left = (minVal / rangeInput[0].max) * 100 + "%";
            }else{
              rangeInput[1].value = maxVal;
              progress.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
            }
          }
        });
      });
      rangeInput.forEach(input =>{
        input.addEventListener("input", e => {
          let minVal = parseInt(rangeInput[0].value),
          maxVal = parseInt(rangeInput[1].value);
          if(maxVal - minVal < priceGap){
            if(e.target.className === "range-min"){
              rangeInput[0].value = maxVal - priceGap;
            }else{
              rangeInput[1].value = minVal + priceGap;
            }
          }else{
            priceInput[0].value = minVal;
            priceInput[1].value = maxVal;
            progress.style.left = (minVal / rangeInput[0].max) * 100 + "%";
            progress.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
          }
        });
      });
    }
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

.wrapper{
  width: 250px;
  background: rgba(255, 255, 255);
  border-radius: 10px;
  padding: 5px 5px 10px;
}
.price-input{
  width: 100%;
  display: flex;
  margin: 30px 0 35px;
}
.price-input .field{
  height: 50px;
  width: 300px;
  display:flex;
  align-items: center;
}
.field .input1{
  width: 65%;
  height: 40%;
  outline: none;
  font-size: 13px;
  text-align: center;
  margin-left: 10px;
  border-radius: 5px;
  border: 1px solid rgb(0, 0, 0);
  -moz-appearance: textfield;
}
.input1[type="number"]::-webkit-outer-spin-button,
.input1[type="number"]::-webkit-inner-spin-button{
  -webkit-appearance: none;
}
.price-input .separator{
  width: 130px;
  display: flex;
  font-size: 19px;
  align-items: center;
  justify-content: center;
}
.slider{
  height: 5px;
  border-radius: 5px;
  background: #ddd;
  position: relative;
}
.slider .progress{
  height: 5px;
  left: 10px;
  right: 10px;
  position:absolute;
  border-radius: 5px;
  background: #17A2B8;
}
.range-input{
  position: relative;
}
.range-input .input1{
  position: absolute;
  top: -5px;
  height: 5px;
  width: 100%;
  pointer-events:none;
  background: none;
  -webkit-appearance: none;
}
.input1[type="range"]::-webkit-slider-thumb{
  height: 17px;
  width: 17px;
  border-radius: 50%;
  pointer-events:auto;
  -webkit-appearance: none;
  background: #17A2B8;
}
.input1[type="range"]::-moz-range-thumb{
  height: 17px;
  width: 17px;
  border: none;
  border-radius: 50%;
  pointer-events:auto;
  -moz-appearance: none;
  background: #17A2B8;
}
</style>
