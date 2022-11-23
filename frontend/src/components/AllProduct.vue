<template>
  <div class="col-lg-4 col-md-6 col-sm-6">
    <div class="product__item">
      <div class="latest-product__item">
        <div class="product__item">
          <div class="product__item-inner">
            <div class="img-container">
              <v-card>
                <div class="product-image-wrap">
                  <img :src="product.get_thumbnail" class="image">
                  <div class="overlay">
                    <button class="btn btn-outline-secondary btn-sm" @click="addToCart()"><i
                        class="fas fa-cart-plus mr-2"></i>Add To Cart</button>
                    <router-link :to="`/shop${product.get_absolute_url}`" class="product__item">
                      <button class="btn btn-outline-secondary btn-sm">Product Details</button>
                    </router-link>
                  </div>
                </div>
              </v-card>
            </div>
            <div class="product__item__text">
              <h6>
                {{product.name}}
              </h6>
              <h5>Giá: {{ product.price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".") }} VNĐ</h5>
            </div>
          </div>
        </div>
        </div>
    </div>
  </div>
  <router-view />
</template>

<script>
export default {
  name: "AllProduct",
  props: {
    product: Object,
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
