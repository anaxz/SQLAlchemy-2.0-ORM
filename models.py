from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,Text
from typing import List

## Import notes:
# DeclarativeBase allows to create a base class that inherits from all database model classes
# Mapped allows you to define the types of columns in a table
# mapped_column = define more attributes e.g. primary key
# Text = text / basic strings ?
# from typing import List -> inbuilts; don't need to install again

class Base(DeclarativeBase):
    pass


# User inherit from base class
class User(Base):
    # '__tablename__' is a table object
    # In ver 2.0 you map the type
    
    __tablename__ = 'users' # name of the table

    # Mapped[type of var]
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(nullable=False)

    # did not add mapped_column as to leave it optional
    email_address:Mapped[str] 

    # access list of Comment objects by a specific user
    # List("class name")
    # back_populates refers to what you should use to access users on specific comments so comment.user aka 'user'
    comments:Mapped[List["Comment"]] = relationship(back_populates='user')

    # represent table as a string when printed
    def __repr__(self) -> str:
        return f"<User username={self.username}>"


class Comment(Base):
    __tablename__ = 'comments'
    id:Mapped[int] = mapped_column(primary_key=True)

    # mapped_column -> use this for ForeignKey
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'),nullable=False)

    text:Mapped[str] = mapped_column(Text,nullable=False)

    # each comment belongs to 1 user so not a list
    # 1 to many relationship
    # comments points to User table's comments column
    user:Mapped["User"] =relationship(back_populates='comments')

    def __repr__(self):
        return f"<Comment text={self.text} by {self.user.username}>"