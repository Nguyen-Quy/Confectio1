<template>
  <div class="login-page">
    <transition name="fade">
      <div v-if="!registerActive" class="wallpaper-login"></div>
    </transition>
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
          <div
            v-if="!registerActive"
            class="card login"
            :class="{ error: emptyFields }"
          >
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
              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" :key="error">{{ error }}</p>
              </div>
              <input type="submit" class="btn btn-primary" @click="doLogin" />
              <p>
                Chưa có tài khoản?
                <a
                  href="/sign-up"
                  @click="
                    (registerActive = !registerActive), (emptyFields = false)
                  "
                  >Đăng ký tại đây</a
                >
              </p>
              <p><a href="/forgot-password">Quên mật khẩu?</a></p>
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
  name: "LogIn",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Đăng nhập | Confectio";
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");

      const formData = {
        username: this.username,
        password: this.password,
      };

      await axios
        .post("/api/v1/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token;

          this.$store.commit("setToken", token);

          axios.defaults.headers.common["Authorization"] = "Token " + token;

          localStorage.setItem("token", token);

          const toPath = this.$route.query.to || "/cart";

          this.$router.push(toPath);
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
          } else {
            this.errors.push("Có lỗi xảy ra. Vui lòng thử lại.");

            console.log(JSON.stringify(error));
          }
        });
    },
  },
};
</script>
