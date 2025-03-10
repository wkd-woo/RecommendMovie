"""
Django settings for RecommendMovie project.

Generated by 'django-admin startproject' using Django 3.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

import os, environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accountapp',
    'articleapp',
    'profileapp',
    'analysisapp',
    'rmapp',
    'goapp',
    'bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RecommendMovie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'RecommendMovie.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASE_ROUTERS = ['RecommendMovie.dbrouter.MultiDBRouter']    # 다수의 DB를 사용하기 위한 DB 라우터.
DATABASE_APPS_MAPPING = { 'genome_data' : 'genome_db', 'rating_data' : 'rating_db'}

DATABASES = {
    'default': {  # 기본 db (user 정보 등)
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'genome_db': {  # genome-score db
        'ENGINE': 'django.db.backends.mysql', # 사용 엔진 , mysql
        'NAME': 'genome_data', # 연동할 mysql DB 이름
        'USER': 'root', # DB 접속 계정명
        'PASSWORD': '1234', # 해당 DB 접속 계정 비밀번호
        'HOST': 'localhost', # 실제 DB 주소
        'PORT': '3306', # 포트번호
    },
    'rating_db': {  # 평점 db
        'ENGINE': 'django.db.backends.mysql', # 사용 엔진 , mysql
        'NAME': 'rating_data', # 연동할 mysql DB 이름
        'USER': 'root', # DB 접속 계정명
        'PASSWORD': '1234', # 해당 DB 접속 계정 비밀번호
        'HOST': 'localhost', # 실제 DB 주소
        'PORT': '3306', # 포트번호
    }

}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 로그인/로그아웃 성공 시 이동할 페이지 등록
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MODEL_ROOT = os.path.join(BASE_DIR, 'models')  # 학습 모델들을 저장할 디렉토리
