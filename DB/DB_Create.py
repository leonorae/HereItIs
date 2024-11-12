import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect("postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a.oregon-postgres.render.com/mohammed_db")
print("Database Connection Successful")
cur = conn.cursor()

# Create Artist table
cur.execute('''
    CREATE TABLE IF NOT EXISTS Artist (
        ArtistID SERIAL PRIMARY KEY,
        ArtistUserName VARCHAR(255) NOT NULL UNIQUE,
        Name VARCHAR(255) NOT NULL,
        Bio TEXT,
        ImageURL VARCHAR(255),
        Location VARCHAR(255),
        FacebookURL VARCHAR(255),
        InstagramURL VARCHAR(255),
        SoundCloudURL VARCHAR(255)
    );
''')

# Create Venue table
cur.execute('''
    CREATE TABLE IF NOT EXISTS Venue (
        VenueID SERIAL PRIMARY KEY,
        Name VARCHAR(255) NOT NULL UNIQUE,
        Location VARCHAR(255),
        Description VARCHAR(255)
    );
''')

# Create Event table with foreign keys referencing Artist and Venue tables
cur.execute('''
    CREATE TABLE IF NOT EXISTS Event (
        idEvent SERIAL PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        DateTime TIMESTAMP NOT NULL,
        Description TEXT,
        ArtistID INT NOT NULL,
        PosterURL VARCHAR(255),
        VenueID INT NOT NULL,
        TicketPrice DECIMAL(8,2),
        CONSTRAINT fk_artist
            FOREIGN KEY(ArtistID) 
            REFERENCES Artist(ArtistID)
            ON DELETE CASCADE,
        CONSTRAINT fk_venue
            FOREIGN KEY(VenueID)
            REFERENCES Venue(VenueID)
            ON DELETE CASCADE
    );
''')

# Commit table creation
conn.commit()

# Verify tables exist
tables = ['Artist', 'Venue', 'Event']
for table in tables:
    cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name='{table.lower()}');")
    exists = cur.fetchone()[0]
    print(f"Table '{table}' exists: {exists}")

# Insert sample data for verification
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

    # Insert into Event
    cur.execute('''
        INSERT INTO Event (Name, DateTime, Description, ArtistID, VenueID, TicketPrice)
        VALUES ('Concert One', '2025-01-01 19:00:00', 'New Year concert', %s, %s, 49.99)
        RETURNING idEvent;
    ''', (artist_id, venue_id))
    event_id = cur.fetchone()[0]

    # Commit sample data insertion
    conn.commit()
    print("Sample data inserted successfully.")

    # Retrieve and verify sample data
    cur.execute('SELECT * FROM Artist WHERE ArtistID = %s;', (artist_id,))
    print("Artist Record:", cur.fetchone())

    cur.execute('SELECT * FROM Venue WHERE VenueID = %s;', (venue_id,))
    print("Venue Record:", cur.fetchone())

    cur.execute('SELECT * FROM Event WHERE idEvent = %s;', (event_id,))
    print("Event Record:", cur.fetchone())

    # Delete sample data after verification
    cur.execute('DELETE FROM Event WHERE idEvent = %s;', (event_id,))
    cur.execute('DELETE FROM Venue WHERE VenueID = %s;', (venue_id,))
    cur.execute('DELETE FROM Artist WHERE ArtistID = %s;', (artist_id,))
    conn.commit()
    print("Sample data deleted successfully after testing.")

except Exception as e:
    print("An error occurred during insertion, retrieval, or deletion:", e)
    conn.rollback()

# Close the cursor and connection
cur.close()
conn.close()
