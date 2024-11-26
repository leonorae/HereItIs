############################################
#
# HereItIs - Flask App
#
# This file uses routes to render HTML templates and to fetch data from the API, 
# which is passed to JavaScript.
# 
############################################



from flask import Flask, url_for, render_template, request, jsonify
from markupsafe import escape
import requests

app = Flask(__name__)

# Index Route
@app.route('/')
def home():
    return render_template('index.html')

# API Route for Index Page
@app.route('/api/events')
def get_events():
    """
    " Get events from the API
    " @return: JSON response with events
    """
    print('Fetching events...')
    try:
        response = requests.get('https://hereitis-aomy.onrender.com/api/events')
        response.raise_for_status()  # Raise an exception for HTTP errors
        events = response.json()
        print('Events fetched successfully:', events)
    except requests.exceptions.RequestException as e:
        print('Error fetching events:', e)
        events = []
    return jsonify(events)

# Event Page
@app.route('/events/<int:event_id>')
def event(event_id):
    return render_template('event.html', event_id=event_id)

# API Route for Event Page
@app.route('/api/events/<int:event_id>')
def get_event(event_id):
    """
    " Get event details from the API
    " @param event_id: ID of the event
    " @return: JSON response with event details
    """
    print('Fetching event...')
    try:
        response = requests.get('https://hereitis-aomy.onrender.com/api/events')
        if response.status_code == 200:
            print('Events fetched succssfully')
            print(f'Fetching event details for {event_id}...')

            # Should I loop though the JSON to find the matching event ID? 
            for event in response.json():
                print(f"An event: {event}")
                for key in event:
                    print(f"Key: {key}, Value: {event[key]}")
                if event['idevent'] == event_id:
                    print('Event found:', event)
                    return event

            # Looped through and didn't find the event_id 
            print(f'Event with ID {event_id} not found.')
            return jsonify({})

    except requests.exceptions.RequestException as e:
        print('Error fetching event:', e)
        return f'Error fetching event: {e}'
    finally:
        pass


"""
curl -X POST https://hereitis-aomy.onrender.com/api/event -H "Content-Type: application/json" -d '{
    "Name": "Concert One",
    "DateTime": "2025-01-01 19:00:00",
    "Description": "New Year concert",
    "ArtistID": 1,   // replace with actual ArtistID
    "VenueID": 1,    // replace with actual VenueID
    "TicketPrice": 49.99,
    "PosterURL": "http://poster.url"
}'
"""

@app.route('/addeventform', methods=['GET', 'POST'])
def submit_event_form():
    # Determine if the form is a get or post request
    if request.method == 'GET':
        return render_template('addeventform.html')
    
    # If the form is a post request
    if request.method == 'POST':
        name = request.form['event-name']
        date = request.form['event-date']
        description = request.form['description']
        artist_id = request.form['artist-id']
        venue_id = request.form['venue-id']
        ticket_price = request.form['ticket-price']
        poster_url = request.form['poster-url']

        print(f'Name: {name}, Date: {date}, Description: {description}, ArtistID: {artist_id}, VenueID: {venue_id}, TicketPrice: {ticket_price}, PosterURL: {poster_url}')

        # Add the event to the database
        response = requests.post('https://hereitis-aomy.onrender.com/api/event', json={
            'Name': name,
            'DateTime': date,
            'Description': description,
            'ArtistID': artist_id,
            'VenueID': venue_id,
            'TicketPrice': ticket_price,
            'PosterURL': poster_url
        })
        # TODO: check the error handling, it throws an error despite successful post to DB
        if response.status_code != 201:
            print(f"Error adding event: {response.text}")
            return f"Error adding event: {response.text}"
        else:
            print(f"Event added successfully: {response.text}")
            return f"Event added successfully: {response.text}"

# Artist List Page
@app.route('/artists')
def artists():
    return render_template('artistlist.html')

# API Route for Artist List
@app.route('/api/artists')
def get_artists():
    """
    " Get artists from the API
    " @return: JSON response with artists
    """
    print('Fetching artists...')
    try:
        response = requests.get('https://hereitis-aomy.onrender.com/api/artists')
        response.raise_for_status()  # Raise an exception for HTTP errors
        artists = response.json()
        print('Artists fetched successfully:', artists)
    except requests.exceptions.RequestException as e:
        print('Error fetching artists:', e)
        artists = []
    return jsonify(artists)

# Artist Page
@app.route('/artists/<int:artist_id>')
def artist(artist_id):
    return render_template('artist.html', artist_id=artist_id)

# API Route for Artist Page
@app.route('/api/artists/<int:artist_id>')
def get_artist(artist_id):
    """
    " Get artist details from the API
    " @param artist_id: ID of the artist
    " @return: JSON response with artist details
    """
    print('Fetching artist...')
    try:
        response = requests.get('https://hereitis-aomy.onrender.com/api/artists')
        if response.status_code == 200:
            print('Artists fetched succssfully')
            print(f'Fetching artist details for {artist_id}...')

            # Should I loop though the JSON to find the matching artist ID? 
            for artist in response.json():
                print(f"An artist: {artist}")
                for key in artist:
                    print(f"Key: {key}, Value: {artist[key]}")
                if artist['artistid'] == artist_id:
                    print('Artist found:', artist)
                    return artist

            # Looped through and didn't find the artist_id 
            print(f'Artist with ID {artist_id} not found.')
            return jsonify({})

    # TODO: check the error handling here I think it isn't working properly
    except requests.exceptions.RequestException as e:
        print('Error fetching artist:', e)
        return f'Error fetching artist: {e}'
    finally:
        pass


# Add Artist Form
@app.route('/addartistform', methods=['GET', 'POST'])
def submit_artist_form():
    # TODO: Check the parameters and the form fields to make sure they match and include all data
    if request.method == 'GET':
        return render_template('addartistform.html')
    if request.method == 'POST':
        username = request.form['artist-username']
        name = request.form['artist-name']
        bio = request.form['artist-bio']
        profile_url = request.form['profile-url']
        location = request.form['artist-location']

        print(f'Username: {username}, Name: {name}, Bio: {bio}, ProfileURL: {profile_url}, Location: {location}')

        # Add new artist to DB
        response = requests.post('https://hereitis-aomy.onrender.com/api/artist', json={
            'ArtistUserName': username,
            'Name': name,
            'Bio': bio,
            'ImageURL': profile_url,
            'Location': location
        })

        #TODO: verify the correct status
        if response.status_code != 201:
            print(f"Error adding artist: {response.text}")
            print(f"Response Code: {response.status_code}")
            return f"Error adding artist: {response.text}... Response Code: {response.status_code}"
        else:
            print(f"Artist added successfully: {response.text}")
            return f"Artist added successfully: {response.text}"
        



if __name__ == '__main__':
    app.run(debug=True)
