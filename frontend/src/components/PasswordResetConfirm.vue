<template>
  <div class="reset-page">
    <div class="wallpaper-register"></div>
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
          <div class="card singup">
            <h1>Reset Password</h1>
            <form class="form-group" @submit.prevent="submitForm">
              <input
                v-model="new_password"
                type="password"
                class="form-control"
                placeholder="New Password"
                required
              />
              <input
                v-model="re_new_password"
                type="password"
                class="form-control"
                placeholder="Renew Password"
                required
              />
              <input
                v-model="uid"
                type="hidden"
                class="form-control"
                required
              />
              <input
                v-model="token"
                type="hidden"
                class="form-control"
                required
              />
              <input
                type="submit"
                class="btn btn-primary"
                @click="doResetpassword"
              />
              <p v-for="error in errors" :key="error">{{ error }}</p>
              <p>
                Already have an account?
                <a
                  href="/log-in"
                  @click="
                    (registerActive = !registerActive), (emptyFields = false)
                  "
                  >Sign in here</a
                >
              </p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignUp",
  data() {
    return {
      new_password: "",
      re_new_password: "",
      uid: "",
      token: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Sign Up";
  },
  methods: {
    submitForm() {
      this.errors = [];


      if (this.new_password === "") {
        this.errors.push("The new password is missing!");
      }

      if (this.new_password !== this.re_new_password) {
        this.errors.push("The current password doesn't match");
      }

      if (!this.errors.length) {
        const formData = {
          new_password: this.new_password,
          uid: this.$route.params.uid,
          token: this.$route.params.token,
        };

        axios
          .post(`/api/v1/users/reset_password_confirm/`, formData)
          .then((response) => {
            const token = response.data.auth_token;

            this.$store.commit("setToken", token);

            axios.defaults.headers.common["Authorization"] = "Token " + token;

            localStorage.setItem("token", token);

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
