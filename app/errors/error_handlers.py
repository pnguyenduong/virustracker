from flask import Blueprint


errors = Blueprint('error', __name__)


@errors.app_errorhandler(403)
def error_403(error):
    return '<h3>You don\'t have permission to do that (403). Please check your account and try again</h3>', 404


@errors.app_errorhandler(404)
def error_404(error):
    return '<h3>Oops, Page not Found (404). That page does not exist. Please try a different location</h3>', 404

@errors.app_errorhandler(500)
def error_500(error):
    return '<h3>Something went wrong (500). We\'re experiencing some trouble on our end. Pleaes try again later</h3>', 404