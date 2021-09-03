import algoliasearch from "algoliasearch";
import firebase from 'firebase'

if (!firebase.apps.length) {
    firebase.initializeApp({
        apiKey: 'AIzaSyBGEECDX11Pc3I1ivGgXXEAtPmjL6ot26E',
        authDomain: 'team-b-26329.firebaseapp.com',
        projectId: 'team-b-26329',
        storageBucket: 'team-b-26329.appspot.com',
        messagingSenderId: '703938629335',
        appId: '1:703938629335:web:3c941ceb676a2734e82a92',
        measurementId: 'G-8XY8FM1TM6',
    })
}
export const db = firebase.firestore()


// const client = algoliasearch("", "");
// const index = client.initIndex('syllabus');

exports.indexSyllabus = db.document('selenium2/sampustest/sanndacampus/{classId}').get().then((snap) => {
    console.log(snap.data())
})
