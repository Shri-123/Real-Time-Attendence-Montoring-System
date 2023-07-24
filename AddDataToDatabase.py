import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://real-time-face-detection-fd855-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Shrihari Mangle",
            "major": "Computer",
            "starting_year":2020,
            "total_attendence":7,
            "standing":"G",
            "year":4,
            "last_attendence_time":"2023-07-22 00:54:34"

        },

    "852741":
        {
            "name": "Emily Blunt",
            "major": "Economics",
            "starting_year":2018,
            "total_attendence":12,
            "standing":"B",
            "year":2,
            "last_attendence_time":"2023-07-22 00:54:34"

        },

    "963852":
        {
            "name": "Elon Musk",
            "major": "AI",
            "starting_year":2014,
            "total_attendence":13,
            "standing":"E",
            "year":3,
            "last_attendence_time":"2023-07-22 00:54:34"

        },
}

for key, value in data.items():
    ref.child(key).set(value)