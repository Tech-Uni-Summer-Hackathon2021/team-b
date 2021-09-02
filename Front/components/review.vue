<template>
  <div class="tab-item-wrapper">
    <section>
      <p>{{ $route.params.id }}</p>
    </section>
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
    <v-row v-else> </v-row>
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
  data() {
    return {
      writtenReview: {
        rating: '',
        post: '',
      },
      editMode: false,
    }
  },
  mounted() {
    console.log(this.$route.params.slug)
  },
  methods: {
    toggleMode() {
      this.editMode = !this.editMode
    },
    submit() {
      const dbReviews = db.collection('reviews')
      dbReviews.add({
        rating: this.rating,
        post: this.post,
      })
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
