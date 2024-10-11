# SQL Design
## Tables:

### Table: User

#### Table Description
TBD

#### Attributes and Description
- idUser (Integer, Primary Key, Auto Increment)
- UserName (String, Not Null, Unique)
- Name (String, Not Null)
- Role (String, Not Null): Must be one of the predefined roles ('Fan', 'Artist', 'Planner').
- Location (String, Nullable)

#### Tests
TBD


### Table: Venue

#### Table Description
TBD

#### Attributes and Description
- idVenue (Integer, Primary Key, Auto Increment)
- Name (String, Not Null)
- Location (String, Nullable)
- Description (String, Nullable)

#### Tests
TBD

### Table: Event
#### Table Description
TBD

#### Attributes and Description
- idEvent (Integer, Primary Key, Auto Increment)
- Name (String, Not Null)
- DateTime (DateTime, Not Null)
- Description (Text, Nullable)
- Artist (String or Foreign Key)
- VenueID (Integer, Foreign Key to Venue.idVenue, Not Null)
- Planner (Integer, Foreign Key to User.idUser, Not Null)

#### Tests
TBD



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
Description: Add event to the database
Input: Event details
Returns: Add event to Event table in the database
Tests: make sure ArtistID and PlannerID exist in the database, and all fields are not null.
Location: TBD

### GetEvent(idEvent):
Description: Retreive event details
Input: idEvent
Return: Event Details
Tests: idEvent is valid
Location: Per event page

### AddUser(UserName, Name, Role, Location):
Description: Add a new user to the website
Input: User details
Returns: Add user to User table in the database
Tests: All fields available. UserName is not duplicate
Location: Main Users page

### GetUser(UserName):
Description: Retrieve information from UserName. Helpful in the user page
Input: UserName
Return: User details
Tests: Username is available
Location: per user page

### AddAnnoucement(EventID, Title, DateTime, userID, Note):
Description: Add announcement
Input: User details
Returns: Add user to User table in the database
Tests: Make sure all fields are not null. Also, EventID and userID are available.

#### GetAnnoucementByEvent(EventID):
Description: Receive all announcements for a single event
Input: EventID
Returns: All announcements for this event

### GetUpcomingEventsByArtist:
Location: Artist Page

### GetUpcomingEventsByPlanner:
Location: Planner Page


### GetAllUpcomingEvents:
Location: Home page

### AddVenue(.....):
#### GetVenue(......):

