# Page Testing Documentation

## 1. Home Page

### Page Title
Home

### Page Description
The Home page serves as the main landing page for the application, displaying upcoming events and allowing users to navigate to other sections of the site.

[Insert mockup or hand-drawn image here]


### Parameters needed for the page
- Current date (for filtering upcoming events)

### Data needed to render the page
- List of upcoming events (limited to next 10)
- Featured artists (if any)
- User's location (for event recommendations) <!-- Might be difficult to implement first time MA -->

### Link destinations for the page
- Event details pages
- Artist profile pages
- Search/Filter events page <!-- Might not be needed, MA -->
- static "about page"

### List of tests for verifying the rendering of the page
1. Test: Verify upcoming events display
   - Ensure the page loads with a list of upcoming events
   - Check that events are sorted by date
   - Confirm that only future events are displayed

2. Test: Responsive design
   - Check that the page layout adjusts appropriately for desktop, tablet, and mobile views

3. Test: Navigation functionality
   - Ensure all navigation links are working and lead to correct pages

4. Test: Event recommendations <!-- Might not be needed, MA -->
   - Verify that event recommendations are displayed based on user's location (if available)

## 2. Event Page

### Page Title
Event Details: [Event Name]

### Page Description
This page displays detailed information about a specific event, including the artist, venue, date, time, and ticket information.

[Insert mockup or hand-drawn image here]

### Parameters needed for the page
- Event ID

### Data needed to render the page
- Event details (name, date, time, description)
- List of Artists
- Artist information

### Link destinations for the page
- Artist profile page
- Venue details page <!-- we don't have web pages for venues, so might skip this? MA -->
- List of Artists
  



### List of tests for verifying the rendering of the page
1. Test: Event information display
   - Verify all event details are correctly displayed
   - Ensure the page title includes the event name

2. Test: Artist and venue links
   - Check that links to artist and venue pages are present and functional

3. Test: Ticket information
   - Confirm ticket availability and pricing information is accurate
   - Test the link to ticket purchase page

4. Test: Dynamic content loading
   - Ensure the page loads correctly with different event IDs

## 3. Artist Profile Page

### Page Title
Artist Profile: [Artist Name]

### Page Description
This page showcases information about a specific artist, including their bio, upcoming events, and past performances.

[Insert mockup or hand-drawn image here]

### Parameters needed for the page
- Artist ID

### Data needed to render the page
- Artist details (name, bio, image)
- List of upcoming events for the artist
- Past performances
- Social media links

### Link destinations for the page
- Event details pages for upcoming events
- Social media profiles
- Music samples or videos (if available)

### List of tests for verifying the rendering of the page
1. Test: Artist information display
   - Verify artist name, bio, and image are correctly displayed
   - Ensure the page title includes the artist name

2. Test: Upcoming events list
   - Check that upcoming events are listed and sorted by date
   - Verify links to event details pages are functional

3. Test: Music samples <!-- might no be needed? MA -->
   - If available, test the functionality of music sample players or video embeds

4. Test: Dynamic content loading
   - Ensure the page loads correctly with different artist IDs

## 4. Add Event:


### Page Title
Add Event 

### Page Description
This page allows the user to create a new event and will prompt for event details. 

[Insert mockup or hand-drawn image here]


### Data needed to render the page
- User details (username, name, email, location)


### Link destinations for the page
- link back to homepage
- link to event page 
  

### List of tests for verifying the rendering of the page
1. Test: 


## 5. Add artist:
### Page Title
Add Artist: 

### Page Description
This page allows the user to create a new artist and will prompt for artist details. 

[Insert mockup or hand-drawn image here]


### Data needed to render the page
- Webform requesting artist details
- Artist details (name, type, etc.)


### Link destinations for the page
- Link back to homepage
- List of artist
  

### List of tests for verifying the rendering of the page
1. Form with correct questions
   - User able to add new artist with correct form
2. Attempt complete message after new data entry
3. Correct link to the destination page


## 6. List of artist:

