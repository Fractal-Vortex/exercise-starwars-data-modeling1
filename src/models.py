from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    
    posts = relationship("Posts", back_populates="user")
    comments = relationship("Comments", back_populates="author")
    followers_from = relationship("Followers", back_populates="user_from")
    followers_to = relationship("Followers", back_populates="user_to")


class Posts(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="posts")
    comments = relationship("Comments", back_populates="post")
    media = relationship("Media", back_populates="post")


class Comments(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))

    author = relationship("User", back_populates="comments")
    post = relationship("Posts", back_populates="comments")


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum('ACTIVE', 'INACTIVE', 'BANNED', name='user_status'), nullable=False)
    url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))

    post = relationship("Posts", back_populates="media")


class Followers(Base):
    __tablename__ = 'followers'
    user_from_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    user_to_id = Column(Integer, ForeignKey("user.id"), primary_key=True)

    user_from = relationship("User", back_populates="followers_from")
    user_to = relationship("User", back_populates="followers_to")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
