# -*- coding: utf-8 -*-
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'forest_fire',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',
        'PASSWORD': '1q2w3e',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    },

    'hntu_new': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hntu_new',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',
        'PASSWORD': '1q2w3e',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }

}