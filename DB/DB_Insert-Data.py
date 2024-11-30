import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect("postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a.oregon-postgres.render.com/mohammed_db")
print("Database Connection Successful")
cur = conn.cursor()


# Insert sample data
try:
    # Insert into Artist
    cur.execute('''
        INSERT INTO Artist (ArtistUserName, Name, Bio, ImageURL, Location)
        VALUES ('artist1', 'Artist One', 'A sample bio', 'http://image.url', 'New York')
        RETURNING ArtistID;
    ''')
    artist_id = cur.fetchone()[0]

    # Insert into Venue
    cur.execute('''
        INSERT INTO Venue (Name, Location, Description)
        VALUES ('Venue One', 'Los Angeles', 'A popular concert venue')
        RETURNING VenueID;
    ''')
    venue_id = cur.fetchone()[0]

    # Insert into Event 1
    cur.execute('''
        INSERT INTO Event (Name, DateTime, Description, ArtistID, VenueID, TicketPrice)
        VALUES ('Concert One', '2025-01-01 19:00:00', 'New Year concert', %s, %s, 49.99)
        RETURNING idEvent;
    ''', (artist_id, venue_id))
    event_id1 = cur.fetchone()[0]

     # Insert into Event 2
    cur.execute('''
        INSERT INTO Event (Name, DateTime, Description, ArtistID, VenueID, TicketPrice)
        VALUES ('Concert Two', '2025-01-01 19:00:00', 'New Year concert 2', %s, %s, 49.99)
        RETURNING idEvent;
    ''', (artist_id, venue_id))
    event_id2 = cur.fetchone()[0]


    # Commit sample data insertion
    conn.commit()
    print("Sample data inserted successfully.")

    # Retrieve and verify sample data
    cur.execute('SELECT * FROM Artist WHERE ArtistID = %s;', (artist_id,))
    print("Artist Record:", cur.fetchone())

    cur.execute('SELECT * FROM Venue WHERE VenueID = %s;', (venue_id,))
    print("Venue Record:", cur.fetchone())

    cur.execute('SELECT * FROM Event WHERE idEvent = %s;', (event_id1,))
    print("Event Record 1:", cur.fetchone())

    cur.execute('SELECT * FROM Event WHERE idEvent = %s;', (event_id2,))
    print("Event Record 2:", cur.fetchone())



except Exception as e:
    print("An error occurred during insertion, retrieval, or deletion:", e)
    conn.rollback()
