<template>
  <div class="page-success">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Cảm ơn quý khách</h1>

        <p>Đơn hàng của bạn sẽ được xử lý trong vòng 48 giờ.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Success",
  mounted() {
    document.title = "Thành công | Confectio";
  },
};
</script>
