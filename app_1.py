# app.py
from flask import Flask, jsonify, request, render_template
from config import Config
import psycopg2
from database import get_db_connection

# Initialize Flask application
app = Flask(__name__)

# Route to test database connectivity
@app.route('/api/test-db')
def test_db():
    """
    Endpoint to verify database connection is working.
    Returns current timestamp from database if successful.
    """
    try:
        # Attempt to establish database connection
        conn = get_db_connection()
        if conn:
            # Create cursor for executing queries
            cur = conn.cursor()
            # Get current timestamp from database
            cur.execute('SELECT NOW();')
            result = cur.fetchone()
            # Clean up database resources
            cur.close()
            conn.close()
            # Return success response with timestamp
            return jsonify({
                'status': 'success',
                'message': 'Database connected successfully',
                'timestamp': result['now']
            })
        else:
            # Return error if connection failed
            return jsonify({
                'status': 'error',
                'message': 'Could not connect to database'
            }), 500
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# Endpoint to get all upcoming events
@app.route('/api/events', methods=['GET'])
def get_events():
    """
    Retrieves all future events with their associated venue and artist information.
    Returns events sorted by date in ascending order.
    """
    try:
        # Establish database connection
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Execute query to get all future events with related data
        # Uses PostgreSQL's json_build_object to create nested JSON structures
        cur.execute("""
            SELECT 
                e.idevent,                   
                e.name,                       
                e.datetime,                  
                e.description,                
                e.ticket_price,              
                e.poster_url,                 
                json_build_object(            
                    'id', v.venueid,
                    'name', v.name,
                    'location', v.location
                ) as venue,
                json_build_object(            
                    'id', a.artistid,
                    'name', a.name
                ) as artist
            FROM event e
            JOIN venue v ON e.venueid = v.venueid        
            JOIN artist a ON e.artistid = a.artistid     
            WHERE e.datetime > NOW()                    
            ORDER BY e.datetime;                         
        """)
        
        # Fetch all results
        events = cur.fetchall()
        # Clean up database resources
        cur.close()
        conn.close()
        
        # Return success response with events data
        return jsonify({
            'status': 'success',
            'events': events
        })
        
    except Exception as e:
        # Handle any database or processing errors
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# Endpoint to get details of a specific event
@app.route('/api/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    """
    Retrieves detailed information about a specific event, including
    comprehensive venue and artist information with social media links.
    
    Args:
        event_id (int): The unique identifier of the event
    """
    try:
        # Establish database connection
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Execute query to get specific event with extended information
        cur.execute("""
            SELECT 
                e.idevent,
                e.name,
                e.datetime,        
                e.description,
                e.ticket_price,
                e.poster_url,
                json_build_object(         
                    'id', v.venueid,
                    'name', v.name,
                    'location', v.location
                ) as venue,
                json_build_object(            
                    'id', a.artistid,
                    'name', a.name,
                    'bio', a.bio,
                    'social_links', json_build_object(
                        'instagram', a.instagramurl,
                        'facebook', a.facebookurl,
                        'soundcloud', a.soundcloudurl
                    )
                ) as artist
            FROM event e
            JOIN venue v ON e.venueid = v.venueid
            JOIN artist a ON e.artistid = a.artistid
            WHERE e.idevent = %s;
        """, (event_id,))  # Use parameterized query to prevent SQL injection
        
        # Fetch the event
        event = cur.fetchone()
        # Clean up database resources
        cur.close()
        conn.close()
        
        # Return 404 if event not found
        if not event:
            return jsonify({
                'status': 'error',
                'message': 'Event not found'
            }), 404
        
        # Return success response with event data    
        return jsonify({
            'status': 'success',
            'event': event
        })
        
    except Exception as e:
        # Handle any database or processing errors
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# Run the application in debug mode if executed directly
if __name__ == '__main__':
    app.run(debug=True)
