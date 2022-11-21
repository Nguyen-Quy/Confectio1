<style scoped>
  @import './assets/css/bootstrap.min.css';
  @import './assets/css/font-awesome.min.css';
  @import './assets/css/elegant-icons.css';
  @import './assets/css/nice-select.css';
  @import './assets/css/slicknav.min.css';
  @import './assets/css/style.css';
</style>

<template>
  <header class="header">
    <div class="container">
      <div class="row">
        <div class="col-lg-3">
          <div class="header__logo">
            <a href="/"><img src="../src/assets/img/logo.png" alt=""></a>
          </div>
        </div>
        
        <div class="col-lg-6">
          <nav class="header__menu">
            <ul>
              <li><router-link to="/">Home</router-link></li>
              <li><router-link to="/shop">Shop</router-link></li>
            </ul>
          </nav>
        </div>
        <div class="col-lg-3">
          <nav class="header__cart">
            <ul>
              <li>
                <router-link to="/cart" class="cart-drawer flex v-center" >
                  <div class="cart-number-badge">{{ cartTotalLength }}</div>
                  <i class="fa fa-shopping-cart" aria-hidden="true"></i>
                </router-link>
              </li>
              <li>
                <template v-if="$store.state.isAuthenticated">
                  <router-link to="/my-account" class="button is-light">My account</router-link>
                </template>

                <template v-else>
                  <router-link to="/log-in">Sign In / Sign Up</router-link>
                </template>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  </header>
  <section class="section">
    <router-view/>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
      cartTotalLength() {
          let totalLength = 0

          for (let i = 0; i < this.cart.items.length; i++) {
              totalLength += this.cart.items[i].quantity
          }

          return totalLength
      }
  }
}
</script>
