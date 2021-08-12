<template>
  <div>
    <v-container>
      <v-card width="400px" class="mx-auto mt-5">
        <v-row>
          <v-col cols="12" class="text-center">
            <h1 class="display-1">ログイン</h1>
          </v-col>
          <v-col cols="12" class="text-center">
            <v-form style="padding: 10px">
              <v-text-field
                v-model="usermail"
                prepend-icon="mdi-account-circle"
                label="e-mail"
              />
              <v-text-field
                v-model="userpass"
                label="パスワード"
                @click:append="showPassword = !showPassword"
              />
            </v-form>
            <v-btn @click="login(onEmail)"> ログイン</v-btn>
          </v-col>
          <v-col cols="12" class="text-center">
            <p>または</p>
          </v-col>

          <v-col cols="12" class="text-center">
            <p text-align="center">すでにアカウントをお持ちですか？</p>
            <v-btn @click="onSignup"> 新規登録はこちら</v-btn>
          </v-col>
        </v-row>
      </v-card>
    </v-container>
  </div>
</template>
<script>
import firebase from '~/plugins/firebase'
export default {
  name: 'Login',
  components: {},
  data: () => ({
    showPassword: false,
    usermail: '',
    userpass: '',
    nexturl: '',
    localDatas: undefined,
  }),
  computed: {},
  mounted() {
    // this.nexturl = this.$route.query.url //後々に実装予定
  },
  methods: {
    async onEmail() {
      await firebase
        .auth()
        .signInWithEmailAndPassword(this.usermail, this.userpass)
    },
    async login(loginFunc) {
      try {
        this.$nuxt.$loading.start()
        await loginFunc()
        this.$nuxt.$loading.finish()
        this.$router.push('/')
      } catch (error) {}
      this.$nuxt.$loading.finish()
    },
    onSignup(signup) {
      this.$router.push(`/signup`)
    },
  },
}
</script>
