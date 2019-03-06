import os
from src.domain.user import User

# path
PATH_TO_XML_FILE = os.path.abspath(os.path.dirname(__file__)) + '\\data\\'

# user credentials
USER_BY_DEFAULT = User('automation@keepitqa.com', 'E#*b2wGIbFHz')
USER_WITH_WRONG_LOGIN = User('some@wrong.login', 'E#*b2wGIbFHz')

# url
BASIC_URL = 'https://ws-test.keepit.com/users/zhc4v6-5ev7di-9hhhlm'

# response methods
GET = 'get'

# response statuses
SUCCESS = 200
UNAUTHORIZED = 401

# response messages
UNAUTHORIZED_MSG = 'Anonymous access denied - suggest authentication.'
WRONG_CREDENTIALS_ERROR_MSG = 'User authentication error: Username or password is incorrect.'

