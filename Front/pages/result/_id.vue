<template>
  <div class="tab-container">
    <v-tabs color="pink lighten-3" right>
      <v-tab>シラバス</v-tab>
      <v-tab>レビュー</v-tab>
      <v-tab>過去問</v-tab>

      <v-tab-item class="tab">
        <v-row v-for="(value, name) in syllabus" :key="name">
          <v-col>{{ name }}</v-col>
          <v-col>{{ value }}</v-col>
        </v-row>
      </v-tab-item>

      <v-tab-item class="tab">
        <review :id="id" />
      </v-tab-item>

      <v-tab-item class="tab">
        <old-question :id="id" />
      </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
import OldQuestion from '~/components/oldQuestion'
import { db } from '~/plugins/firebase'

export default {
  name: 'Result',
  components: { OldQuestion },
  data() {
    return {
      syllabus: {},
      id: '',
    }
  },
  mounted() {
    this.readSample()
  },
  methods: {
    async readSample() {
      const docRef = db
        .collection('courses/campus/sanndacampus/')
        .where('id', '==', this.$route.query.id)

      // Read collection
      await docRef
        .get()
        .then((snapshot) => {
          const docs = snapshot.docs
          for (const doc of docs) {
            this.syllabus = doc.data()
            this.id = doc.id
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
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
  overflow: scroll;
}
</style>
<style>
.v-tabs-items {
  background-color: rgba(255, 255, 255, 0) !important;
}
</style>
