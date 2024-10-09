###############################################################################
##
##TBD
##TBD
##
###############################################################################


###############################################################################
# Import libraries
from flask import Flask, url_for
from markupsafe import escape
from flask import render_template
from flask import request



# create app to use in this Flask application
app = Flask(__name__)



# index page
@app.route('/')
def index():
    return render_template('index.html')


# venue page
@app.route('/venue/<venue_name>')
def venue():
    return render_template('venues/venue.html',venue_name=venue_name)

# venue page
@app.route('/venue/<venue_name>')
def venue():
    return render_template('venues/venue.html',venue_name=venue_name)

# user page
@app.route('/users/<user_name>')
def venue():
    return render_template('users/user.html',user_name=user_name)


# events page
@app.route('/events/<event_name>')
def venue():
    return render_template('event/event.html',event_name=event_name)


# artist page
@app.route('/artists/<artist_name>')
def venue():
    return render_template('artists/artist.html',artist_name=artist_name)
###############################################################################
# main driver function
if __name__ == '__main__':
    app = main()
    # run() method of Flask class runs the application
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)
