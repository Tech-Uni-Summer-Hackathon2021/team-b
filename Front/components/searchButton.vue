<template>
  <div>
    <v-text-field
      rounded
      solo
      label="Search"
      append-icon="mdi-magnify"
      @click:append="clickAction"
    ></v-text-field>
  </div>
</template>

<script>
export default {
  name: 'SearchButton',
  methods: {
    clickAction() {
      alert('ha ha pl ya ml')
    },
  },
}
</script>

<style scoped></style>
