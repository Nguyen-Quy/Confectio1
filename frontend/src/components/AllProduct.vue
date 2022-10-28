<template>
  <div class="col-lg-4 col-md-6 col-sm-6">
    <div class="product__item">
      <div class="product__item__pic set-bg">
        <img :src="product.get_thumbnail">
        <ul class="product__item__pic__hover">
          <li>
            <a href="#"><i class="fa fa-heart"></i></a>
          </li>
          <li>
            <a href="#"><i class="fa fa-retweet"></i></a>
          </li>
          <li>
            <a href="#"><i class="fa fa-shopping-cart"></i></a>
          </li>
        </ul>
      </div>
      <div class="product__item__text">
        <h6>
          <router-link :to="product.get_absolute_url">{{
            product.name
          }}</router-link>
        </h6>
        <h5>{{ product.price }}</h5>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductBox",
  props: {
    product: Object,
  },
};
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
