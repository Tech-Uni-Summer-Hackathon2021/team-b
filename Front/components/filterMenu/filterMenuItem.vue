<template>
  <v-row align="center">
    <v-col cols="20">
      <v-select
        menu-props="auto"
        :label="label"
        :prepend-inner-icon="icon"
        :items="item"
        dense
        solo
      ></v-select>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'FilterMenuItem',
  props: {
    label: String,
    icon: String,
    item: String,
  },
}
</script>

<style scoped></style>
