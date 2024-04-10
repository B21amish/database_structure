from enum import Enum


class UserAccountStatusEnum(Enum):
    ACTIVE = "active"
    DELETED = "deleted"


class AuthenticationTypeEnum(Enum):
    USERNAME = "username"


class UserLogEvent(Enum):
    CREATED = "created"
    DELETED = "deleted"
