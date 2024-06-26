"""
Django settings for my_web project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z5e-7mjj*e(n_75*7u&mlkxxm4_%dr#vdj=xq(#f_9$w%^w__+'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG常量是用于开启、关闭调试模式的，开始过程中用True就行，一旦布置后则需要设置为False，不然会泄露项目的关键信息。
DEBUG = True

# 默认是一个空列表，一个代表这个 Django 网站可以服务的主机／域名的字符串列表。如果 DEBUG 为 False，还需要正确设置 ALLOWED_HOSTS 配置。否则，所有的请求都会以 “Bad Request (400) ” 返回。
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "app01",
    "comic",
]

# 中间件，可以暂时先不用管
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 主路由，这里指的就是my_web/my_web/urls.py文件
ROOT_URLCONF = 'my_web.urls'


# 模板引擎，这里默认就是Django的模板引擎，其中DIRS表示会搜索的路径，默认为根目录下的templates文件夹，APP_DIRS设置为True,表示会搜索app目录下的templates文件夹。
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

# WSGI服务器，指的是my_web/my_web/wsgi.py文件中的application,可以打开这个文件看看里面的内容，不要动就好了。
WSGI_APPLICATION = 'my_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 修改DATABASES 配置项
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'web',  # 数据库名称
        'HOST': '127.0.0.1',  # 数据库地址，本机 ip 地址 127.0.0.1
        'PORT': 3306,  # 端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456789',  # 数据库密码
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_file')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
