from crypt import methods
from flask import Flask, Blueprint, render_template, request, redirect
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint('tags', __name__)

@tags_blueprint.route('/tags')
def index():
    tags = tag_repository.select_all()
    return render_template('tags/index.html', tags=tags)

@tags_blueprint.route('/tags', methods=['POST'])
def create_tag():
    name = request.form['name']
    tag = Tag(name)
    tag_repository.save(tag)
    return redirect('/tags')