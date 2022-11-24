<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="row">
        <div class="col-lg-5">
          <v-card>
            <div class="product__item-inner_detail">
              <div class="img-container_detail">
                <div class="product-image-wrap_detail">
                  <img :src="product.get_thumbnail" class="image">
                </div>
              </div>
            </div>
          </v-card>
        </div>
        <div class="col-lg-7">
          <div class="title_details">
            <h1>{{ product.name }}</h1>
            <p>{{ product.description }}</p>
            <p><strong>Giá: </strong>{{ String(product.price).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".") }} VNĐ
            </p>
          </div>
          <div class="field has-addons mt-6">
            <div class="control">
              <input type="number" class="input" min="1" v-model="quantity" />
            </div>

            <div class="control">
              <button class="button is-dark" @click="addToCart()">
                Add to cart
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "Product",
  props: {
    product: Object,
  },
  data() {
    return {
      product: {},
      quantity: 1,
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    async getProduct() {
      this.$store.commit("setIsLoading", true);

      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;

      await axios
        .get(`/api/v1/categories/${category_slug}/${product_slug}/`)
        .then((response) => {
          this.product = response.data;

          document.title = this.product.name + "Product detail | BK";
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        product: this.product,
        quantity: this.quantity,
      };

      this.$store.commit("addToCart", item);

      toast({
        message: "The product was added to the cart",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
    },
  },
};

</script>

<style>
.page-product {
  background: rgb(243, 214, 142);
}

.image_detail {
  position: relative;
  left: 5%;
  border-radius: 10%;
  height: 80%;
  width: 80%;
  aspect-ratio: 7/8;
}

.product__item-inner_detail {
  position: relative;
  left: 5%;
  border-radius: 10%;
  height: 100%;
  width: 90%;
  box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
}

.img-container_detail {
  position: relative;
}

.title_details {
  font-family: Calibri;
}
</style>
