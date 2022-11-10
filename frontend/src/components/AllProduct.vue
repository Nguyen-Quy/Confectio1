<template>
  <div class="col-lg-4 col-md-6 col-sm-6">
    <div class="product__item">
      <router-link :to="product.get_absolute_url" class="latest-product__item">
        <div class="product__item__pic set-bg">
          <img :src="product.get_thumbnail" merge-image="center">
        </div>
        <div class="product__item__text">
          <h6>
            <router-link :to="product.get_absolute_url">{{
              product.name
            }}</router-link>
          </h6>
          <h5>Giá: {{ product.price }} VNĐ</h5>
        </div>
      </router-link>
        <div class="button-group">
          <button class="button" @click="addToCart()">Add to cart</button>
            <router-link :to="product.get_absolute_url" class="product__item">
              <button class="button">Product Details</button>
            </router-link>
        </div>
    </div>
  </div>
  <router-view/>  
</template>

import 

<script>
export default {
  name: "AllProduct",
  props: {
    product: Object,
    color:{
      type: String
    },
    background:{
      type: String
    },
    disabled:{
      type: Boolean
    }
  },

  methods: {
    addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity,

            }  

            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
  },

};
</script>

<style scoped>
  .button {
    position: center;
    display: inline-block;
    margin: 0em 1;
    padding: 1em 0.5em;
    background: #fff;
    border: 3px solid tomato;
    border-radius: 10px;
    color: tomato;
    font-family: "Quicksand", sans-serif;
    font-size: 0.6em;
    font-weight: 800;
    letter-spacing: 0.2em;
    line-height: 1;
    text-decoration: none;
    text-transform: uppercase;
    cursor:pointer;
    transition: 0.3s;
  }

  .button:hover {
    background: tomato;
    color: #fff;
  }
</style>