# SQL Design
## Tables:

### Table: User

#### Table Description
The User table stores information about all users of the system, including fans, artists, and event planners.


#### Attributes and Description
- idUser (Integer, Primary Key, Auto Increment): Unique identifier for each user
- UserName (String, Not Null, Unique): User's chosen username for login
- Name (String, Not Null): User's full name
- Role (String, Not Null): Must be one of the predefined roles ('Fan', 'Artist', 'Planner').
- Location (String, Nullable): User's location

#### Tests
1. Test: Insert Valid User
   - Description: Verify that a new user can be successfully inserted with all required fields
   - Test steps:
     1. Insert a new user with valid data for all fields
     2. Retrieve the inserted user
   - Expected result: User is successfully inserted and can be retrieved
   - Actual result: New user is present in the User table with correct information
   - Status: Pass/Fail

2. Test: Enforce Unique UserName
   - Description: Verify that the UserName must be unique
   - Test steps:
     1. Insert a user with a UserName
     2. Attempt to insert another user with the same UserName
   - Expected result: Second insert operation fails due to unique constraint violation
   - Actual result: Database returns an error indicating unique constraint violation
   - Status: Pass/Fail

3. Test: Enforce Valid Role
   - Description: Verify that the Role must be one of the predefined roles
   - Test steps:
     1. Attempt to insert a user with an invalid Role
   - Expected result: Insert operation fails due to check constraint violation
   - Actual result: Database returns an error indicating check constraint violation
   - Status: Pass/Fail


### Table: Venue

#### Table Description

#### Attributes and Description
- idVenue (Integer, Primary Key, Auto Increment)
- Name (String, Not Null)
- Location (String, Nullable)
- Description (String, Nullable)

#### Tests
TBD

### Table: Event
#### Table Description
The Event table stores information about music events, including their name, date and time, description, and associated venue and planner.


#### Attributes and Description
- idEvent (Integer, Primary Key, Auto Increment): Unique identifier for each event
- Name (String, Not Null): The name of the event
- DateTime (DateTime, Not Null): The date and time when the event takes place
- Description (Text, Nullable): A detailed description of the event
- Artist (String or Foreign Key): The artist performing at the event
- VenueID (Integer, Foreign Key to Venue.idVenue, Not Null): The venue where the event takes place
- Planner (Integer, Foreign Key to User.idUser, Not Null): The user who planned the event

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
   - Description: Verify that foreign key constraints are enforced for VenueID and Planner
   - Test steps:
     1. Attempt to insert an event with non-existent VenueID
     2. Attempt to insert an event with non-existent Planner
   - Expected result: Insert operations fail due to foreign key constraint violations
   - Actual result: Database returns errors indicating foreign key constraint violations
   - Status: Pass/Fail



### Table: Announcement
#### Table Description
TBD

#### Attributes and Description
- idAnnouncement (Integer, Primary Key, Auto Increment)
- EventID (Integer, Foreign Key to Event.idEvent, Not Null):
- Title (String, Not Null)
- DateTime (DateTime, Not Null)
- userID (Integer, Foreign Key to User.idUser, Not Null):
- Note (Text, Not Null)

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

