from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flowops.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "dev-secret-key"

CORS(app)

db.init_app(app)
bcrypt.init_app(app)

migrate = Migrate(app, db)


@app.get("/")
def home():
    return {"message": "FlowOps API is running"}


if __name__ == "__main__":
    app.run(port=5555, debug=True)