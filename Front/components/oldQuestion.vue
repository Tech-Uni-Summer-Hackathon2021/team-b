<template>
  <div class="tab-item-wrapper">
    <v-row v-if="editMode" class="flex-column" justify="center">
      <p class="text-center">ファイルをアップロードする</p>

      <v-file-input
        v-model="files"
        color="deep-purple accent-4"
        counter
        label="File input"
        multiple
        placeholder="Select your files"
        prepend-icon="mdi-paperclip"
        outlined
        :show-size="1000"
      >
        <template #selection="{ index, text }">
          <v-chip
            v-if="index < 2"
            color="deep-purple accent-4"
            dark
            label
            small
          >
            {{ text }}
          </v-chip>

          <span
            v-else-if="index === 2"
            class="text-overline grey--text text--darken-3 mx-2"
          >
            +{{ files.length - 2 }} File(s)
          </span>
        </template>
      </v-file-input>
      <v-row justify="center">
        <v-btn depressed width="10px" align="center" @click="submit">
          <v-icon>mdi-send</v-icon>
        </v-btn>
      </v-row>
    </v-row>
    <v-row v-else>
      <div v-for="(item, index) in temp" :key="index">
        <img :src="item.url" />
      </div>
    </v-row>
    <v-btn fab light class="tab-item-wrapper__button" @click="toggleMode">
      <v-icon v-if="!editMode">mdi-plus</v-icon>
      <v-icon v-else>mdi-close</v-icon>
    </v-btn>
  </div>
</template>

<script>
import firebase from 'firebase'
import { db } from '~/plugins/firebase'
export default {
  name: 'OldQuestion',
  props: {
    id: String,
  },
  data() {
    return {
      editMode: false,
      files: [],
      temp: [],
    }
  },
  mounted() {
    this.readSample()
  },
  methods: {
    async readSample() {
      const docRef = db.collection(
        `courses/campus/sanndacampus/${this.id}/oldq`
      )
      // Read collection
      await docRef.get().then((snapshot) => {
        const docs = snapshot.docs
        this.temp.length = 0
        for (const doc of docs) {
          this.temp.push(doc.data())
        }
      })
    },
    toggleMode() {
      this.editMode = !this.editMode
    },
    submit() {
      const dbReviews = db.collection(
        `courses/campus/sanndacampus/${this.id}/oldq`
      )
      this.files.forEach((imageData) => {
        const storageRef = firebase
          .storage()
          .ref(`${imageData.name}`)
          .put(imageData)
        storageRef.on(
          `state_changed`,
          (snapshot) => {
            this.uploadValue =
              (snapshot.bytesTransferred / snapshot.totalBytes) * 100
          },
          (error) => {
            console.log(error.message)
          },
          () => {
            storageRef.snapshot.ref.getDownloadURL().then((url) => {
              dbReviews
                .add({
                  url,
                })
                .then(this.readSample)
              console.log(this.id)
            })
          }
        )
      })

      this.toggleMode()
    },
  },
}
</script>

<style lang="scss" scoped>
.tab-item-wrapper {
  /* vuetify sets the v-tabs__container height to 48px */
  height: 420px;

  &__button {
    position: absolute;
    bottom: 20px;
    right: 10px;
  }
}
</style>
