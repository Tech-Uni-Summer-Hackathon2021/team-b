<template>
  <v-app>
    <v-app-bar fixed app>
      <v-btn icon @click="goHome">
        <v-icon>mdi-home</v-icon>
      </v-btn>

      <v-toolbar-title v-text="title" />
    </v-app-bar>
    <v-main>
      <div class="content">
        <nuxt />
      </div>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      title: 'App name',
    }
  },
  methods: {
    goHome() {
      this.$router.push('/')
    },
  },
}
</script>
<style>
.content {
  background: url('~assets/background.png') no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100%;
}
</style>
