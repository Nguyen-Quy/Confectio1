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
                <img src="../assets/img/avatar.png" alt="Image" class="shadow-img" />
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
            <form
              class="tab-pane fade show active"
              id="account"
              role="tabpanel"
              aria-labelledby="account-tab"
              @submit.prevent="submitForm"
            >
              <h3 class="mb-4">Account Settings</h3>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <label>First Name</label>
                    <input v-model="first_name" type="text" class="form-control" />
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group">
                    <label>Last Name</label>
                    <input v-model="last_name" type="text" class="form-control"/>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group">
                    <label>Email</label>
                    <input
                      v-model="email"
                      type="text"
                      class="form-control"
                    />
                  </div>
                </div>
              </div>
              <p v-for="error in errors" :key="error">{{ error }}</p>
              <div>
                <input type="submit" class="btn btn-primary">
              </div>
            </form>
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
      first_name: "",
      last_name: "",
      email: ""
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
    submitForm() {
      this.errors = [];


      if (this.first_name === "") {
        this.errors.push("The first name No empty ");
      }

      if (this.last_name === "") {
        this.errors.push("The last name No empty");
      }
      if (this.email === "") {
        this.errors.push("The email No empty");
      }

      if (!this.errors.length) {
        const formData = {
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
        };

        axios
          .post(`/api/v1/users/edit-profile/`, formData)
          .then((response) => {

          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }

              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");

              console.log(JSON.stringify(error));
            }
          });
        }
      }
  },
};
</script>
