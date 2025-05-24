# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Tipo_Movimiento(db.Model):

    __tablename__ = 'Tipo_Movimiento'

    id = db.Column(db.Integer, primary_key=True)

    #__Tipo_Movimiento_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    nombre = db.Column(db.String(255),  nullable=True)
    descripcion = db.Column(db.String(255),  nullable=True)

    #__Tipo_Movimiento_FIELDS__END

    def __init__(self, **kwargs):
        super(Tipo_Movimiento, self).__init__(**kwargs)


class Categoria(db.Model):

    __tablename__ = 'Categoria'

    id = db.Column(db.Integer, primary_key=True)

    #__Categoria_FIELDS__
    descripcion = db.Column(db.String(255),  nullable=True)

    #__Categoria_FIELDS__END

    def __init__(self, **kwargs):
        super(Categoria, self).__init__(**kwargs)


class Tipo_Cuenta(db.Model):

    __tablename__ = 'Tipo_Cuenta'

    id = db.Column(db.Integer, primary_key=True)

    #__Tipo_Cuenta_FIELDS__
    descripcion = db.Column(db.String(255),  nullable=True)

    #__Tipo_Cuenta_FIELDS__END

    def __init__(self, **kwargs):
        super(Tipo_Cuenta, self).__init__(**kwargs)


class Subcategoria(db.Model):

    __tablename__ = 'Subcategoria'

    id = db.Column(db.Integer, primary_key=True)

    #__Subcategoria_FIELDS__
    descripcion = db.Column(db.String(255),  nullable=True)

    #__Subcategoria_FIELDS__END

    def __init__(self, **kwargs):
        super(Subcategoria, self).__init__(**kwargs)


class Cuenta(db.Model):

    __tablename__ = 'Cuenta'

    id = db.Column(db.Integer, primary_key=True)

    #__Cuenta_FIELDS__
    saldo = db.Column(db.Integer, nullable=True)

    #__Cuenta_FIELDS__END

    def __init__(self, **kwargs):
        super(Cuenta, self).__init__(**kwargs)


class Movimiento(db.Model):

    __tablename__ = 'Movimiento'

    id = db.Column(db.Integer, primary_key=True)

    #__Movimiento_FIELDS__
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())
    importe = db.Column(db.Integer, nullable=True)
    concepto = db.Column(db.String(255),  nullable=True)
    fecha_vencimiento = db.Column(db.DateTime, default=db.func.current_timestamp())
    estado = db.Column(db.Boolean, nullable=True)

    #__Movimiento_FIELDS__END

    def __init__(self, **kwargs):
        super(Movimiento, self).__init__(**kwargs)



#__MODELS__END
