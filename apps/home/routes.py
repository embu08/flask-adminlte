# -*- encoding: utf-8 -*-

from apps.home import blueprint
from apps import db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from apps.home.models import Product
from apps.home.forms import AddNewProductForm, DeleteProductForm, UpdateProductForm, UPCForm

headers = ('UPC', 'Image', 'Product name', 'Brand name', 'Model', 'Quantity', 'Price', 'Last change')


@blueprint.route('/add-new', methods=['GET', 'POST'])
@login_required
def add_new():
    form = AddNewProductForm(request.form)
    errors = {}
    if form.validate_on_submit():
        try:
            upc = request.form['upc']
            if db.session.query(Product).filter_by(upc=upc).first():
                raise ValueError(f'upc {upc} already exists')
            main_pic = request.form['main_pic']
            name = request.form['name']
            brand_name = request.form['brand_name']
            model = request.form['model']
            qty = request.form['qty']
            in_stock = True
            price = request.form['price']
            free_shipping = request.form['free_shipping']
            product = Product(upc=upc,
                              main_pic=main_pic,
                              name=name,
                              brand_name=brand_name,
                              model=model,
                              qty=qty,
                              in_stock=in_stock,
                              price=price,
                              free_shipping=free_shipping)
            db.session.add(product)
            db.session.commit()
            flash('Product added successfully', category='text-white bg-success')
        except Exception as e:
            flash("Product wasn't added: " + str(e), category='text-white bg-danger')
    else:
        errors = get_errors(form.data)
        if errors:
            flash("There is some trouble(-s) with form", category='text-white bg-danger')
    return render_template('home/add-new.html', form=form, errors=errors)


@blueprint.route('/products')
@login_required
def products():
    data = db.session.query(Product.upc, Product.main_pic, Product.name, Product.brand_name, Product.model, Product.qty,
                            Product.price, Product.last_change)
    return render_template('home/products.html', headers=headers, data=data)


@blueprint.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    form = UPCForm(request.form)
    if form.validate_on_submit():
        try:
            upc = form.upc.data  # request.form['upc']
            cur_product = db.session.query(Product).filter_by(upc=upc).first()
            if cur_product:
                return redirect(url_for('home_blueprint.update_post', upc=upc))
            else:
                flash(f"There is no product with such UPC - {upc}", category='text-white bg-danger')
        except Exception as e:
            flash("Product wasn't showed: " + str(e), category='text-white bg-danger')
    else:
        if form.errors:
            flash("There is some trouble(-s) with form", category='text-white bg-danger')
    return render_template('home/update.html', form=form)


@blueprint.route('/update-post-<upc>', methods=['GET', 'POST'])
@login_required
def update_post(upc):
    form = UpdateProductForm(request.form)
    data = show_product(upc)
    errors = {}
    if form.validate_on_submit():
        try:
            values = ('main_pic', 'name', 'brand_name', 'model', 'qty', 'price', 'free_shipping')
            updating = {}
            for v in values:
                if request.form[v]:
                    updating[v] = request.form[v]
            if updating:
                db.session.query(Product).filter_by(upc=upc).update(updating)
                db.session.commit()
                flash('Product was successfully updated', category='text-white bg-success')
                data = show_product(upc)
        except Exception as e:
            flash("Product wasn't updated: " + str(e), category='text-white bg-danger')
    else:
        errors = get_errors(form.data)
        if errors:
            flash("There is some trouble(-s) with form", category='text-white bg-danger')

    return render_template('home/update-post.html', form=form, upc=upc, data=data, errors=errors)


@blueprint.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    form = DeleteProductForm(request.form)
    data = False
    if form.validate_on_submit():
        try:
            upc = request.form['upc']
            cur_product = db.session.query(Product).filter_by(upc=upc).first()
            if cur_product:
                if 'delete' in request.form:
                    db.session.query(Product).filter_by(upc=upc).delete()
                    db.session.commit()
                    flash('Product was successfully deleted', category='text-white bg-success')
                elif 'show_product' in request.form:
                    data = show_product(upc)
            else:
                flash(f"There is no product with such UPC - {upc}", category='text-white bg-danger')
        except Exception as e:
            flash("There is some problem: " + str(e), category='text-white bg-danger')
    else:
        if form.errors:
            flash("There is some trouble(-s) with form", category='text-white bg-danger')
    return render_template('home/delete.html', form=form, data=data)


@blueprint.route('/contacts')
@login_required
def contacts():
    return render_template('home/contacts.html')


@blueprint.route('/<template>')
@login_required
def unrecognized_template(template):
    if '.html' in template:
        template = template[:-5]
    return render_template('home/' + template + '.html')


def show_product(upc):
    db_product = db.session.query(Product.upc, Product.main_pic, Product.name, Product.brand_name,
                                  Product.model, Product.qty,
                                  Product.price, Product.last_change).filter_by(upc=upc).first()
    data = [(headers[i], db_product[i]) for i in range(len(headers))]
    return data


def get_errors(data):
    er = {}
    for d in data:
        if data[d] and d not in ('csrf_token', 'submit'):
            er[d] = data[d]
    return er
