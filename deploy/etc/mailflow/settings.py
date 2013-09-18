DEBUG = False

SQLALCHEMY_DATABASE_URI = "postgres://mailflow.user:1234@localhost/mailflow"
SQLALCHEMY_POOL_SIZE = 20
SQLALCHEMY_POOL_TIMEOUT = 30
SQLALCHEMY_POOL_RECYCLE = 5 * 3600
SQLALCHEMY_MAX_OVERFLOW = 20

SECRET_KEY = 'Chi6riup1gaetiengaShoh=Wey1pohph0ieDaes7eeph'

INBOX_LOGIN_LENGTH = 16
INBOX_PASSWORD_LENGTH = 16
INBOX_PAGE_SIZE = 50

INBOX_HOST = 'mailflow.openpz.org'
INBOX_PORT = 25

RAW_EMAIL_FOLDER = "/var/tmp"

RABBITMQ_URI = 'amqp://mailflow:youneverguess@localhost//mail'
RABBITMQ_EXCHANGE_NAME = 'mail'
RABBITMQ_MAIL_QUEUE_PREFIX = 'newmail'

WTF_CSRF_TIME_LIMIT = 21600

CACHE_TYPE = 'memcached'
CACHE_DEFAULT_TIMEOUT = 300

CACHE_MEMCACHED_SERVERS = ('localhost:11211', )