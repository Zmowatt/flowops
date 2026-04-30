from flask import Flask, request, session
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, bcrypt, User, Request, Update

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flowops.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "dev-secret-key"

CORS(app, supports_credentials=True)

db.init_app(app)
bcrypt.init_app(app)

migrate = Migrate(app, db)


@app.get("/")
def home():
    return {"message": "FlowOps API is running"}



@app.post("/signup")
def signup():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    role = data.get("role", "Requester")
    password = data.get("password")

    if not name or not email or not password:
        return {"error": "Name, email, and password are required"}, 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return {"error": "Email already exists"}, 400

    new_user = User(
        name=name,
        email=email,
        role=role
    )

    new_user.password_hash = password

    db.session.add(new_user)
    db.session.commit()

    session["user_id"] = new_user.id

    return new_user.to_dict(), 201


@app.post("/login")
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Email and password are required"}, 400

    user = User.query.filter_by(email=email).first()

    if user and user.authenticate(password):
        session["user_id"] = user.id
        return user.to_dict(), 200

    return {"error": "Invalid email or password"}, 401


@app.get("/check_session")
def check_session():
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    user = User.query.get(user_id)

    if not user:
        return {"error": "User not found"}, 404

    return user.to_dict(), 200


@app.delete("/logout")
def logout():
    session.pop("user_id", None)
    return {}, 204



if __name__ == "__main__":
    app.run(port=5555, debug=True)