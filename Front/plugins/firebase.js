import firebase from 'firebase'

if (!firebase.apps.length) {
  firebase.initializeApp({
    apiKey: 'AIzaSyAObcU-JPuQiec7EnCQPKRNHx7Rqjp_awY',
    authDomain: 'test-f601a.firebaseapp.com',
    projectId: 'test-f601a',
    storageBucket: 'test-f601a.appspot.com',
    messagingSenderId: '767385971484',
    appId: '1:767385971484:web:3cbd44a269f95d8990a8d9',
    measurementId: 'G-8XY8FM1TM6',
  })
}
export const db = firebase.firestore()
export default firebase
