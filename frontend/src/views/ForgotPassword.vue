<template>
  <div class="forgot-password">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
          <div class="card singup">
            <form class="form-group">
              <h3>Quên mật khẩu</h3>
              <input
                type="email"
                class="form-control form-control-lg"
                placeholder="Địa chỉ email"
              />
              <button type="submit" class="btn btn-dark btn-lg btn-block">
                Đặt lại mật khẩu
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "ForgotPassword",
  data() {
    return {};
  },
};
</script>
