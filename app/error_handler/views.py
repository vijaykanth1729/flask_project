from flask import Flask,render_template,abort
from .. import app
from . import error
@error.app_errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html',title="Forbidden"),403

@error.app_errorhandler(404)
def notFound(error):
    return render_template('errors/404.html',title="Not Found"),404

@error.app_errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html',title="internal server error"),500

@app.route('/500')
def error():
    abort(500)
