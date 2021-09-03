<template>
  <div style="display: flex; flex-direction: row; align-items: center">
    <v-text-field
      v-model="search"
      placeholder="search class"
      rounded
      solo
      label="Search"
      append-icon="mdi-filter"
      @click:append="clickAction"
      @keyup.enter="searchClass"
    />
    <v-btn
      fab
      style="margin-top: -30px; margin-left: 30px"
      color="grey lighten-5"
      @click="searchClass"
    >
      <v-icon color="grey darken-2">mdi-magnify</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  name: 'SearchButton',
  data() {
    return {
      search: '',
      hits: [],
    }
  },
  methods: {
    clickAction() {
      this.$emit('filter-open')
    },
    searchClass() {
      this.$emit('search', this.search)
    },
  },
}
</script>
