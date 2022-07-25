# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import Length, URL, DataRequired, Optional


class AddNewProductForm(FlaskForm):
    upc = IntegerField('UPC', validators=[DataRequired(message='Not a valid integer value.')])
    main_pic = StringField('Image (url)', validators=[URL()])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=64, message='From 2 to 64 symbols')])
    brand_name = StringField('Brand')
    model = StringField('Model')
    qty = IntegerField('Quantity', validators=[DataRequired(message='Not a valid integer or float value.')])
    price = FloatField('Price', validators=[DataRequired(message='Not a valid integer or float value.')])
    free_shipping = FloatField('Free shipping over',
                               validators=[DataRequired(message='Not a valid integer or float value.')])
    submit = SubmitField('Add a product')


class DeleteProductForm(FlaskForm):
    upc = IntegerField('UPC', validators=[DataRequired(message='Not a valid integer value.')])
    delete = SubmitField('Delete a product')
    show_product = SubmitField('Show a product')


class UpdateProductForm(FlaskForm):
    main_pic = StringField('Image (url)', validators=[Optional(), URL()])
    name = StringField('Name', validators=[Optional(), Length(min=3, max=64, message='From 2 to 64 symbols')])
    brand_name = StringField('Brand', validators=[Optional()])
    model = StringField('Model', validators=[Optional()])
    qty = IntegerField('Quantity', validators=[Optional()])
    price = FloatField('Price', validators=[Optional()])
    free_shipping = FloatField('Free shipping over', validators=[Optional()])
    update = SubmitField('Update a product')


class UPCForm(FlaskForm):
    upc = IntegerField('UPC', validators=[DataRequired(message='Not a valid integer value.')])
    show_product = SubmitField('Show a product')
