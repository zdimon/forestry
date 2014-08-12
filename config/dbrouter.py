# -*- coding: utf-8 -*-
class Oldproject(object):
    """
    Маршрутизатор запросов к старой базе hntu_new
    Все модели из приложения oldproject обращаются к базе hntu_new
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'oldproject':
            return 'hntu_new'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'oldproject':
            return 'hntu_new'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'oldproject' or obj2._meta.app_label == 'oldproject':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'hntu_new':
            return model._meta.app_label == 'oldproject'
        elif model._meta.app_label == 'oldproject':
            return False
        return None
