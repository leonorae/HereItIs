# Page Testing Documentation

## 1. Home Page (Events)

### Page Title
HereItIs (Upcoming Events)

### Page Description
The Home page serves as the main landing page for the application, displaying upcoming events and allowing users to navigate to other sections of the site. Shows the next 10 upcoming events, each with a name, venue location, time, price, and list of artists performing.

TODO finish and insert mockup

### Parameters needed for the page
- Current date (for filtering upcoming events)

### Data needed to render the page
- List of upcoming events
- Featured artists (if any) <!--- remove if this space needed for filter dialogs ---!>

### Link destinations for the page
- About Page
- Event details pages (per displayed event)
- Artist profile pages (per displayed event) <!--- maybe not enough space? ---!>
- All Artists page

### List of tests for verifying the rendering of the page
1. Test: Verify upcoming events display
   - Ensure the page loads with a list of upcoming events
   - Check that events are sorted by date
   - Confirm that only future events are displayed

2. Test: Responsive design
   - Check that the page layout adjusts appropriately for desktop, tablet, and mobile views

3. Test: Navigation functionality
   - Ensure all navigation links are working and lead to correct pages

4. Test: Event recommendations
   - Verify that event recommendations are displayed based on user's location (if available)

## 2. Event Page

### Page Title
[Event Name] @ [Venue Name]

### Page Description
This page displays detailed information about a specific event, including the artists performing, venue location, date, time, ticket information, and a description.

TODO finish and insert mockup

### Parameters needed for the page
- Event ID

### Data needed to render the page
- Event details (name, venue, date, time, price, description)
- Event name
- Venue name and address
- Date and time
- List of Artists performing
- Pricing
- Description

### Link destinations for the page
- Artist pages
- Back to home

### List of tests for verifying the rendering of the page
1. Test: Event information display
   - Verify all event details are correctly displayed
   - Ensure the page title includes the correct event and venue name

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
This page showcases information about a specific artist, including their image, bio, social media links, an embedded example of their work (video or audio), upcoming events, and past performances.

TODO add mockup

### Parameters needed for the page
- Artist Name

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
   - Verify artist name, bio, and image are correctly displayed
   - Ensure the page title includes the artist name

2. Test: Upcoming events list
   - Check that upcoming events are listed and sorted by date
   - Verify links to event details pages are functional

3. Test: Music samples
   - If available, test the functionality of music sample players or video embeds

4. Test: Dynamic content loading
   - Ensure the page loads correctly with different artist IDs

## 4. Add Event:

### Page Title
Add Event: 

### Page Description
This page allows the user to create a new event page and will prompt for event details. Will have relevant text-boxes and selectors for adding values to each required field.

### Data needed to render the page
- Current date/time (for checking that new event will be after current date)

### Link destinations for the page
- links back to homepage (either submitting or cancelling)

### List of tests for verifying the rendering of the page
1. Test: 


## 5. Add artist:
### Page Title
Add New Artist: 

### Page Description
Similarly to the Add Event page, this page allows the user to create a new artist page and will includes text-boxes and selectors for each required field.

### Data needed to render the page
- User details (username, name, email, location)

### Link destinations for the page
- links back to homepage (either submitting or cancelling)

### List of tests for verifying the rendering of the page


## 6. List of artist:
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

## 7. About Page:
### Page Title
About

### Page Description
A simple about page, with a description of what the app is and how to use 

### Data needed to render the page
- User details (username, name, email, location)

### Link destinations for the page
