<template>
  <v-container fluid>
    <filter-menu-item
      v-for="item in filteredItems"
      :key="item.label"
      :label="item.label"
      :icon="item.icon"
      :selected-list="item.selectedList"
      @value-select="onSelect"
    />
    <v-row justify="center">
      <v-btn fab color="grey lighten-5" @click="closeTab">
        <v-icon color="grey darken-2">mdi-close</v-icon>
      </v-btn>
    </v-row>
  </v-container>
</template>

<script>
import algoliasearch from 'algoliasearch/lite'
import FilterMenuItem from '~/components/filterMenu/filterMenuItem'

export default {
  name: 'FilterMenu',
  components: { FilterMenuItem },
  data() {
    return {
      filterString: '',
      filteredItems: [],
      labels: [
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
  mounted() {
    const client = algoliasearch(
      '8HJGZZGNDD',
      '632e9c93339b56eea4ff6ee4b0af9ada'
    )
    const index = client.initIndex('syllabus')
    this.labels.forEach((item) => {
      index.searchForFacetValues(item.label, '').then(({ facetHits }) => {
        const temp = facetHits.map((item) => item.value)
        this.filteredItems.push({
          label: item.label,
          icon: item.icon,
          selectedList: temp,
          current: '',
        })
      })
    })
  },
  methods: {
    closeTab() {
      this.$emit('close-filter', this.getSearchString())
    },
    onSelect(val) {
      this.filteredItems.forEach((item) => {
        if (item.label === val[0]) {
          item.current = val[1]
        }
      })
    },
    getSearchString() {
      let temp = ''
      this.filteredItems.forEach((item) => {
        temp += ' ' + item.current
      })
      return temp
    },
  },
}
</script>

<style scoped></style>
