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
      <v-col>教授名</v-col>
      <v-col>丸先生</v-col>
    </v-row>
    <v-btn fab light class="tab-item-wrapper__button" @click="toggleMode">
      <v-icon v-if="!editMode">mdi-plus</v-icon>
      <v-icon v-else>mdi-close</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  name: 'OldQuestion',
  data() {
    return {
      editMode: false,
      files: [],
    }
  },

  methods: {
    toggleMode() {
      this.editMode = !this.editMode
    },
    submit() {},
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
