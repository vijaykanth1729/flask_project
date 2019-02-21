from flask import Blueprint,render_template
error=Blueprint('error',__name__)
from . import views