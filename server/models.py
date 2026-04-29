from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    requests = db.relationship("Request", back_populates="user", cascade="all, delete-orphan")
    updates = db.relationship("Update", back_populates="user", cascade="all, delete-orphan")

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes may not be viewed")
    
    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role
        }

class Request(db.Model):
    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String, nullable=False)
    address - db.Column(db.String, nullable=False)
    parts_requested = db.Column(db.String, nullable=False)
    date_needed = db.Column(db.String, nullable=False)
    priority = db.Column(db.String, default="Normal")
    status = db.Column(db.String, default="Requested")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User", back_populates="requests")
    updates = db.relationship("Update", back_populates="request", cascade="all delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "job_name": self.job_name,
            "address": self.address,
            "parts_requested": self.parts_requested,
            "date_needed": self.date_needed,
            "priority": self.priority,
            "status": self.status,
            "user_id": self.user_id
        }

class Update(db.Model):
    __tablename__ = "updates"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    request_id = db.Column(db.Integer, db.ForeignKey("requests.id"))

    user = db.relationship("User", back_populates="updates")
    request - db.relationship("Request", back_populates="updates")

    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "user_id": self.user_id,
            "request_id": self.request_id
        }