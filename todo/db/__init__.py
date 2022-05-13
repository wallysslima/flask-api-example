from todo import config
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import DateTime
from werkzeug import security

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(config.TODO_DATABASE_ADDRESS)
session = scoped_session(sessionmaker(autocommit=False, bind=engine))
Base = declarative_base()
Base.query = session.query_property()


def init():
    Base.metadata.create_all(bind=engine)


def teardown():
    session.remove()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = security.generate_password_hash(
            password + config.TODO_PASSWORD_SALT
        )

    def check_password(self, password):
        salted_password = password + config.TODO_PASSWORD_SALT
        return security.check_password_hash(self.password, salted_password)

    @classmethod
    def by_username(cls, username):
        return cls.query.filter_by(username=username).first()


class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="logs")
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    response_data = Column(Text, nullable=False)
    response_status_code = Column(Integer, nullable=False)

    @classmethod
    def add(cls, user_id, response_data, response_status_code):
        log = cls(
            user_id=user_id,
            response_data=str(response_data),
            response_status_code=response_status_code,
        )
        session.add(log)
        session.commit()
