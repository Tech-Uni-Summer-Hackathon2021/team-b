export default class Environment {
  static get FIREBASE_API_KEY() {
    return 'AIzaSyBGEECDX11Pc3I1ivGgXXEAtPmjL6ot26E'
  }

  static get FIREBASE_AUTH_DOMAIN() {
    return process.env.FIREBASE_AUTH_DOMAIN
  }

  static get FIREBASE_PROJECT_ID() {
    return process.env.FIREBASE_PROJECT_ID
  }

  static get FIREBASE_STORAGE_BUCKET() {
    return 'team-b-26329.appspot.com'
  }

  static get FIREBASE_MESSAGING_SENDER_ID() {
    return process.env.FIREBASE_MESSAGING_SENDER_ID
  }

  static get FIREBASE_APP_ID() {
    return process.env.FIREBASE_APP_ID
  }

  static get FIREBASE_MEASUREMENT_ID() {
    return process.env.FIREBASE_MEASUREMENT_ID
  }
}
