from extensions import db
from datetime import datetime

class HairAssessment(db.Model):
    __tablename__ = "hair_assessments"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    hair_type = db.Column(db.String(50), nullable=False)
    concerns = db.Column(db.String(255), nullable=False)

    hair_score = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)