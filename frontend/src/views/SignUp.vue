<template>
  <div class="singup-page">
    <div class="wallpaper-register"></div>
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
          <div class="card singup">
            <h1>Đăng nhập</h1>
            <form class="form-group" @submit.prevent="submitForm">
              <input
                v-model="username"
                type="text"
                class="form-control"
                placeholder="Username"
                required
              />
              <input
                v-model="password"
                type="password"
                class="form-control"
                placeholder="Password"
                required
              />
              <input
                v-model="confirmReg"
                type="password"
                class="form-control"
                placeholder="Confirm Password"
                required
              />
              <input
                v-model="email"
                type="email"
                class="form-control"
                placeholder="Email"
                required
              />
              <input
                type="submit"
                class="btn btn-primary"
                @click="doRegister"
              />
              <p v-for="error in errors" :key="error">{{ error }}</p>
              <p>
                Đã có tài khoản?
                <a
                  href="/log-in"
                  @click="
                    (registerActive = !registerActive), (emptyFields = false)
                  "
                  >Đăng nhập tại đây</a
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
import { toast } from "bulma-toast";

export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      password: "",
      confirmReg: "",
      email: "",
      errors: [],
    };
  },
  methods: {
    submitForm() {
      this.errors = [];

      if (this.username === "") {
        this.errors.push("The username is missing");
      }

      if (this.password === "") {
        this.errors.push("The password is too short");
      }

      if (this.password !== this.confirmReg) {
        this.errors.push("The passwords doesn't match");
      }

      if (this.email !== this.email) {
        this.errors.push("The passwords doesn't match");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
          email: this.email,
        };

        axios
          .post("/api/v1/users/", formData)
          .then((response) => {
            toast({
              message: "Đã tạo tài khoản, hãy đăng nhập!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });

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
              this.errors.push("Có lỗi xảy ra. Vui lòng thử lại.");

              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>
