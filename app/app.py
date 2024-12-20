############################################
#
# HereItIs - Flask App
#
# This file uses routes to render HTML templates and to fetch data from the API, 
# which is passed to JavaScript.
# 
############################################
#
# Routes Included:
#
# '/' - Index Route
# '/api/events' - API Route for Index Page
# '/events/<int:event_id>' - Event Page
# '/api/events/<int:event_id>' - API Route for Event Page
# '/addeventform' - Add Event Form
# '/api/event/' - API Endpoint to add an event
# '/artists' - Artist List Page
# '/api/artists' - API Route for Artist List
# '/artists/username/<string:artist_username>' - Artist Page
# '/api/artists/username/<string:artist_username>/info-and-events' - (deprecated) API Endpoint for artist info and upcoming events
# '/api/artists/username/<string:username>' - API Endpoint to get artist details by username
# '/api/artists/<int:artist_id>' - API Endpoint to get artist details by username
# '/api/artists/<int:artist_id>/events' - API Endpoint to get upcoming events for artist by artistID
# '/addartistform' - Site route for the form to add an artist
# '/api/artist' - API Endpoint to insert an Artist
# '/api/venue' - API Endpoint to insert a Venue
# '/api/venues' - API Endpoint to retrieve all venues from the Venue table
# '/about' - Site route for the about Page
#
############################################

# TODO: Standardize the error handling: I disassmebled some for error handling, ironically but it was indention errors that caused issues
# TODO: Comments for each route (docstrings, inline comments, etc.) / Sorry for lack of comments :( I got focused on getting it up and running

from flask import Flask, url_for, render_template, request, jsonify
from markupsafe import escape
from psycopg2.extras import RealDictCursor
from psycopg2 import DatabaseError
import psycopg2
import requests
import json

# create app to use in this Flask application
app = Flask(__name__)

### Database
# Database connection details
db_url = "postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a.oregon-postgres.render.com/mohammed_db"
# Database connection function
def get_db_connection():
    try:
        conn = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None
    
### Routes
# Site route for homepage (list of all events)
@app.route('/')
def home():
    return render_template('index.html')

# API Endpoint for getting all events (called by index page)
@app.route('/api/events')
def get_events():
    """
    Fetches and returns all event records from the Event table.
    Returns:
        JSON: A list of event records or an error message if an exception occurs.
    """
    try:
        # Establish database connection
        conn = get_db_connection()
        cur = conn.cursor()

        # Execute SQL query to fetch all events
        cur.execute('SELECT * FROM Event;')
        # Need to also fetch Arist Name and Venue Name from Event ID
        cur.execute('''
            SELECT e.*, a.Name as ArtistName, v.Name as VenueName, a.ArtistUserName
            FROM Event e
            LEFT JOIN Artist a ON e.ArtistID = a.ArtistID
            LEFT JOIN Venue v ON e.VenueID = v.VenueID;
                    ''')
        events = cur.fetchall()  # Fetch all results
        
        # Return the list of events as a JSON response
        return jsonify(events), 200
    except Exception as e:
        # Handle and return any errors as JSON
        return jsonify({"error": str(e)}), 500
    finally:
        # Ensure the cursor and connection are closed
        cur.close()
        conn.close()

# Site route for individual event page (by ID)
@app.route('/events/<int:event_id>')
def event(event_id):
    return render_template('event.html', event_id=event_id)

# API Endpoint to get event details by event ID
@app.route('/api/events/<int:event_id>')
def get_event(event_id):
    """
    Fetches and returns event details for a specific event ID.
    Returns:
        JSON: Event details including associated artist and venue information
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed."}), 500
    try:
        cur = conn.cursor()
        
        # JOIN query, single query
        cur.execute('''
            SELECT 
                e.*,
                a.Name as ArtistName,
                a.ArtistUserName,
                a.ImageURL as ArtistImageURL,
                v.Name as VenueName,
                v.Location as VenueLocation,
                v.Description as VenueDescription
            FROM Event e
            LEFT JOIN Artist a ON e.ArtistID = a.ArtistID
            LEFT JOIN Venue v ON e.VenueID = v.VenueID
            WHERE e.idEvent = %s;
        ''', (event_id,))
        
        event = cur.fetchone()
        
        # Return event if found, otherwise 404
        if event:
            return jsonify(event), 200
        else:
            return jsonify({"error": f"Event with ID {event_id} not found"}), 404

    except Exception as e:
        # Log error and return generic error message
        print("Error fetching event:", str(e))
        return jsonify({"error": "Failed to retrieve event details"}), 500
        
    finally:
        # Ensure database resources are released
        cur.close()
        conn.close()

# Site route for the form to add an event
@app.route('/addeventform', methods=['GET', 'POST'])
def submit_event_form():
    # Determine if the form is a get or post request
    if request.method == 'GET':
        return render_template('AddEventForm.html')
    
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
        response = requests.post('https://hereitis-v3.onrender.com/api/event', json={
            'Name': name,
            'DateTime': date,
            'Description': description,
            'ArtistID': artist_id,
            'VenueID': venue_id,
            'TicketPrice': ticket_price,
            'PosterURL': poster_url
        })
        # TODO: check the error handling, it throws an error despite successful post to DB
        # resolved: this check was not indented under the post method
        if response.status_code != 201:
            print(f"Error adding event: {response.text}")
            print(f"Response Code: {response.status_code}")
            #return f"Error adding event: {response.text}"
            return render_template('failure-form.html')
        else:
            print(f"Event added successfully: {response.text}")
            print(f"Response Code: {response.status_code}")
            #return f"Event added successfully: {response.text}"
            return render_template('successful-form.html')

# LG: Pretty sure this code should really just be in the above route
#     having it post to this other route is silly, but the fastest way to merge.
# TODO: properly merge this hack, see above comment
# Endpoint to insert an Event
@app.route('/api/event', methods=['POST'])
def insert_event():
    data = request.json
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed."}), 500

    try:
        cur = conn.cursor()
        
        # Insert event data and request Event ID to be returned
        cur.execute('''
            INSERT INTO Event (Name, DateTime, Description, ArtistID, VenueID, TicketPrice, PosterURL)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING idEvent;
        ''', (data['Name'], data['DateTime'], data.get('Description'), data['ArtistID'], 
              data['VenueID'], data.get('TicketPrice'), data.get('PosterURL')))
        
        # Fetch the result and retrieve Event ID
        result = cur.fetchone()
        if result:
            event_id = result['idevent'] if 'idevent' in result else None
            conn.commit()
            if event_id:
                return jsonify({"EventID": event_id, "message": "Event added successfully"}), 201
            else:
                return jsonify({"EventID": None, "message": "Event added, but EventID not retrieved"}), 201
        else:
            return jsonify({"error": "Failed to retrieve EventID from database."}), 500

    except Exception as e:
        conn.rollback()
        print("Error on insert:", str(e))
        return jsonify({"error": f"Insertion failed: {str(e)}"}), 400

    finally:
        cur.close()
        conn.close()

# Site route for the artists page, a list of all artists 
@app.route('/artists')
def artists():
    return render_template('artistlist.html')

# API Endpoint for the list of all artists
@app.route('/api/artists')
def get_artists():
    """
    Fetches and returns all artist records from the Artist table.
    Returns:
        JSON: A list of artist records or an error message if an exception occurs.
    """
    # LG: once again, I just replaced it
    # TODO: see if it works, remove this comment if it does
    try:
        # Establish database connection
        conn = get_db_connection()
        cur = conn.cursor()

        # Execute SQL query to fetch all artists
        cur.execute('SELECT * FROM Artist;')
        artists = cur.fetchall()  # Fetch all results

        # Return the list of artists as a JSON response
        return jsonify(artists), 200
    except Exception as e:
        # Handle and return any errors as JSON
        return jsonify({"error": str(e)}), 500
    finally:
        # Ensure the cursor and connection are closed
        cur.close()
        conn.close()

# Site route for individual artist pages, by artist username
@app.route('/artists/username/<string:artist_username>')
def artist(artist_username):
    return render_template('artist.html', artist_username=artist_username)

# LG: This works, but has duplicate code copy/pasted/mangled/taped-and-glued from the API routes in it
#     This should all be refactored
#     UPDATE: this is also basically deprecated and should probably just be removed, but I will leave it for now
# API Endpoint for Artist info, their upcoming events, and the count of their upcoming events
@app.route('/api/artists/username/<string:artist_username>/info-and-events')
def get_artist(artist_username):
    """
    " Get artist details from the API
    " @param artist_id: ID of the artist
    " @return: JSON response with artist details
    """
    print('Fetching artist...')
    # GET ARTIST INFO
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed."}), 500
    try:
        cur = conn.cursor()
        
        # SQL query
        cur.execute('''
            SELECT ArtistID, 
                   ArtistUserName, 
                   Name, 
                   Bio, 
                   ImageURL, 
                   Location,
                   FacebookURL,
                   InstagramURL,
                   SoundCloudURL 
            FROM Artist 
            WHERE ArtistUserName = %s;
        ''', (artist_username,))
        artist = cur.fetchone()
        
        # Return artist if found, otherwise 404
        if not artist:
            return jsonify({"error": f"Artist with username '{username}' not found"}), 404
        
        print('Artist fetched succssfully')
        print(f'Fetching event details for {artist_username}...')
        # get the artist_id and pass it in
        artist_id = artist['artistid']
        print(f'Artist ID: {artist_id}')
        
        # SQL Query for events
        # Get future events only, joined with venue details, sorted by date
        cur.execute('''
            SELECT e.*, v.* 
            FROM Event e
            JOIN Venue v ON e.VenueID = v.VenueID
            WHERE e.ArtistID = %s
            AND e.DateTime >= CURRENT_TIMESTAMP
            ORDER BY e.DateTime ASC;
        ''', (artist_id,))
        upcoming_events = cur.fetchall()
        
        # Format response with events list and count
        artist_events = {
            "events": upcoming_events,
            "event_count": len(upcoming_events)
        }
        
        merged_dict = {**artist, **artist_events}

        return jsonify(merged_dict)
        
    except Exception as e:
        print("Error fetching artist:", str(e))
        return jsonify({"error": "Failed to retrieve artist details"}), 500
    
    finally:
        cur.close()
        conn.close()

# API Endpoint to get artist details by username
@app.route('/api/artists/username/<string:username>', methods=['GET'])
def get_artist_by_username(username):
    """
    Fetches and returns artist details for a specific username.
    Returns:
        JSON: Artist details (id, username, name, bio, image, location, social media URLs)
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed."}), 500

    try:
        cur = conn.cursor()
        
        # SQL query
        cur.execute('''
            SELECT ArtistID, 
                   ArtistUserName, 
                   Name, 
                   Bio, 
                   ImageURL, 
                   Location,
                   FacebookURL,
                   InstagramURL,
                   SoundCloudURL 
            FROM Artist 
            WHERE ArtistUserName = %s;
        ''', (username,))
        artist = cur.fetchone()
        
        # Return artist if found, otherwise 404
        if not artist:
            return jsonify({"error": f"Artist with username '{username}' not found"}), 404
            
        return jsonify(artist), 200
            
    except Exception as e:
        print("Error fetching artist:", str(e))
        return jsonify({"error": "Failed to retrieve artist details"}), 500
        
    finally:
        cur.close()
        conn.close()

# API Endpoint to get all events for artist by artistID 
@app.route('/api/artists/<int:artist_id>/events', methods=['GET'])
def get_artist_events(artist_id):
    """
    Fetches and returns all upcoming events for a specific artist ID.
    Returns:
        JSON: List of upcoming events with venue details
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed."}), 500

    try:
        cur = conn.cursor()

        #SQL Query    
        # Get all events, joined with venue details, sorted by date
        cur.execute('''
            SELECT e.name as eventName, v.name as venueName, e.*, v.*
            FROM Event e
            JOIN Venue v ON e.VenueID = v.VenueID
            WHERE e.ArtistID = %s
            ORDER BY e.DateTime ASC;
        ''', (artist_id,))
        
        events = cur.fetchall()
        
        # Format response with events list and count
        response = {
            "events": events,
            "event_count": len(events)
        }
        
        return jsonify(response), 200
            
    except Exception as e:
        print("Error fetching artist events:", str(e))
        return jsonify({"error": "Failed to retrieve artist events"}), 500
        
    finally:
        cur.close()
        conn.close()

# Site route for the form to add an artist
@app.route('/addartistform', methods=['GET', 'POST'])
def submit_artist_form():
    # TODO: Check the parameters and the form fields to make sure they match and include all data
    if request.method == 'GET':
        return render_template('AddArtistForm.html')
    if request.method == 'POST':
        username = request.form['artist-username']
        name = request.form['artist-name']
        bio = request.form['artist-bio']
        profile_url = request.form['profile-url']
        location = request.form['artist-location']
        facebook_url = request.form['facebook-url']
        instagram_url = request.form['instagram-url']
        soundcloud_url = request.form['soundcloud-url']

        print(f'Username: {username}, Name: {name}, Bio: {bio}, ProfileURL: {profile_url}, Location: {location}')

        # Add new artist to DB
        response = requests.post('https://hereitis-v3.onrender.com/api/artist', json={
            'ArtistUserName': username,
            'Name': name,
            'Bio': bio,
            'ImageURL': profile_url,
            'Location': location,
            'FacebookURL': facebook_url,
            'instagramURL': instagram_url,
            'SoundCloudURL': soundcloud_url,
        })

        #TODO: verify the correct status
        if response.status_code != 201:
            print(f"Error adding artist: {response.text}")
            print(f"Response Code: {response.status_code}")
            # return f"Error adding artist: {response.text}... Response Code: {response.status_code}"
            return render_template('failure-form.html')
        else:
            print(f"Artist added successfully: {response.text}")
            # return f"Artist added successfully: {response.text}"
            return render_template('successful-form.html')

# LG: I did the same thing as with addevent.
#     Once again, pretty sure this code should really just be in the above route,
#     having it post to this other route is silly, but the fastest way to merge.
# TODO: properly merge this hack, see above comment
# API Endpoint to insert an Artist
@app.route('/api/artist', methods=['POST'])
def insert_artist():
    data = request.json
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed."}), 500

    try:
        cur = conn.cursor()
        
        # Insert artist data and request ArtistID to be returned
        cur.execute('''
            INSERT INTO Artist (ArtistUserName, Name, Bio, ImageURL, Location, FacebookURL, InstagramURL, SoundCloudURL)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING ArtistID;
        ''', (data['ArtistUserName'], data['Name'], data.get('Bio'), data.get('ImageURL'), data.get('Location'), data.get('FacebookURL'), data.get('InstagramURL'), data.get('SoundCloudURL')))
        
        # Fetch the result and retrieve ArtistID
        result = cur.fetchone()
        if result:
            artist_id = result['artistid'] if 'artistid' in result else None
            conn.commit()
            if artist_id:
                return jsonify({"ArtistID": artist_id, "message": "Artist added successfully"}), 201
            else:
                return jsonify({"ArtistID": None, "message": "Artist added, but ArtistID not retrieved"}), 201
        else:
            return jsonify({"error": "Failed to retrieve ArtistID from database"}), 500

    except Exception as e:
        conn.rollback()
        print("Error on insert:", str(e))
        return jsonify({"error": f"Insertion failed: {str(e)}"}), 400

    finally:
        cur.close()
        conn.close()

# LG: do we need this venue code? leaving it just in case
# API Endpoint to insert a Venue
@app.route('/api/venue', methods=['POST'])
def insert_venue():
    """
    Inserts a new venue into the Venue table.
    Expects JSON data with 'Name', 'Location', and 'Description' fields.
    Returns the new VenueID upon successful insertion.
    """
    data = request.json
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed."}), 500

    try:
        cur = conn.cursor()

        # Insert venue data and request VenueID to be returned
        cur.execute('''
            INSERT INTO Venue (Name, Location, Description)
            VALUES (%s, %s, %s)
            RETURNING VenueID;
        ''', (data['Name'], data.get('Location'), data.get('Description')))
        
        # Fetch the result and retrieve VenueID
        result = cur.fetchone()
        if result:
            venue_id = result['venueid'] if 'venueid' in result else None
            conn.commit()
            if venue_id:
                return jsonify({"VenueID": venue_id, "message": "Venue added successfully"}), 201
            else:
                return jsonify({"VenueID": None, "message": "Venue added, but VenueID not retrieved"}), 201
        else:
            return jsonify({"error": "Failed to retrieve VenueID from database."}), 500

    except Exception as e:
        conn.rollback()
        print("Error on insert:", str(e))
        return jsonify({"error": f"Insertion failed: {str(e)}"}), 400

    finally:
        cur.close()
        conn.close()

# API Endpoint to retrieve all venues from the Venue table
@app.route('/api/venues', methods=['GET'])
def get_all_venues():
    """
    Fetches and returns all venue records from the Venue table.
    Returns:
        JSON: A list of venue records or an error message if an exception occurs.
    """
    try:
        # Establish database connection
        conn = get_db_connection()
        cur = conn.cursor()
        # Execute SQL query to fetch all venues
        cur.execute('SELECT * FROM Venue;')
        venues = cur.fetchall()  # Fetch all results

        # Return the list of venues as a JSON response
        return jsonify(venues), 200
    except Exception as e:
        # Handle and return any errors as JSON
        return jsonify({"error": str(e)}), 500
    finally:
        # Ensure the cursor and connection are closed
        cur.close()
        conn.close()


@app.route('/get-listed')
def get_listed():
    return render_template('get-listed.html')

        
# Site route for the about Page
@app.route('/about')
def about():
    return render_template('about.html')

# Run the app
# Debug mode is on for development but needs to be changed to False for production
if __name__ == '__main__':
    app.run(debug=True)
