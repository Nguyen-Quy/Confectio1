<template>
  <div class="forgot-password">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
          <div class="card-forgot-password">
            <form class="form-group" @submit.prevent="submitForm">
                <h3>Forget Password</h3>
                <input
                v-model="email"
                type="email"
                class="form-control form-control-lg"
                placeholder="Email address"
                required
                />
                <button type="submit" class="btn btn-dark btn-lg btn-block">
                Reset password
              </button>
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
  name: "ForgotPassword",
  data() {
    return {
      email: "",
    };
  },
  mounted() {
    document.title = "Forget Password";
  },
  methods: {
    submitForm() {
      const response = axios.post(`api/v1/request-reset-email/`, {
        email: this.email
        
      })
      this.$router.push("/reset-password-done");
      console.log(response)
    }
  },
  
};
</script>
