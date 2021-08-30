<template>
  <v-data-table :headers="headers" :items="desserts" class="table">
    <template #[`item.oldq`]="{ item }">
      <v-simple-checkbox v-model="item.oldq" disabled />
    </template>
    <template #[`item.review`]="{ item }">
      <v-rating
        v-model="item.review"
        half-increments
        background-color="orange lighten-3"
        color="orange"
        small
        style="pointer-events: none"
      />
    </template>
  </v-data-table>
</template>

<script>
export default {
  name: 'Index',
  data() {
    return {
      desserts: [
        {
          name: 'Frozen Yogurt',
          review: 4.5,
          day: 6.0,
          period: 24,
          oldq: true,
        },
        {
          name: 'Ice cream sandwich',
          review: 2,
          day: 9.0,
          period: 37,
          oldq: false,
        },
        {
          name: 'Eclair',
          review: 2,
          day: 16.0,
          period: 23,
          oldq: false,
        },
        {
          name: 'Jelly bean',
          review: 3,
          day: 0.0,
          period: 94,
          oldq: true,
        },
        {
          name: 'Lollipop',
          review: 3,
          day: 0.2,
          period: 98,
          oldq: true,
        },
        {
          name: 'KitKat',
          review: 5,
          day: 26.0,
          period: 65,
          oldq: false,
        },
      ],
      headers: [
        {
          text: '授業名',
          align: 'start',
          value: 'name',
        },
        { text: 'レビュー', value: 'review' },
        { text: '過去問', value: 'oldq' },
        { text: '曜日', value: 'day' },
        { text: '時限', value: 'period' },
      ],
    }
  },
}
</script>

<style lang="scss" scoped>
.table {
  backdrop-filter: blur(2px);
  background-color: rgba(255, 255, 255, 0.8);
}
</style>
<style>
.v-data-table-header {
  backdrop-filter: blur(2px);
  background-color: rgba(248, 185, 185, 0.4) !important;
}
</style>
