<template>
  <div style="display: flex; flex-direction: row; align-items: center">
    <v-text-field
      rounded
      solo
      label="Search"
      append-icon="mdi-filter"
      @click:append="clickAction"
      @keyup.enter="clickAction"
    />
    <v-btn
      fab
      style="margin-top: -30px; margin-left: 30px"
      color="grey lighten-5"
    >
      <v-icon color="grey darken-2">mdi-magnify</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  name: 'SearchButton',
  methods: {
    clickAction() {
      this.$emit('filter-open')
    },
  },
}
</script>

<style scoped></style>
