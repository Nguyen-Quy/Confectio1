<template>
  <div
    class="d-flex flex-row justify-content-between align-items-center pt-lg-4 pt-2 pb-3 border-bottom mobile"
  >
    <div class="d-flex flex-row align-items-center">
      <router-link :to="`/shop${item.product.get_absolute_url}`">
        <img
            :src="item.product.get_image"
            width="150"
            height="150"
            alt=""
            id="image"
        />
      </router-link>
      <div class="title-product d-flex flex-column pl-md-3 pl-1">
        <h6>{{item.product.name}}</h6>
      </div>
    </div>
    <div class="pl-md-0 pl-1"><b>{{ item.product.price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".") }} VNĐ</b></div> 
    <div class="pl-md-0 pl-2">
      <a class="fa fa-minus-square" @click="decrementQuantity(item)"></a>
      <span class="px-md-3 px-1">{{ item.quantity }}</span>
      <a class="fa fa-plus-square " @click="incrementQuantity(item)"></a>
    </div>
    <div class="pl-md-0 pl-1"><b>{{ getItemTotal(item).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".") }} VNĐ</b></div>
    <button class="close" @click="removeFromCart(item)">&times;</button>
  </div>
</template>

<script>
export default {
  name: "CartItem",
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem,
    };
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    decrementQuantity(item) {
      item.quantity -= 1;

      if (item.quantity === 0) {
        this.$emit("removeFromCart", item);
      }

      this.updateCart();
    },
    incrementQuantity(item) {
      item.quantity += 1;

      this.updateCart();
    },
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
    removeFromCart(item) {
      this.$emit("removeFromCart", item);

      this.updateCart();
    },
  },
};
</script>
