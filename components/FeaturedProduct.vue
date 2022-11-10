<template>
  <div class="col-lg-3 col-md-4 col-sm-6 mix oranges fresh-meat" style="">
    <div class="featured__item">
      <router-link :to="product.get_absolute_url" class="latest-product__item">
        <div
          class="featured__item__pic set-bg"
          :data-setbg="product.get_absolute_url"
          :style="{ 'background-image': 'url(' + product.get_thumbnail + ')' }"
        >
        </div>
        <div class="featured__item__text">
          <h6>
            <a href="#">{{ product.name }}</a>
          </h6>
          <h5>Giá: {{ product.price }} </h5>
        </div>
      </router-link>
    </div>
  </div>
  <router-view/>
</template>

<script>
export default {
  name: "FeaturedProduct",
  props: {
    product: Object,
  }
};
</script>
