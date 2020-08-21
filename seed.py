from models import User, Post, db
from app import app

db.drop_all()
db.create_all()


User.query.delete()

user1 = User(first_name='Genna',
             last_name='K')

user2 = User(first_name='Bean',
             last_name='K')

db.session.add(user1)
db.session.add(user2)
db.session.commit()