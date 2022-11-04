<template>
  <div class="latest-product__slider owl-carousel">
    <div class="latest-prdouct__slider__item">
      <router-link :to="product.get_absolute_url" class="latest-product__item">
        <div class="latest-product__item__pic">
          <img :src="product.get_thumbnail" />
        </div>
        <div class="latest-product__item__text">
          <h6>{{ product.name }}</h6>
          <span>{{ product.price }} VNĐ</span>
        </div>
      </router-link>
    </div>
  </div>
  <router-view />
</template>

<script>
export default {
  name: "LastProduct",
  props: {
    product: Object,
  },
};
</script>
