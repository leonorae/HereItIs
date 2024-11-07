## HereItIs Flask Routes
from flask import Flask, url_for, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    # display all future events
    return render_template('home.html')
# unsure if filtering should be done with additional routes or JS
@app.route('/events/filter/<string:genre>')
def events_filter_genre(genre):
    # display all future events of given genre
    pass

@app.route('/event/<int:event_id>')
def event(event_id):
    # blablabla event_table = api.get_event(event_id)
    
    # placeholder
    event_name = 'test event'
    venue_name = 'cool zone'
    event_description = 'there is music'
    
    return render_template('event.html',
                           event_name=event_name,
                           venue_name=venue_name,
                           # venue address
                           # date/time
                           # artists
                           # ticket pricing
                           # image
                           # media url
                           event_description=event_description)

@app.route('/artists')
def artists():
    # get all artists from database, display them all
    pass
# again unsure if filtering should be done with additional routes or JS
@app.route('/artists/filter/<string:genre>')
def artists_filter_genre(genre):
    # get all artists
    pass

@app.route('/artist/<int:artist_id>') # this would be neater to have as artist_name but id is probably easier to implement
def artist(artist_id):
    # get artist details from database

    # pass values to template
    pass

@app.route('/list/artist')
def list_artist():
    pass

@app.route('/list/event')
def list_event():
    pass
