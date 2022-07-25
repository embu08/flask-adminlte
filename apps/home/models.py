# -*- encoding: utf-8 -*-

from datetime import datetime
from apps import db


class Product(db.Model):
    __tablename__ = 'Products'

    upc = db.Column(db.Integer, primary_key=True)
    main_pic = db.Column(db.Text)
    name = db.Column(db.String(64))
    brand_name = db.Column(db.String(64))
    model = db.Column(db.String(64))
    qty = db.Column(db.Float)
    in_stock = db.Column(db.Boolean)
    price = db.Column(db.Float)
    free_shipping = db.Column(db.Float)
    last_change = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'upc={self.upc}, name={self.name}'
