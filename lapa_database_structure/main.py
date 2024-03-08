from enum import Enum


class DatabasesEnum(str, Enum):
    lapa = "lapa"
    testing = "testing"

class SchemaEnum(str, Enum):
    public = "public"
    file_storage = "file_storage"
    authentication = "authentication"

class TablesEnum(str, Enum):
    file = "file"
    user_validation_status = "user_validation_status"
    user_registration = "user_registration"
    hashing_algorithm = "hashing_algorithm"
    user = "user"

