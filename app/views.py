from flask import render_template, flash
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, UserMixin, current_user, login_required
from app import app, db, models
from .forms import FilterForm, LoginForm, NewPostForm
import json

bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
   return models.User.query.get(user_id)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
   posts = models.Post.query.all()
   form = FilterForm()
   if form.validate_on_submit():
      posts = db.session.query(models.Post).join(models.Post.tags).filter_by(tag_name=form.tag.data).all()
   return render_template('dashboard.html', title='Dashboard', posts=posts, form=form)

@app.route('/like-post/<int:post_id>', methods=['POST'])
def like_post(post_id):
   post = models.Post.query.get(post_id)
   for liked_post in current_user.liked_posts:
      if liked_post == post_id:
         return json.dumps({'status': 'ERROR','likes': post.likes,}) #if user has already liked post
   post.likes += 1
   db.session.commit()
   current_user.liked_posts.append(post_id)
   return json.dumps({'status': 'OK', 'likes': post.likes,})

@app.route('/', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   #If logged in successfully
   if form.validate_on_submit():
      flash('Login validated, checking...')
      users = models.User.query.all()
      logged_in = False
      for user in users:
          if user.username == form.username.data and bcrypt.check_password_hash(user.password,form.password.data):
             logged_in = True
             login_user(user)
             flash('Login successful!')
             break
   return render_template('login.html', title='Login', form=form)

@app.route('/new-post', methods=['GET', 'POST'])
@login_required
def new_post():
   #Need user to be logged in
   form = NewPostForm()
   if form.validate_on_submit():
      post = models.Post(title=form.title.data, body=form.body.data, likes=0)
      post.user = current_user
      tags = []
      for tag in form.tags.data.split(","):
         tags.append(tag.strip())
      for tag in tags:
         tag = models.Tag(tag_name=tag)
         db.session.add(tag)
         post.tags.append(tag)
      db.session.add(post)
      db.session.commit()
      flash('Post successfully uploaded!')
   return render_template('new_post.html', title='New Post', form=form)


