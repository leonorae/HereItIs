# Page Testing Documentation

## 1. Home Page (Events)

### Page Title
HereItIs (Upcoming Events)

### Page Description
The Home page serves as the main landing page for the application, displaying upcoming events and allowing users to navigate to other sections of the site. It shows links to the upcoming events in chronological order, each with a poster image, name, and list of artists performing (further details are included in the event's details page). Also contains a mechanism for filtering events by a genre.

TODO finish and insert mockup

### Parameters needed for the page
- Current date (for filtering upcoming events)

### Data needed to render the page
- Names of upcoming events
- Artists performing at upcoming events
- Dates and times of upcoming events
- Images for upcoming events
- Featured artists (if any)

### Link destinations for the page
- Event details pages (per displayed event)
- Artist profile pages (per displayed event)
- All Artists page
- Get Listed (Add Event, Add Artist)
- About Page
- Featured artist

### List of tests for verifying the rendering of the page
1. Test: Verify upcoming events display
   - Ensure the page loads with a list of upcoming events
   - Check that events are sorted by date
   - Confirm that only future events are displayed

2. Test: Filtering events by genre
   - Confirm that filtering events by genre displays only correct events

4. Test: Navigation functionality
   - Ensure navigation links (about page, event details links, artist profile links, all artists page) are working and lead to correct pages

5. Test: Responsive design
   - Check that the page layout adjusts appropriately for various page sizes (desktop, tablet, and mobile views)

## 2. Event Page

### Page Title
[Event Name] @ [Venue Name]

### Page Description
This page displays detailed information about a specific event, including the artists performing, venue location, date, time, ticket information, and a description.

TODO finish and insert mockup

### Parameters needed for the page
- Event ID

### Data needed to render the page
- Event name
- Venue name and address
- Date and time
- List of Artists performing
- Pricing and availability of tickets
- Description
- Poster image

### Link destinations for the page
- Artist pages (artists performing at event)
- Back to home

### List of tests for verifying the rendering of the page
1. Test: Event information display
   - Verify all event details (name, venue, date/time, artists, pricing/availability, description, poster image) are correctly displayed
   - Ensure the page title includes the correct event and venue name

3. Test: Artist and venue links
   - Check that links to artist pages are present and functional

4. Test: Ticket information
   - Confirm ticket availability and pricing information is accurate

5. Test: Dynamic content loading
   - Ensure the page loads correctly with different event IDs, returns an appropriate error page for nonexistent event

6. Test: Responsive design
   - Check that the page layout adjusts appropriately for various page sizes (desktop, tablet, and mobile views)

## 3. Artist Profile Page

### Page Title
Artist Profile: [Artist Name]

### Page Description
This page showcases information about a specific artist, including their image, bio, social media links, an embedded example of their work (video or audio), upcoming events, and past performances.

TODO add mockup

### Parameters needed for the page
- Artist ID

### Data needed to render the page
- Artist Name
- Artist Image (cropped to specific size)
- Artist Bio (plaintext)
- Social media links (Instagram, Facebook, Soundcloud, Bandcamp)
- Embeddable media link (youtube/soundcloud/bandcamp)
- Next 3 upcoming events for the artist
- Past 3 performances by the artist

### Link destinations for the page
- Event details pages for upcoming events
- Event details pages for previous events
- Social media profiles

### List of tests for verifying the rendering of the page
1. Test: Artist information display
   - Verify artist name, bio, image, and social links, are correctly displayed
   - Ensure the page title includes the artist name

3. Test: Music samples
   - If available, test the functionality of music sample players or video embeds

4. Test: Upcoming events list
   - Check that upcoming events are listed and sorted by date
   - Verify links to event details pages are functional

5. Test: Dynamic content loading
   - Ensure the page loads correctly with different artist IDs, returns an appropriate error page for nonexistent artist
  
6. Test: Responsive design
   - Check that the page layout adjusts appropriately for various page sizes (desktop, tablet, and mobile views)

## 4. Add Event:

### Page Title
Add Event: 

### Page Description
This page allows the user to create a new event page and will prompt for event details. Will have relevant text-boxes and selectors for adding values to each required field. Will link to the newly created event when user inputs correct data into all fields and confirms input.

### Data needed to render the page
- Current date/time (for checking that the new event will be after the current date)

### Link destinations for the page
- links back to homepage (either submitting or canceling)
- link to add artist page

### List of tests for verifying the rendering of the page
1. Test: Forms display correct fields:
   - Ensure correct fields for data entry, with required fields appropriately marked
   - Ensure user is able to enter data of correct type for new event into the correct question forms

2. Test: Attempt complete message after new data entry
   - If valid data is supplied in each required form, display a "successful event creation" message

3. Test: Correct link to the destination pages
   - Ensure link back to home page works correctly
   - Ensure a link to the newly created event is displayed after user submits correct information

5. Test: Verify input type and constraints
   - Ensure input of incorrect data type into an entry form is either impossible or displays an error to the user

6. Test: Responsive design
   - Check that the page layout adjusts appropriately for various page sizes (desktop, tablet, and mobile views)
  
## 5. Add artist:
### Page Title
Add New Artist: 

### Page Description
Similarly to the Add Event page, this page allows the user to create a new artist page and will includes text-boxes and selectors for each required field.

### Data needed to render the page
- User details (username, name, email, location)

### Link destinations for the page
- links back to homepage (either submitting or cancelling)
- link to add event page

### List of tests for verifying the rendering of the page
1. Test: Forms display correct fields:
   - Ensure correct fields for data entry, with required fields appropriately marked
   - Ensure user is able to enter data of correct type for new event into the correct question forms

2. Test: Attempt complete message after new data entry
   - If valid data supplied in each required form, display a "successful artist creation" message

3. Test: Correct link to the destination pages
   - Ensure link back to list of artists page works correctly
   - Ensure a link to the newly created artist is displayed after user submits correct information

5. Test: Verify input type and constraints
   - Ensure input of incorrect data type into an entry form is either impossible or displays an error to the user

6. Test: Responsive design
   - Check that the page layout adjusts appropriately for various page sizes (desktop, tablet, and mobile views)


## 6. List of artists:
### Page Title
Artists

### Page Description
Displays the artists who have created pages on the website in alphabetical order and links to their pages. Allows users to filter the artists by genre.

### Data needed to render the page
- All artist names, photos, and genres.

### Link destinations for the page
- Link to each displayed artist's page
- back to home

### List of tests for verifying the rendering of the page
1. Test: Artist List Display
   - Ensure all artists display correctly and are sorted alphabetically

2. Test: Filtering artists by genre
   - Confirm that filtering events by genre displays only the correct artists

3. Test: Destination Links
   - Correct links to destination pages: artist profiles, home page, add new artist page

## 7. About Page:
### Page Title
About HereItIs

### Page Description
A simple about page, with a description of what the app is and how to use it.

### Data needed to render the page
- Description of application, instructions for usage for new users

### Link destinations for the page
- back to home

### List of tests for verifying the rendering of the page
1. Test: Correct information displayed
   - Ensure correct description is displayed and any images used are rendered properly
  
2. Test: Correct link to the destination pages
   - Ensure link back to home works correctly

3. Test: Responsive design
   - Check that the page layout adjusts appropriately for various page sizes (desktop, tablet, and mobile views)
