from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    DateTime,
    Enum,
    text,
    String,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

from lapa_database_structure.lapa.authentication.enums import (
    UserAccountStatusEnum,
    AuthenticationTypeEnum,
    UserLogEvent,
)

Base = declarative_base(metadata=MetaData(schema="authentication"))

data_to_insert = []


class User(Base):
    __tablename__ = "user"

    user_id = Column(
        UUID,
        primary_key=True,
        nullable=False,
        unique=True,
        default=text("gen_random_uuid()"),
    )
    user_account_status = Column(
        Enum(UserAccountStatusEnum),
        nullable=False,
        default=text(UserAccountStatusEnum.ACTIVE.value),
    )


class AuthenticationUsername(Base):
    __tablename__ = "authentication_username"

    authentication_username_id = Column(
        Integer, primary_key=True, nullable=False, unique=True, autoincrement=True
    )
    user_id = Column(
        UUID,
        ForeignKey(User.user_id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    authentication_username_username = Column(
        String,
        nullable=False,
        unique=True,
    )
    authentication_username_hashed_password = Column(String, nullable=False)
    authentication_username_password_salt = Column(String, nullable=False, unique=True)
    authentication_username_access_token = Column(String, nullable=False)
    authentication_username_refresh_token = Column(String, nullable=False)


class UserProfile(Base):
    __tablename__ = "user_profile"

    user_profile_id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True,
    )
    user_id = Column(
        UUID,
        ForeignKey(User.user_id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )


class UserAuthentication(Base):
    __tablename__ = "user_authentication"

    user_authentication_id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True,
    )
    user_id = Column(
        UUID,
        ForeignKey(User.user_id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    user_authentication_authentication_type = Column(
        Enum(AuthenticationTypeEnum),
        nullable=False,
        default=AuthenticationTypeEnum.USERNAME.value,
    )


class UserLog(Base):
    __tablename__ = "user_log"

    user_log_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(
        UUID,
        ForeignKey(User.user_id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    user_log_datetime = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    user_log_event = Column(Enum(UserLogEvent), nullable=False)
