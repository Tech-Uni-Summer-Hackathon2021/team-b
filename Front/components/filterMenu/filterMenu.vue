<template>
  <v-container fluid>
    <filter-menu-item
      v-for="item in filterItems"
      :key="item.label"
      :label="item.label"
      :icon="item.icon"
      :items="item.item"
    />
    <v-row justify="center">
      <v-btn fab color="grey lighten-5" @click="closeTab">
        <v-icon color="grey darken-2">mdi-close</v-icon>
      </v-btn>
    </v-row>
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
          item: ['上ヶ原', 'sanda'],
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
  methods: {
    closeTab() {
      this.$emit('close-filter')
    },
  },
}
</script>

<style scoped></style>
