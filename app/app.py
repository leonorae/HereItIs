## HereItIs Flask Routes
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')        

@app.route('/event/<int:event_id>')
def event(event_id):
    # blablabla event_table = api.get_event(event_id)
    # (gets event and instantiates python object)
    # placeholder
    event_name = 'test event'
    venue_name = 'cool zone'
    event_description = 'there is music'
    # the args will just be getters from an event object
    return render_template('event.html',
                           event_name=event_name,
                           venue_name=venue_name,
                           event_description=event_description)

