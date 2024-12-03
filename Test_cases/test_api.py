"""
test_api.py: Test file for API endpoints in app.py
Purpose: Verify the functionality of all API endpoints including Artist, Venue, and Event operations
Author: Wizard Team 
"""

import unittest
import json
from app.app import app, get_db_connection
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, timedelta

class TestAPI(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Verify database connection before running any tests."""
        try:
            # Use get_db_function from Flask app
            conn = get_db_connection()
            if conn is None:
                raise unittest.SkipTest("Could not connect to database")
            conn.close()
        except Exception as e:
            raise unittest.SkipTest(f"Could not connect to database: {e}")

    def setUp(self):
        """Create and initialize test environment before each test."""
        # Initialize Flask test client
        self.app = app
        self.client = self.app.test_client()
        
        # Test data for Artist API tests
        self.test_artist = {
            "ArtistUserName": "testartist",
            "Name": "Test Artist",
            "Bio": "Test bio",
            "ImageURL": "http://test.com/image.jpg",
            "Location": "Test Location",
            "FacebookURL": "http://facebook.com/test",
            "InstagramURL": "http://instagram.com/test",
            "SoundCloudURL": "http://soundcloud.com/test"
        }
        
        # Test data for Venue API tests
        self.test_venue = {
            "Name": "Test Venue",
            "Location": "Test Location",
            "Description": "Test Description"
        }
        
        # Test data for Event API tests
        self.test_event = {
            "Name": "Test Event",
            "DateTime": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "Description": "Test Description",
            "PosterURL": "http://test.com/poster.jpg",
            "TicketPrice": 25.00
        }

    def tearDown(self):
        """Delete test data after each test."""
        try:
            # Connect to db
            conn = get_db_connection()
            if conn:
                cur = conn.cursor()
                # Clean up any test data created during tests
                cur.execute("DELETE FROM Event WHERE Name = 'Test Event'")
                cur.execute("DELETE FROM Artist WHERE ArtistUserName = 'testartist'")
                cur.execute("DELETE FROM Venue WHERE Name = 'Test Venue' OR Name = 'Minimal Test Venue'")
                conn.commit()
                cur.close()
                conn.close()
        except Exception as e:
            print(f"Error in tearDown: {e}")

    def test_add_valid_artist(self):
        """Verify that a new artist can be successfully inserted with all required fields."""
        # Convert test_artist to JSON and send POST request
        response = self.client.post(
            '/api/artist',
            data=json.dumps(self.test_artist),
            content_type='application/json'
        )

        # Code 201 = successful creation of resource
        self.assertEqual(response.status_code, 201)

        # Parse the JSON response back into a Python dictionary
        data = json.loads(response.data)

        # Verify 'ArtistID' key exists in response
        self.assertIn('ArtistID', data)
        
        # Verify artist was added correctly to database
        conn = get_db_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Artist WHERE ArtistUserName = %s", 
                       (self.test_artist["ArtistUserName"],))
            artist = cur.fetchone()
            cur.close()
            conn.close()
            
            # Verify artist exists and username matches
            self.assertIsNotNone(artist)
            self.assertEqual(artist["artistusername"], self.test_artist["ArtistUserName"])

    def test_add_duplicate_artist_username(self):
        """Verify that the ArtistUserName must be unique."""
        # Initial artist insertion
        self.client.post(
            '/api/artist',
            data=json.dumps(self.test_artist),
            content_type='application/json'
        )
        
        # Attempt duplicate insertion - should fail
        response = self.client.post(
            '/api/artist',
            data=json.dumps(self.test_artist),
            content_type='application/json'
        )
        
        # Expect 400 for duplicate username
        self.assertEqual(response.status_code, 400)


    def test_add_artist_missing_required_fields(self):
        """Verify that all non-null attributes are required."""
        # Create invalid artist
        invalid_artist = {
            "Bio": "Test bio",
            "Location": "Test Location"
        }
        
        # Attempt to add invalid artist - should fail 
        response = self.client.post(
            '/api/artist',
            data=json.dumps(invalid_artist),
            content_type='application/json'
        )
        
        # Expect 400 
        self.assertEqual(response.status_code, 400)

    def test_add_valid_venue(self):
        """Verify that a new venue can be successfully inserted with all required fields."""
        # Attempt to add valid venue with all required fields
        response = self.client.post(
            '/api/venue',
            data=json.dumps(self.test_venue),
            content_type='application/json'
        )
        
        # 201 = successful creation
        self.assertEqual(response.status_code, 201)
        
        # Parse response and verify VenueID was returned
        data = json.loads(response.data)
        self.assertIn('VenueID', data)

    def test_add_venue_missing_required_fields(self):
        """Verify that all non-null attributes are required."""
        # Create venue missing required Name field
        invalid_venue = {
            "Location": "Test Location",
            "Description": "Test Description"
        }
        
        # Attempt to add invalid venue - should fail
        response = self.client.post(
            '/api/venue',
            data=json.dumps(invalid_venue),
            content_type='application/json'
        )
        
        # Expect 400 
        self.assertEqual(response.status_code, 400)

    def test_add_venue_null_location_description(self):
        """Verify that a venue can be inserted with null location and description."""
        # Create venue with only name field
        minimal_venue = {
            "Name": "Minimal Test Venue"
        }
        
        # Attempt to add minimal venue - should succeed
        response = self.client.post(
            '/api/venue',
            data=json.dumps(minimal_venue),
            content_type='application/json'
        )
        
        # Expect 201 
        self.assertEqual(response.status_code, 201)

    def test_add_valid_event(self):
        """Verify that a new event can be successfully inserted with all required fields."""
        artist_response = self.client.post(
            '/api/artist',
            data=json.dumps(self.test_artist),
            content_type='application/json'
        )
        artist_data = json.loads(artist_response.data)
        
        # Create venue and get VenueID
        venue_response = self.client.post(
            '/api/venue',
            data=json.dumps(self.test_venue),
            content_type='application/json'
        )
        venue_data = json.loads(venue_response.data)
        
        # Set foreign key references in event data
        self.test_event["ArtistID"] = artist_data["ArtistID"]
        self.test_event["VenueID"] = venue_data["VenueID"]
        
        # Attempt to create event with all required fields
        response = self.client.post(
            '/api/event',
            data=json.dumps(self.test_event),
            content_type='application/json'
        )
        
        # Expect 201, successful creation
        self.assertEqual(response.status_code, 201)

    def test_add_event_invalid_foreign_keys(self):
        """Verify that foreign key constraints are enforced."""
        # Set non-existent foreign key IDs 
        self.test_event["ArtistID"] = 99999  
        self.test_event["VenueID"] = 99999   
        
        # Attempt to create event w/ invalid FK
        response = self.client.post(
            '/api/event',
            data=json.dumps(self.test_event),
            content_type='application/json'
        )
        
        # Expect 400 
        self.assertEqual(response.status_code, 400)

    def test_add_event_invalid_datetime(self):
        """Verify Date and Time are valid entries."""
        # Set an invalid datetime
        self.test_event["DateTime"] = "2024-13-32 25:00:00"
        
        # Attempt to create event with invalid datetime
        response = self.client.post(
            '/api/event',
            data=json.dumps(self.test_event),
            content_type='application/json'
        )
        
        # Expect 400 
        self.assertEqual(response.status_code, 400)

    def test_add_event_past_date(self):
        """Verify that new events cannot be in the past."""
        # Set date to yesterday
        self.test_event["DateTime"] = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        
        # Attempt to create event with past date
        response = self.client.post(
            '/api/event',
            data=json.dumps(self.test_event),
            content_type='application/json'
        )
        
        # Expect 400 
        self.assertEqual(response.status_code, 400)

    def test_get_upcoming_events(self):
        """Test retrieving upcoming events."""
        # Get all upcoming events from API
        response = self.client.get('/api/events')
        
        # Verify successful retrieval
        self.assertEqual(response.status_code, 200)
        
        # Parse response data
        data = json.loads(response.data)
        
        # Verify response is a list of events
        self.assertTrue(isinstance(data, list))

    def test_get_event_details(self):
        """Test retrieving specific event details."""
        # Create records for event
        artist_response = self.client.post('/api/artist', data=json.dumps(self.test_artist), content_type='application/json')
        venue_response = self.client.post('/api/venue', data=json.dumps(self.test_venue), content_type='application/json')
        
        # Set FK references 
        self.test_event["ArtistID"] = json.loads(artist_response.data)["ArtistID"]
        self.test_event["VenueID"] = json.loads(venue_response.data)["VenueID"]
        
        # Create test event and get its ID
        event_response = self.client.post('/api/event', data=json.dumps(self.test_event), content_type='application/json')
        event_data = json.loads(event_response.data)
        
        # Retrieve event details
        response = self.client.get(f'/api/events/{event_data["EventID"]}')
        self.assertEqual(response.status_code, 200)
        
        # Verify returned event matches created event
        data = json.loads(response.data)
        self.assertEqual(data["name"], self.test_event["Name"])

    def test_get_nonexistent_event(self):
        """Test retrieving details for non-existent event."""
        # Attempt to get event with invalid ID 
        response = self.client.get('/api/events/99999')
        
        # Expect 404
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    # Load all tests from TestAPI class
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAPI)
    # Run tests with verbose output
    result = unittest.TextTestRunner(verbosity=2).run(suite)