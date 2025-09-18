from flask import Flask,render_template,jsonify

app = Flask(__name__)


leaderboard_data = [
    {"rank": 1,
     "name": "Arjun Nair",
     "points": 1500,
     "tasks": 52,
     "region": "Alappuzha"
     },
    {"rank": 2,
     "name": "Latha Menon",
     "points": 1450,
     "tasks": 48,
     "region": "Munnar"
     },
    {"rank": 3,
     "name": "Balakrishnan K.",
     "points": 1280,
     "tasks": 45,
     "region": "Wayanad"
     },
    {"rank": 4,
     "name": "Meera Joseph",
     "points": 1100,
     "tasks": 39,
     "region": "Kumarakom"
     },
    {"rank": 5,
     "name": "Karthik Pillai",
     "points": 950,
     "tasks": 31,
     "region": "Kovalam"
     },
    {"rank": 6,
     "name": "Sreelakshmi V.",
     "points": 880,
     "tasks": 29,
     "region": "Varkala"
     },
    {"rank": 7,
     "name": "Sudheesh Kumar",
     "points": 700,
     "tasks": 25,
     "region": "Thekkady"
     },
    {"rank": 8,
     "name": "Anjali S.",
     "points": 620,
     "tasks": 22,
     "region": "Poovar"
     },
    {"rank": 9,
     "name": "Vinod Das",
     "points": 500,
     "tasks": 19,
     "region": "Bekal"
     },
    {"rank": 10,
     "name": "Priya Mohan",
     "points": 450,
     "tasks": 18,
     "region": "Athirappilly"
    }
]

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/hindi")
def hindi():
    return render_template('indexh.html')

@app.route("/leaderboard")
def leaderboard():
    return render_template('leaderboard.html',data=leaderboard_data)


if __name__=="__main__":
    app.run(host='0.0.0.0',debug = True)