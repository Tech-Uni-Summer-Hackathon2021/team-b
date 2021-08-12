<template>
  <div>
    <v-overlay :value="loading">
      <v-progress-circular />
    </v-overlay>
  </div>
</template>
<script>
export default {
  components: {},
  model: {},
  props: {},
  data() {
    return {
      loading: false,
      snackbar: false,
      snackbarText: '',
    }
  },
  mounted() {},
  methods: {
    start() {
      this.loading = true
    },
    finish() {
      this.loading = false
    },
    fail(error) {
      console.log(error)
    },
  },
}
</script>
