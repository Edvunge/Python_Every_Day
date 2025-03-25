from flask import request, redirect, url_for, render_template
from app import app, db
from app.models import Item

@app.routes('/')
def index():
    items_ = Item.query.all()
    return render_templete('index.html', items=items_)