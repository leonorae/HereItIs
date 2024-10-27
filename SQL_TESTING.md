# SQL Design
## Tables:

### Table: Artist

#### Table Description
The artist table stores information about all artists in the system.


#### Attributes and Description
- ArtistUserName (String, Primary, Not Null, Unique): User's chosen username for login
- Name (String, Not Null): User's full name
- Role (String, Not Null): Must be one of the predefined roles ('Fan', 'Artist', 'Planner').
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
     1. Insert a artist with missing fields
   - Expected result: Artist will not be added
   - Actual result: An error message is printed, and the artist is not added.
   - Status: Pass/Fail


### Table: Venue

#### Table Description

#### Attributes and Description
- Name (String, Primary Key, Not Null)
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


### Table: Event
#### Table Description
The Event table stores information about music events, including their name, date and time, description, and associated venue and planner.


#### Attributes and Description
- idEvent (Integer, Primary Key, Auto Increment): Unique identifier for each event
- Name (String, Not Null): The name of the event
- DateTime (DateTime, Not Null): The date and time when the event takes place
- Description (Text, Nullable): A detailed description of the event
- ArtistUserName (String, Foreign Key to Artist.ArtistUserName): The artist performing at the event
- VenueName (Integer, Foreign Key to Venue.Name, Not Null): The venue where the event takes place

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


#### Tests
TBD

## Use Cases for Data Access Methods
### AddEvent(Name, DateTime, Description, ArtistID, Venue, PlannerID):
- Description: Add event to the database
- Input: Event details
- Returns: Add event to Event table in the database
- Tests: make sure ArtistID and PlannerID exist in the database, and all fields are not null.
- Location: TBD

### GetEvent(idEvent):
- Description: Retreive event details
- Input: idEvent
- Return: Event Details
- Tests: idEvent is valid
- Location: Per event page

### AddUser(UserName, Name, Role, Location):
- Description: Add a new user to the website
- Input: User details
- Returns: Add user to User table in the database
- Tests: All fields available. UserName is not duplicate
- Location: Main Users page

### GetUser(UserName):
- Description: Retrieve information from UserName. Helpful in the user page
- Input: UserName
- Return: User details
- Tests: Username is available
- Location: per user page

### AddAnnoucement(EventID, Title, DateTime, userID, Note):
- Description: Add announcement
- Input: User details
- Returns: Add user to User table in the database
- Tests: Make sure all fields are not null. Also, EventID and userID are available.

### GetAnnoucementByEvent(EventID):
- Description: Receive all announcements for a single event
- Input: EventID
- Returns: All announcements for this event

### GetUpcomingEventsByArtist:
Location: Artist Page

### GetUpcomingEventsByPlanner:
Location: Planner Page


### GetAllUpcomingEvents:
Location: Home page

### AddVenue(.....):
### GetVenue(......):

