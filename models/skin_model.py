from extensions import db
from datetime import datetime

class SkinAssessment(db.Model):
    __tablename__ = "skin_assessments"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    age = db.Column(db.Integer, nullable=False)
    skin_type = db.Column(db.String(50), nullable=False)
    skin_tone = db.Column(db.String(50), nullable=False)
    concerns = db.Column(db.String(255), nullable=False)

    health_score = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)