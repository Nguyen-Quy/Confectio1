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
                <img src="../assets/img/avatar.png" alt="Image" class="shadow" />
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
                class="nav-link active"
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
                class="nav-link"
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
              class="tab-pane fade show active"
              id="account"
              role="tabpanel"
              aria-labelledby="account-tab"
            >
              <h3 class="mb-4">Account Settings</h3>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <label>First Name</label>
                    <input type="text" class="form-control" value="" />
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group">
                    <label>Last Name</label>
                    <input type="text" class="form-control" value="" />
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group">
                    <label>Email</label>
                    <input
                      type="text"
                      class="form-control"
                      value=""
                    />
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group">
                    <label>Phone number</label>
                    <input
                      type="text"
                      class="form-control"
                      value=""
                    />
                  </div>
                </div>
              </div>
              <div>
                <button class="btn btn-primary">Update</button>
                <button class="btn btn-light">Cancel</button>
              </div>
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