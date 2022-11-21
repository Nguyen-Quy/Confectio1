<template>
  <div class="Cart">
    <div class="container">
      <section class="page-cart">
        <div>
          <h1 class="text-uppercase font-weight-normal">shopping bag</h1>
        </div>
        <div class="bg-white rounded-top mt-5" id="zero-pad">
          <div class="row d-flex justify-content-center">
            <div class="cart-item col-lg-10 col-12 pt-3" v-if="cartTotalLength">
              <div class="d-flex flex-column pt-4">
                <div class="font-weight-normal">
                  {{ cartTotalLength }} items
                </div>
              </div>
              <div class="d-flex flex-row px-lg-5 mx-lg-5 mobile" id="heading">
                <div class="px-lg-5 mr-lg-5" id="produc">PRODUCTS</div>
                <div class="px-lg-5 ml-lg-5" id="prc">PRICE</div>
                <div class="px-lg-5 ml-lg-1" id="quantity">QUANTITY</div>
                <div class="px-lg-5 ml-lg-3" id="total">TOTAL</div>
              </div>
              <CartItem
                v-for="item in cart.items"
                :key="item.product.id"
                :initialItem="item"
                @removeFromCart="removeFromCart"
              />
            </div>

            <p v-else>You don't have any products in your cart...</p>
          </div>
        </div>
        <div class="container bg-light rounded-bottom py-4" id="zero-pad">
          <div class="row d-flex justify-content-center">
            <div class="col-lg-10 col-12">
              <div class="d-flex justify-content-between align-items-center">
                <div>
                  <router-link
                    to="/Shop"
                    class="btn btn-sm bg-light border border-dark"
                  >
                    GO SHOP
                  </router-link>
                </div>
                <div class="px-md-0 px-1" id="footer-font">
                  <b class="pl-md-4"
                    >SUBTOTAL<span class="pl-md-4"
                      >{{ cartTotalPrice.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".") }} VNĐ</span
                    ></b
                  >
                </div>
                <div>
                  <router-link
                    to="/cart/checkout"
                    class="btn btn-sm bg-dark text-white px-lg-5 px-3"
                  >
                    CONTINUE
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import CartItem from "@/components/CartItem.vue";

export default {
  name: "Cart",
  components: {
    CartItem,
  },
  data() {
    return {
      cart: {
        items: [],
      },
    };
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(
        (i) => i.product.id !== item.product.id
      );
    },
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.product.price * curVal.quantity);
      }, 0);
    },
  },
};
</script>
