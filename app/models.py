from app import db
from flask_login import UserMixin

PostTag = db.Table('PostTag',db.Model.metadata,
db.Column('post_id', db.Integer, db.ForeignKey('post.post_id')),
db.Column('tag_id', db.Integer, db.ForeignKey('tag.tag_id')))

class User(UserMixin, db.Model):
   user_id = db.Column(db.Integer, primary_key=True)
   id = user_id #id of current logged in user
   username = db.Column(db.String(500), index=True) 
   password = db.Column(db.String(500))
   posts = db.relationship('Post', backref='user', lazy='dynamic')
   liked_posts = [] #has post_id of liked posts

class Post(db.Model):
   post_id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(500), index=True)
   body = db.Column(db.String(500), index=True)
   likes = db.Column(db.Integer, default=0)
   user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
   tags = db.relationship('Tag', secondary=PostTag)

class Tag(db.Model):
   tag_id = db.Column(db.Integer, primary_key=True)
   tag_name = db.Column(db.String(500), index=True)
   posts = db.relationship('Post', secondary=PostTag, overlaps="tags")

