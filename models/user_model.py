from flask_login import UserMixin
from extensions import db
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    skin_assessments = db.relationship(
        "SkinAssessment",
        backref="user",
        cascade="all, delete",
        passive_deletes=True
    )

    hair_assessments = db.relationship(
        "HairAssessment",
        backref="user",
        cascade="all, delete",
        passive_deletes=True
    )