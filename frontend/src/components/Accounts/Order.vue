<template>
  <section class="py-5 my-5">
    <div class="MyAccount">
      <div class="container">
        <h1 class="mb-5">Account Settings</h1>
        <div class="column is-12">
          <button @click="logout()" class="btn btn-primary">Log out</button>
        </div>
        <div class="bg-white shadow rounded-lg d-block d-sm-flex">
          <div class="profile-tab-nav border-right">
            <div class="p-4">
              <div class="img-circle text-center mb-3">
                <img src="./avatar.png" alt="Image" class="shadow" />
              </div>
              <h4 class="text-center"></h4>
            </div>
            <div
              class="nav flex-column nav-pills"
              id="v-pills-tab"
              role="tablist"
              aria-orientation="vertical"
            >
              <router-link
                class="nav-link"
                id="account-tab"
                data-toggle="pill"
                to="/my-account"
                role="tab"
                aria-controls="account"
                aria-selected="true"
              >
                <i class="fa fa-home text-center mr-1"></i>
                Account
              </router-link>
              <router-link
                class="nav-link"
                id="password-tab"
                data-toggle="pill"
                to="/my-account/password"
                role="tab"
                aria-controls="password"
                aria-selected="false"
              >
                <i class="fa fa-key text-center mr-1"></i>
                Password
              </router-link>
              <router-link
                class="nav-link active"
                id="order-tab"
                data-toggle="pill"
                to="/my-account/order"
                role="tab"
                aria-controls="order"
                aria-selected="false"
              >
                <i class="fa fa-shopping-bag text-center mr-1"></i>
                Order
              </router-link>
            </div>
          </div>
          <div class="tab-content p-4 p-md-5" id="v-pills-tabContent">
            <div
              class="tab-pane fade active show"
              id="password"
              role="tabpanel"
              aria-labelledby="password-tab"
            >
              <h3 class="mb-4">My orders</h3>
              <OrderSummary
                v-for="order in orders"
                :key="order.id"
                :order="order"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <router-view />
</template>

<script>
import axios from "axios";

import OrderSummary from "@/components/OrderSummary.vue";
import { RouterView } from "vue-router";

export default {
  name: "MyAccount",
  components: {
    OrderSummary,
  },
  data() {
    return {
      orders: [],
    };
  },
  mounted() {
    document.title = "My account | BK";

    this.getMyOrders();
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");

      this.$store.commit("removeToken");

      this.$router.push("/");
    },
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
  },
};
</script>
