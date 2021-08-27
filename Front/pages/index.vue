<template>
  <div>
    <filter-menu v-if="showFilter" @close-filter="toggleFilter" />
    <search-button v-else @filter-open="toggleFilter" />
  </div>
</template>

<script>
import SearchButton from '~/components/searchButton'
import FilterMenu from '~/components/filterMenu/filterMenu'

export default {
  components: { FilterMenu, SearchButton },
  data() {
    return {
      showFilter: false,
    }
  },
  methods: {
    toggleFilter() {
      this.showFilter = !this.showFilter
    },
  },
}
</script>

<style></style>
