from .common import *

INSTALLED_APPS += ["debug_toolbar"]  # 끝에 추가

# 맨 앞에 추가 됨
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] + MIDDLEWARE

INTERNAL_IPS = [
    "127.0.0.1",
]
