<template>
  <div class="col-lg-3 col-md-4 col-sm-6 mix oranges fresh-meat" style="">
    <div class="featured__item">
      <div
        class="featured__item__pic set-bg"
        :data-setbg="product.get_absolute_url"
        :style="{ 'background-image': 'url(' + product.get_thumbnail + ')' }"
      >
        <ul class="featured__item__pic__hover">
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
      <div class="featured__item__text">
        <h6>
          <a href="#">{{ product.name }}</a>
        </h6>
        <h5>Giá: {{ product.price }} VNĐ</h5>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductBox",
  props: {
    product: Object,
  }
};
</script>
