<template>
  <v-data-table
    :headers="headers"
    :items="hits"
    class="table"
    @click:row="handleClick"
  >
    <template #[`item.oldq`]="{ item }">
      <v-simple-checkbox v-model="item.oldq" disabled />
    </template>
    <template #[`item.review`]="{ item }">
      <v-rating
        v-model="item.review"
        half-increments
        background-color="orange lighten-3"
        color="orange"
        small
        style="pointer-events: none"
      />
    </template>
  </v-data-table>
</template>

<script>
import algoliasearch from 'algoliasearch/lite'

export default {
  name: 'Class',
  props: {
    search: String,
  },
  data() {
    return {
      hits: [],
      headers: [
        {
          text: '授業名',
          align: 'start',
          value: '科目',
        },
        { text: '曜日', value: '曜日' },
        { text: '時限', value: '時限' },
      ],
    }
  },
  mounted() {
    const client = algoliasearch(
      '8HJGZZGNDD',
      '632e9c93339b56eea4ff6ee4b0af9ada'
    )
    const index = client.initIndex('syllabus')
    index.searchForFacetValues('学部', '').then(({ facetHits }) => {
      console.log(facetHits)
    })
    index
      .search(this.search, {
        attributesToRetrieve: ['id', '科目', '曜日', '時限'],
      })
      .then(({ hits }) => {
        this.hits = hits
      })
  },
  methods: {
    handleClick(item) {
      this.$router.push(`/result?id=${item.id}`)
    },
  },
}
</script>

<style lang="scss" scoped>
.table {
  backdrop-filter: blur(2px);
  background-color: rgba(255, 255, 255, 0.8);
  //height: 500px;
  width: 800px;
}
</style>
<style>
.v-data-table-header {
  backdrop-filter: blur(2px);
  background-color: rgba(248, 185, 185, 0.4) !important;
}
</style>
