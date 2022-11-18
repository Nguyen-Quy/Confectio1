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
                <h4>Price</h4>
              <div class="wrapper">
                <div class="price-input">
                  <div class="field">
                    <span>Min</span>
                    <input type="number" class="input-min" value="10000">
                  </div>
                  <div class="separator">-</div>
                  <div class="field">
                    <span>Max</span>
                    <input type="number" class="input-max" value="1500000">
                  </div>
                </div>
                <div class="slider">
                  <div class="progress"></div>
                </div>
                <div class="range-input">
                  <input type="range" class="range-min" min="0" max="1500000" value="10000" step="5000">
                  <input type="range" class="range-max" min="0" max="1500000" value="1500000" step="5000">
                </div>
              </div>
              <div class="sidebar__item">
                <div class="latest-product__text">
                  <h4>Latest Products</h4>
                  <LastestProduct
                    v-for="product in latestProducts"
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
                :product="product"
              />
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- Product Section End -->
  </div>
  <router-view/>
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
    };
  },
  components: {
    AllProduct,
    LastestProduct,
  },
  mounted() {
    this.getAllProducts(),
      this.getLastProducts(),
      this.getloadCategories(),
      this.getSlider(),
      (document.title = "Shop | BK");
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
        .get(`/api/v1/products/latest/`)
        .then((response) => {
          this.latestProducts = response.data;
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
            progress.style.right =100 - (maxVal / rangeInput[1].max) * 100 + "%";
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

.field input{
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

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button{
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

.range-input input{
  position: absolute;
  top: -5px;
  height: 5px;
  width: 100%;
  pointer-events:none;
  background: none;
  -webkit-appearance: none;
}

input[type="range"]::-webkit-slider-thumb{
  height: 17px;
  width: 17px;
  border-radius: 50%;
  pointer-events:auto;
  -webkit-appearance: none;
  background: #17A2B8;
}

input[type="range"]::-moz-range-thumb{
  height: 17px;
  width: 17px;
  border: none;
  border-radius: 50%;
  pointer-events:auto;
  -moz-appearance: none;
  background: #17A2B8;
}
</style>
