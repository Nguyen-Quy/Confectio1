import { createRouter, createWebHistory } from "vue-router";

import store from "../store";

import Home from "../views/Home.vue";
import Shop from "../views/Shop.vue";
import Product from "../views/Product.vue";
import Category from "../views/Category.vue";
import Search from "../views/Search.vue";
import Cart from "../views/Cart.vue";
import SignUp from "../views/SignUp.vue";
import LogIn from "../views/LogIn.vue";
import MyAccount from "../views/MyAccount.vue";
import SetPassword from '../components/SetPassword.vue';
import Checkout from "../views/Checkout.vue";
import Success from "../views/Success.vue";
import ForgetPassword from '../views/ForgetPassword.vue';
import PasswordResetConfirm from '../components/PasswordResetConfirm.vue';
import ResetPasswordDone from '../components/ResetPasswordDone.vue';

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/shop",
    name: "Shop",
    component: Shop,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  },
  {
    path: "/log-in",
    name: "LogIn",
    component: LogIn,
  },
  {path: '/forget-password', name: 'ForgetPassword', component: ForgetPassword},
  {path: '/reset-password/:uid/:token', name: 'PasswordResetConfirm', component: PasswordResetConfirm},
  {path: '/reset-password-done', name: 'ResetPasswordDone', component: ResetPasswordDone},
  {
    path: "/my-account",
    name: "MyAccount",
    component: MyAccount,
    meta: {
      requireLogin: true,
    },
  },
  {path: '/my-account/set-password', name: 'SetPassword', component: SetPassword},
  {
    path: "/search",
    name: "Search",
    component: Search,
  },
  {
    path: "/cart",
    name: "Cart",
    component: Cart,
  },
  {
    path: "/cart/success",
    name: "Success",
    component: Success,
  },
  {
    path: "/cart/checkout",
    name: "Checkout",
    component: Checkout,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/shop/:category_slug/:product_slug",
    name: "Product",
    component: Product,
  },
  {
    path: "/shop/:category_slug",
    name: "Category",
    component: Category,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !store.state.isAuthenticated
  ) {
    next({ name: "LogIn", query: { to: to.path } });
  } else {
    next();
  }
});

export default router;