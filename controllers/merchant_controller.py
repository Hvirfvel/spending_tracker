from crypt import methods
from flask import Flask, Blueprint, redirect, render_template, request
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint('merchants', __name__)


@merchants_blueprint.route('/merchants')
def new_merchant_current_merchants():
    merchants = merchant_repository.select_all()
    return render_template('merchants/index.html', merchants=merchants)

@merchants_blueprint.route('/merchants', methods=['POST'])
def create_merchant():
    name = request.form['name']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    return redirect('/merchants')

@merchants_blueprint.route('/merchants/<id>/edit')
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    merchants = merchant_repository.select_all()
    return render_template('merchants/edit.html', merchant=merchant, merchants=merchants)

@merchants_blueprint.route('/merchants/<id>', methods=['POST'])
def update_merchant(id):
    name = request.form['updated_name']
    merchant = Merchant(name, id)
    merchant_repository.update(merchant)
    return redirect('/merchants')
