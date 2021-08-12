<template>
  <div>
    <v-container>
      <v-card width="400px" class="mx-auto mt-5">
        <v-card-title style="text-align: center">
          <v-layout class="column justify-center align-center">
            <h1 class="display-1">新規登録</h1>
          </v-layout>
        </v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field
              v-model="usermail"
              prepend-icon="mdi-email"
              label="e-mail"
              :rules="[rules.required, rules.email]"
            />
            <v-text-field
              v-model="password"
              label="パスワード"
              @click:append="showPassword = !showPassword"
            />
            <v-text-field
              v-model="againpassword"
              label="パスワード（確認用）"
              @click:append="showPassword = !showPassword"
            />
            <v-col cols="12" class="text-center">
              <p>または</p>
            </v-col>
          </v-form>
        </v-card-text>
        <v-col cols="12" class="text-center">
          <v-btn class="max-width" @click="signup(onEmail)"> 登録</v-btn>
          <v-col cols="12" class="text-center">
            <p font-size="10px">すでにアカウントをお持ちですか？</p>
            <v-btn @click="onLogin"> ログインはこちら</v-btn>
          </v-col>
        </v-col>
      </v-card>
    </v-container>
  </div>
</template>
<script>
import firebase from '~/plugins/firebase'
export default {
  name: 'Signup',
  components: {},
  data: () => ({
    showPassword: false,
    usermail: '',
    password: '',
    againpassword: '',
    starturl: '',
    rules: {
      required: (value) => !!value || '必須項目.',
      counter: (value) => value.length <= 20 || 'Max 20 characters',
      email: (value) => {
        const pattern =
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        return pattern.test(value) || '不正なメール形式です'
      },
    },
  }),
  mounted() {
    console.log(process.env.FIREBASE_API_KEY)
    this.starturl = this.$route.query.url
  },
  methods: {
    checkPassword() {
      return this.password === this.againpassword
    },
    async onEmail() {
      if (this.checkPassword()) {
        await firebase
          .auth()
          .createUserWithEmailAndPassword(this.usermail, this.password)
      } else {
        throw new Error('パスワードが一致しません')
      }
    },
    async signup(func) {
      this.$nuxt.$loading.start()
      try {
        await func()
        this.$router.push('/')
      } catch (error) {
        console.log(error)
      }
      this.$nuxt.$loading.finish()
    },
    onLogin(login) {
      this.$router.push(`/login`)
    },
  },
}
</script>
