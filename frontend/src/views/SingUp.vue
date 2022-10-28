<template>
    <div class="singup-page">
        <div class="wallpaper-register"></div>
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
                    <div class="card singup">
                        <h1>Sign Up</h1>
                        <form class="form-group">
                            <input
                                v-model="emailReg"
                                type="email"
                                class="form-control"
                                placeholder="Email"
                                required
                            />
                            <input
                                v-model="passwordReg"
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
                            <input type="submit" class="btn btn-primary" @click="doRegister" />
                            <p>
                                Already have an account?
                                <a
                                href="/login"
                                @click="(registerActive = !registerActive), (emptyFields = false)"
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
export default {
  name: "SingUpPage",
  data() {
    return {
      emailLogin: "",
      passwordLogin: "",
      emailReg: "",
      passwordReg: "",
      confirmReg: "",
      registerActive: false,
    emptyFields: false
    };
  },
  methods: {
    doRegister() {
      if (
        this.emailReg === "" ||
        this.passwordReg === "" ||
        this.confirmReg === ""
      ) {
        this.emptyFields = true;
      } else {
        alert("You are now registered");
      }
    },
  },
};
</script>
