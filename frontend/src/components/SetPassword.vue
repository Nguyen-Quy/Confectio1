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
                class="nav-link"
                id="order-tab"
                data-toggle="pill"
                to="/my-account"
                role="tab"
                aria-controls="order"
                aria-selected="false"
              >
                <i class="fa fa-shopping-bag text-center mr-1"></i>
                Order
              </router-link>
              <router-link
                class="nav-link active"
                id="password-tab"
                data-toggle="pill"
                to="/my-account/set-password"
                role="tab"
                aria-controls="password"
                aria-selected="false"
              >
                <i class="fa fa-key text-center mr-1"></i>
                Set Password
              </router-link>
            </div>
          </div>
          <div class="tab-content p-4 p-md-5" id="v-pills-tabContent">
            <form
              class="tab-pane fade active show"
              id="password"
              role="tabpanel"
              aria-labelledby="password-tab"
              @submit.prevent="submitForm"
            >
              <h3 class="mb-4">Password Settings</h3>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <label>Old password</label>
                    <input v-model="current_password" type="password" class="form-control" required/>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <label>New password</label>
                    <input v-model="new_password" type="password" class="form-control" required/>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group">
                    <label>Confirm new password</label>
                    <input v-model="re_new_password" type="password" class="form-control" required/>
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

export default {
  name: "MyAccount",
  components: {
    OrderSummary,
  },
  data() {
    return {
      orders: [],
      current_password: "",
      new_password: "",
      re_new_password: "",
      errors: [],
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


      if (this.current_password === "") {
        this.errors.push("The current password not true");
      }
      if (this.new_password === "") {
        this.errors.push("The new password is too short");
      }

      if (this.new_password !== this.re_new_password) {
        this.errors.push("The current password doesn't match");
      }

      if (!this.errors.length) {
        const formData = {
          current_password: this.current_password,
          new_password: this.new_password,
        };

        axios
          .post('/api/v1/users/set_password/', formData)
          .then((response) => {
            this.$router.push("/log-in");
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
    },
  },
};
</script>
