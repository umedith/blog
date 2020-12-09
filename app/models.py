from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Quote:
    '''
    Quote class to define quote Objects
    '''

    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self.quote = quote
        



class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    blog = db.relationship('Blog',backref = 'user',lazy = "dynamic")
    
    
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password) 
       
    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    '''
    Pitch class to define Pitch Objects
    '''
    __tablename__ = 'blog'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    content =  db.Column(db.String(1000))
    date = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
   
        

    def save_blog(self):
        '''
        Function that saves pitches
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_blogs(cls):
        '''
        Function that queries the databse and returns all the pitches
        '''
        return Blog.query.all()

    @classmethod
    def delete_blog(cls,id):
        '''
        '''
        db.session.delete()

   



# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User',backref = 'role',lazy="dynamic")
#     def __repr__(self):
#         return f'User {self.name}'


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
   
    


    def save_comments(self):
        db.session.add(self)
        db.session.commit()
        

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id).all()
        return comments


    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()


class Subscribe(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50))