<template>
  <div>
    <filter-menu v-if="showFilter" @close-filter="toggleFilter" />
    <class v-else-if="search" :search="search" />
    <search-button v-else @filter-open="toggleFilter" @search="searchClass" />
  </div>
</template>

<script>
import SearchButton from '~/components/searchButton'
import FilterMenu from '~/components/filterMenu/filterMenu'
import Class from '~/components/class'

export default {
  components: { Class, FilterMenu, SearchButton },
  data() {
    return {
      showFilter: false,
      search: '',
    }
  },
  methods: {
    toggleFilter(val) {
      if (val) {
        this.search += val
      }
      this.showFilter = !this.showFilter
    },
    searchClass(value) {
      this.search = value
    },
  },
}
</script>

<style></style>
