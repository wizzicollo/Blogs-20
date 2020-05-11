from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from . import login_manager
from . import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    full_name = db.Column(db.String)
    email = db.Column(db.String)
    pass_word = db.Column(db.String)
    blogg = db.relationship('Blogs', backref = 'user', lazy = 'dynamic')
    @property
    def password(self):
        raise  AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_word = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_word, password)

    def __repr__(self):
        return f'User {self.username}'

    
class Blogs(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key = True)
    blog_title = db.Column(db.String)
    blog_content = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete()

    @classmethod
    def get_blog(cls, id):
        blog = Blogs.query.filter_by(blog_id=id).all()
        return blog


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    comment = db.Column(db.Text(),nullable = False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.delete()

    @classmethod
    def get_comments(cls,user_id):
        comments = Comment.query.filter_by(user_id=user_id).all()

        return comments


class Quotes:
    '''
    class that returns the quotes objects
    '''

    def __init__(self,author,id,quote):
        self.id = id
        self.author = author
        self.quote = quote

class Subscriber(db.Model):
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'