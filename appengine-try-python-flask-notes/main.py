from flask import Flask
from google.appengine.api import users
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

def check_auth(username, password):
    user = users.get_current_user()
	if user:
		greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
					(user.nickname(), users.create_logout_url('/')))
	else:
		greeting = ('<a href="%s">Sign in or register</a>.' %
					users.create_login_url('/'))

	return greeting

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello Vider!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
