
<template>
  <div class="col-lg-4 col-md-6 col-sm-6">
    <div class="product__item">
      <div class="product__item-inner">
        <div class="img-container">
        <v-card>
          <div class="product-image-wrap">
            <img :src="product.get_thumbnail" class="image">
            <div class="overlay">
              <button class="btn btn-outline-secondary btn-sm" @click="addToCart()"><i class="fas fa-cart-plus mr-2" ></i>Add To Cart</button>
              <router-link :to="product.get_absolute_url" class="product__item">
                <button class="btn btn-outline-secondary btn-sm">Product Details</button>
              </router-link>
            </div>
          </div>
        </v-card>
        </div>
      </div>
      <div class="product__item__text">
        <h6>
          <router-link :to="product.get_absolute_url">{{
            product.name
          }}</router-link>
        </h6>
        <h5>Giá: {{ product.price }} VNĐ</h5>
      </div>
      </div>  
    </div>
  <router-view/>  
</template>

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

.img-container{
  position: relative;
}

.image{
  position: relative;
  transition: .5s ease;
  backface-visibility: hidden;
  border-radius: 10%;
  height:100%;
  width:100%;
  aspect-ratio: 4/3;
}

.overlay{
  transition: .5s ease;
  opacity: 0;
  position:absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%,50%);
}

.img-container:hover .image{
  opacity: 0.2;
}

.img-container:hover .overlay{
  opacity: 1;
}

.product__item{
  flex: 1 1 33.333%;
  width: 100%;
  padding: .5px;
}
.product__item-inner{
  position:relative;
  padding: 10px;
  border-radius: 10%;
  box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
}

.product__item-image-wrap .image{
  width: 100%;
  border-radius: 10%;
}
</style>
