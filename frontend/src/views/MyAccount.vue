<template>
  <section class="my-5">
    <div class="MyAccount">
      <div class="container">
        <h1 class="text-uppercase font-weight-normal mb-5">Account Settings</h1>
        <LogOut />
        <div class="bg-white shadow rounded-lg d-block d-sm-flex">
          <div class="profile-tab-nav border-right">
            <div class="p-4">
              <div class="img-circle text-center mb-3">
                <img src="../assets/img/avatar.png" alt="Image" class="shadow-img" />
              </div>
              <LoadCustomer />
            </div>
            <div
              class="nav flex-column nav-pills"
              id="v-pills-tab"
              role="tablist"
              aria-orientation="vertical"
            >
              <router-link
                class="nav-link active"
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
                class="nav-link"
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
            <OrderSummary />
          </div>
        </div>
      </div>
    </div>
  </section>
  <router-view />
</template>

<script>
import OrderSummary from "@/components/OrderSummary.vue";
import LogOut from "@/views/LogOut.vue";
import LoadCustomer from "@/components/LoadCustomer";

export default {
  name: "MyAccount",
  components: {
    OrderSummary,
    LogOut,
    LoadCustomer,
  },
  mounted() {
    document.title = "My account | BK";
  },
};
</script>
