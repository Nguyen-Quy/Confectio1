<template>
  <div class="col-lg-4 col-md-6 col-sm-6">
    <div class="product__item">
      <router-link :to="product.get_absolute_url" class="latest-product__item">
        <div class="product__item__pic set-bg">
          <img :src="product.get_thumbnail" />
        </div>
        <div class="product__item__text">
          <h6>
            <router-link :to="product.get_absolute_url">{{
              product.name
            }}</router-link>
          </h6>
          <h5>Giá: {{ product.price }} VNĐ</h5>
        </div>
      </router-link>
    </div>
  </div>
  <router-view />
  <router-view />
</template>

<script>
export default {
  name: "AllProduct",
  props: {
    product: Object,
  },
};
</script>
