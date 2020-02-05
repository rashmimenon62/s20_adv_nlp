from flask import Blueprint, render_template, request
from . import db
from .models import ReutersDoc

reuters_docs = Blueprint('reuters_docs', __name__)

@reuters_docs.route('/reuters_dataset')
def reuters_dataset():

    docs = []
    docs = ReutersDoc.query.all()
    return render_template('reuters_dataset.html', docs=docs)

@reuters_docs.route('/view_page')
def view_page():
    id = request.args.get('id', default=1, type=int)
    doc = ReutersDoc.query.filter_by(id=id).first()

    return render_template('view_page.html', doc=doc)