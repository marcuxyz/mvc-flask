from tests.app import db


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
