###############################################################################
##
##TBD
##TBD
##
###############################################################################


###############################################################################
# Import libraries
from flask import Flask, url_for, request, jsonify, render_template
from markupsafe import escape
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import DatabaseError

# create app to use in this Flask application
app = Flask(__name__)



# Database connection details
db_url = "postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a.oregon-postgres.render.com/mohammed_db"



# index page
@app.route('/')
def index():
    return render_template('index.html')


# venue page
@app.route('/venue/<venue_name>')
def venue():
    return render_template('venues/venue.html',venue_name=venue_name)


# user page
@app.route('/users/<user_name>')
def user():
    return render_template('users/user.html',user_name=user_name)


# events page
@app.route('/events/<event_name>')
def event():
    return render_template('event/event.html',event_name=event_name)


# artist page
@app.route('/artists/<artist_name>')
def artist():
    return render_template('artists/artist.html',artist_name=artist_name)

# Database connection function
def get_db_connection():
    try:
        conn = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None

# Endpoint to insert an Artist
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


# Endpoint to insert a Venue
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


# Endpoint to retrieve all artists from the Artist table
@app.route('/api/artists', methods=['GET'])
def get_all_artists():
    """
    Fetches and returns all artist records from the Artist table.
    Returns:
        JSON: A list of artist records or an error message if an exception occurs.
    """
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

# Endpoint to retrieve all venues from the Venue table
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

# Endpoint to retrieve all events from the Event table
@app.route('/api/events', methods=['GET'])
def get_all_events():
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

# Endpoint to get event details by event ID
@app.route('/api/events/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    """
    Fetches and returns event details for a specific event ID.
    Returns:
        JSON: Event details including associated artist and venue information
    """
    # Establish database connection with error handling
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

# Endpoint to get artist details by username        
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

# Endpoint to get upcoming events for artist by artistID 
@app.route('/api/artists/<int:artist_id>/events', methods=['GET'])
def get_artist_upcoming_events(artist_id):
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
        response = {
            "events": upcoming_events,
            "event_count": len(upcoming_events)
        }
        
        return jsonify(response), 200
            
    except Exception as e:
        print("Error fetching artist events:", str(e))
        return jsonify({"error": "Failed to retrieve artist events"}), 500
        
    finally:
        cur.close()
        conn.close()


###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308, debug=True)
