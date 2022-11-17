<template>
  <div
    class="tab-pane fade active show"
    id="order"
    role="tabpanel"
    aria-labelledby="order-tab"
  >
    <h3 class="mb-4">My orders</h3>
    <div class="order-box box mb-4" v-for="order in orders" :key="order.id">
      <h3 class="is-size-4 mb-6">Order #{{ order.id }}</h3>

      <h4 class="is-size-5">Products</h4>

      <table class="table is-fullwidth">
        <thead>
          <tr>
            <th>Product</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Total</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="item in order.items" :key="item.product.id">
            <td>{{ item.product.name }}</td>
            <td>{{ item.product.price }} VNĐ</td>
            <td>{{ item.quantity }}</td>
            <td>{{ (getItemTotal(item) + getItemTotal(item)*0.1).toFixed(3) }} VNĐ</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "OrderSummary",
  data() {
    return {
      orders: [],
    };
  },
  mounted() {
    this.getMyOrders();
  },
  methods: {
    async getMyOrders() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/v1/orders/")
        .then((response) => {
          this.orders = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    orderTotalLength(order) {
      return order.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },
  },
};
</script>
