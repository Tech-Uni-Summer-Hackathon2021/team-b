<template>
  <v-row align="center">
    <v-col cols="20">
      <v-select
        v-model="current"
        :items="selectedList"
        :label="label"
        :prepend-inner-icon="icon"
        dense
        menu-props="auto"
        solo
      />
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'FilterMenuItem',
  props: {
    label: String,
    icon: String,
    selectedList: Array,
  },
  data() {
    return { first: '', current: '' }
  },
  watch: {
    current() {
      this.$emit('value-select', [this.first, this.current])
    },
  },
  mounted() {
    this.first = this.label
  },
}
</script>

<style scoped></style>
