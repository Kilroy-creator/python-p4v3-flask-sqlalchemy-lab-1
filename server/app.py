from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///earthquakes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# =====================
# Model
# =====================
class Earthquake(db.Model):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String)
    magnitude = db.Column(db.Float)
    year = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "magnitude": self.magnitude,
            "location": self.location,
            "year": self.year
        }


# =====================
# Routes
# =====================
@app.route("/")
def index():
    return "<h1>Earthquakes API</h1>"


@app.route("/earthquakes/<int:id>")
def get_earthquake(id):
    quake = Earthquake.query.get(id)
    if quake:
        return jsonify(quake.to_dict()), 200

    return jsonify({
        "message": f"Earthquake {id} not found."
    }), 404


@app.route("/earthquakes/magnitude/<float:mag>")
def earthquakes_by_magnitude(mag):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= mag).all()

    return jsonify({
        "count": len(quakes),
        "quakes": [q.to_dict() for q in quakes]
    })


# =====================
# DB Setup
# =====================
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)