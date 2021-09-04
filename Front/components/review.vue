<template>
  <div class="tab-item-wrapper">
    <v-row v-if="editMode" class="flex-column">
      <div class="text-center">
        <span>あなたの評価</span>
        <v-rating
          v-model="writtenReview.rating"
          background-color="orange lighten-3"
          color="orange"
        ></v-rating>
        <v-textarea
          v-model="writtenReview.post"
          outlined
          type="text"
          name="input-7-4"
          label="コメント"
          value="コメント入ります"
        ></v-textarea>
        <v-btn depressed width="10px" color="light gray" @click="submit">
          <v-icon>mdi-send</v-icon>
        </v-btn>
      </div>
    </v-row>
    <v-row v-else>
      <div v-for="(item, index) in temp" :key="index">
        <v-card class="elevation-16 mx-auto" width="300">
          <v-card-text>
            {{ item.post }}

            <div class="text-center mt-12">
              <v-rating
                v-model="rating"
                color="yellow darken-3"
                background-color="grey darken-1"
                half-increments
                hover
                large
                value="{{item.rating}}"
              ></v-rating>
            </div>
          </v-card-text>
        </v-card>
      </div>
    </v-row>
    <v-btn fab light class="tab-item-wrapper__button" @click="toggleMode">
      <v-icon v-if="!editMode">mdi-pencil</v-icon>
      <v-icon v-else>mdi-close</v-icon>
    </v-btn>
  </div>
</template>

<script>
import { db } from '~/plugins/firebase'

export default {
  name: 'Review',
  props: {
    id: String,
  },
  data() {
    return {
      temp: [],
      writtenReview: {
        rating: '',
        post: '',
      },
      editMode: false,
    }
  },
  mounted() {
    this.readSample()
  },
  methods: {
    async readSample() {
      const docRef = db.collection(
        `courses/campus/sanndacampus/${this.id}/review`
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
    async submit() {
      const dbReviews = db.collection(
        `courses/campus/sanndacampus/${this.id}/review`
      )
      await dbReviews
        .add({
          rating: this.writtenReview.rating,
          post: this.writtenReview.post,
        })
        .then(this.readSample)
      this.editMode = !this.editMode
    },
  },
}
</script>

<style lang="scss" scoped>
.tab-item-wrapper {
  /* vuetify sets the v-tabs__container height to 48px */
  height: 420px;
  display: flex;
  flex-direction: column;

  &__button {
    position: absolute;
    bottom: 20px;
    right: 10px;
  }
}
</style>
