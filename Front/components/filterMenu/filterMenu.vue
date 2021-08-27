<template>
  <v-container fluid>
    <filter-menu-item
      v-for="item in filterItems"
      :key="item.label"
      :label="item.label"
      :icon="item.icon"
    />
  </v-container>
</template>

<script>
import FilterMenuItem from '~/components/filterMenu/filterMenuItem'

export default {
  name: 'FilterMenu',
  components: { FilterMenuItem },
  data() {
    return {
      filterItems: [
        {
          label: 'キャンパス',
          icon: 'mdi-office-building',
        },
        {
          label: '学部',
          icon: 'mdi-book-education-outline',
        },
        {
          label: '学期',
          icon: 'mdi-book-clock-outline',
        },
        {
          label: '曜日',
          icon: 'mdi-calendar-clock',
        },
        {
          label: '時限',
          icon: 'mdi-alarm',
        },
      ],
    }
  },
}
</script>

<style scoped></style>
