<template>
  <div class="tab-container">
    <v-tabs color="pink lighten-3" right>
      <v-tab>シラバス</v-tab>
      <v-tab>レビュー</v-tab>
      <v-tab>過去問</v-tab>

      <v-tab-item class="tab">
        <v-row>
          <v-col>教授名</v-col>
          <v-col>丸先生</v-col>
        </v-row>
      </v-tab-item>

      <v-tab-item class="tab">
        <review />
      </v-tab-item>

      <v-tab-item class="tab">
        <old-question />
      </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
import OldQuestion from '~/components/oldQuestion'

export default {
  name: 'Result',
  components: { OldQuestion },
}
</script>

<style lang="scss" scoped>
.tab-container {
  height: 500px;
  width: 800px;
  backdrop-filter: blur(2px);
  background-color: rgba(255, 255, 255, 0.8);
}

.tab {
  padding: 20px;
}
</style>
<style>
.v-tabs-items {
  background-color: rgba(255, 255, 255, 0) !important;
}
</style>
