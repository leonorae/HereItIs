# SQL Design
## Tables:

### Table: Artist

#### Table Description
The artist table stores information about all artists in the system.


#### Attributes and Description
- ArtistID(INT, Primary Key, Auto Increment)
- ArtistUserName (String, Not Null, Unique): User's chosen username for login
- Name (String, Not Null): User's full name
- Bio (TEXT, Nullable)
- ImageURL (VARCHAR(255), Nullable)
- Location (String, Nullable): User's location

#### Tests
1. Test: Insert Valid Artist
   - Description: Verify that a new artist can be successfully inserted with all required fields
   - Test steps:
     1. Insert a new artist with valid data for all fields
     2. Retrieve the inserted user
   - Expected result: User is successfully inserted and can be retrieved
   - Actual result: New artist is present in the artist table with correct information
   - Status: Pass/Fail

2. Test: Enforce Unique ArtistUserName
   - Description: Verify that the ArtistUserName must be unique
   - Test steps:
     1. Insert a user with a ArtistUserName
     2. Attempt to insert another user with the same ArtistUserName
   - Expected result: Second insert operation fails due to unique constraint violation
   - Actual result: Database returns an error indicating unique constraint violation
   - Status: Pass/Fail
     
3. Test: Check all valid attributes are available
   - Description: Verify that the all non-null attributes are inserted
   - Test steps:
     1. Insert a artist with missing Name
   - Expected result: Artist will not be added
   - Actual result: An error message is printed, and the artist is not added.
   - Status: Pass/Fail


### Table: Venue

#### Table Description

#### Attributes and Description
- VenueID (INT, Primary Key, Auto Increment)
- Name (String, Not Null)
- Location (String, Nullable)
- Description (String, Nullable)

#### Tests
1. Test: Insert Valid Venue
   - Description: Verify that a new venue can be successfully inserted with all required fields
   - Test steps:
     1. Insert a new venue with valid data for all fields
     2. Retrieve the inserted venue
   - Expected result: Venue is successfully inserted and can be retrieved
   - Actual result: New venue is present in the User table with correct information
   - Status: Pass/Fail

2. Test: Check all valid attributes are available
   - Description: Verify that the all non-null attributes are inserted
   - Test steps:
     1. Insert a venue with missing fields
   - Expected result: Venue will not be added to the table
   - Actual result: An error message is printed, and the artist is not added.
   - Status: Pass/Fail
     
3. Test: Enforce Unique Name
   - Description: Verify that the venue name is unique to prevent duplicate entries.
   - Test steps:
     1. Insert a venue with a specific name.
     2. Attempt to insert another venue with the same name.
   - Expected result: Second insert operation fails due to unique constraint violation.
   - Actual result: Error message is printed
   - Status: Pass/Fail
  
4. Test: Handle Null Location and Description
   - Description: Verify that a venue can be inserted without a location or description.
   - Test steps:
     1. Insert a venue with only the name provided.
   - Expected result: Insert fails due missing attribute
   - Actual result: Error message is printed
   - Status: Pass/Fail
  


### Table: Event
#### Table Description
The Event table stores information about music events, including their name, date and time, description, and associated venue and planner.


#### Attributes and Description
- idEvent (Integer, Primary Key, Auto Increment): Unique identifier for each event
- Name (String, Not Null): The name of the event
- DateTime (DateTime, Not Null): The date and time when the event takes place
- Description (Text, Nullable): A detailed description of the event
- ArtistID (String, Foreign Key to Artist.ArtistID): The artist performing at the event
- PosterURL	(VARCHAR(255), Nullable)
- VenueID (Integer, Foreign Key to Venue.VenueID, Not Null): The venue where the event takes place
- TicketPrice (DECIMAL(8,2), Nullable )

#### Tests
1. Test: Insert Valid Event
   - Description: Verify that a new event can be successfully inserted with all required fields
   - Pre-conditions: Venue and User (Planner) exist in their respective tables
   - Test steps:
     1. Insert a new event with valid data for all fields
     2. Retrieve the inserted event
   - Expected result: Event is successfully inserted and can be retrieved
   - Actual result: New event is present in the Event table with correct information
   - Status: Pass/Fail

2. Test: Enforce Foreign Key Constraints
   - Description: Verify that foreign key constraints are enforced for ArtistUserName and VenueName
   - Test steps:
     1. Attempt to insert an event with non-existent ArtistUserName
     2. Attempt to insert an event with non-existent VenueName
   - Expected result: Insert operations fail due to foreign key constraint violations
   - Actual result: Database returns errors indicating foreign key constraint violations
   - Status: Pass/Fail
  
3. Test: Valid DateTime
   - Description: Verify Date and Time are valid entries
   - Test steps:
     1. Attempt to insert an event with time hour 25:00
     2. Attempt to insert an event on December 32
   - Expected result: Insert operations fail due to DateTime constraints
   - Actual result: Database returns errors
   - Status: Pass/Fail
  
4. Test: New events cannot be in the past
   - Description: Verify that the Date and Time of new events are not in the past
   - Test steps:
     1. Attempt to insert an event with a date already passed
   - Expected result: Insert operations fail due to DateTime constraints
   - Actual result: Database returns errors
   - Status: Pass/Fail


## Use Cases for Data Access Methods
### GetAllUpcomingEvents
- Description: Retrieves all upcoming events (those with a future date) along with their associated venues.
- Parameters: None
- Returns: EventID, Name, DateTime, PosterURL, VenueName
- List of tests for verifying each access method:
  1. Valid Upcoming Events
     - Description: Ensure that only events with a future date are returned.
     - Steps: Insert an event dated today and check if it available next day.
     - Expected Results: Event should not show
  2. No Upcoming Events
      - Description: Verify behavior when no upcoming events exist.
      - Steps: Delete all events
      - Expected Results: No events available
  3. Proper Ordering by Date
      - Description: Ensure events are sorted in ascending order by date.
      - Steps: insert multiple events not in data order
      - Expected Results: Events are ordered by date

### AddEvent
- Description: Add event to the database with all relevant details
- Parameters: Event details, DateTime, Description, PosterURL, VenueID, TicketPrice, ArtistIDs
- Returns: If success, add to database and Returns the EventID otherwise error message
- List of tests for verifying each access method:
  1. Insert Valid Event
     - Description: Ensure an event is correctly inserted with all valid data.
     - Steps: Insert an event with all required fields.
     - Expected Results: Event is successfully inserted and retrievable.
  2. Insert Event with Missing Data
      - Description: 
      - Steps:
      - Expected Results: 
  3. Invalid VenueID Handling
      - Description: 
      - Steps: 
      - Expected Results:


### GetEventDetails
- Description: Retrieves detailed information about a specific event, including venue and associated artists.
- Parameters: EventID
- Return: Name, DateTime, Description, PosterURL, VenueName, Location, TicketPrice, ArtistIDs
- List of tests for verifying each access method:
  1. Valid Event ID
     - Description: 
     - Steps: 
     - Expected Results: 
  2. TBD
      - Description: 
      - Steps:
      - Expected Results: 
  3. TBD
      - Description: 
      - Steps: 
      - Expected Results:
        
### AddArtist
- Description: Inserts a new artist into the database with relevant information,
- Parameters: Name, Bio, ImageURL, SocialLinks, Genre
- Returns: If success, add to database and Returns the ArtistID otherwise error message
- List of tests for verifying each access method:
  1. Insert Valid Artist
     - Description: 
     - Steps: 
     - Expected Results: 
  2. Handle Missing Optional Fields
      - Description: 
      - Steps:
      - Expected Results: 
  3. Enforce Unique Artist Name
      - Description: 
      - Steps: 
      - Expected Results:


### GetArtistDetails
- Description: Retrieve information from UserName. Helpful in the user page
- Parameters: ArtistID
- Return: Name, Bio, ImageURL, SocialLinks
- List of tests for verifying each access method:
  1. Valid Artist ID
     - Description: 
     - Steps: 
     - Expected Results: 
  2. TBD
      - Description: 
      - Steps:
      - Expected Results: 
  3. TBD
      - Description: 
      - Steps: 
      - Expected Results:


