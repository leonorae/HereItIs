///////////////////////////
// Event Page Javascript
// Handles the data for an invidual event page
//
//
// Functions Used:
// - generateEvent(event): Renders the event data by creating HTML elements
//
///////////////////////////

document.addEventListener('DOMContentLoaded', () => {
  // Get the event ID from the URL
  const rootURL = window.location.origin;
  // fetch the event from API
  fetch(`${rootURL}/api/events/${eventID}`)
      .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok ' + response.statusText);
          }
          return response.json();
      })
      .then(event => {
        console.log(`${event}`); // This should log the events data
        generateEvent(event); // This function renders the list of events
      })
      .catch(error => console.error('Error:', error));
});

// Make the event page: create the HTML elements, provide data, and append to the container
const generateEvent = (event) => {
  // Set title of page
  document.getElementsByTagName('title')[0].textContent = event.name;
  const eventContainer = document.getElementById('event-container');

  // Generate Event Name and Date for Header
  const header = document.getElementsByTagName('header')[0];
  const headerContent = document.createElement('h2');
  headerContent.textContent = event.name + ' - ' + event.datetime;
  header.append(headerContent);

  // Create the 4 containers for the event page
  const eventCardLeft = document.createElement('div');
  const eventCardTop = document.createElement('div');
  const eventCardRight = document.createElement('div');
  const eventCardBottom = document.createElement('div');

  eventCardTop.classList.add('event-card-top');
  eventCardLeft.classList.add('event-card-left');
  eventCardRight.classList.add('event-card-right');
  eventCardBottom.classList.add('event-card-bottom');

  eventContainer.append(eventCardTop);

  // left and right go into top container
  eventCardTop.append(eventCardLeft);
  eventCardTop.append(eventCardRight);
  eventContainer.append(eventCardBottom);

  console.log(event);

  // Create HTML elements for event data
  
  const dateTime = document.createElement('p');
  const eventDescription = document.createElement('p');

  // Event Poster Container
  const eventPosterContainer = document.createElement('div');
  eventPosterContainer.classList.add('event-poster-container');
  eventCardLeft.append(eventPosterContainer);

  // Create event poster
  const eventPoster = document.createElement('img');
  eventPoster.classList.add('event-poster');
  eventPoster.src = event.posterurl;
  eventPosterContainer.append(eventPoster);

  // Venue Information
  const venueDescription = document.createElement('p');
  
  venueDescription.classList.add('venue-description');

  // pass the event data into HTML element
  const artistName = event.artistname;

  const venueName = event.venuename;
  venueName.textContent = event.venuename;
  // TODO: break up the date time into separate elements for display
  dateTime.textContent = event.datetime;
  eventDescription.textContent = `Event Description: ${event.description}`;
  venueDescription.textContent = `Venue Description: ${event.venuedescription}`;
  
  // TODO: get the venue name from the venue ID
  venueName.textContent = event.venuename;

  console.log(event);
  
  

  const artistAndVenue = document.createElement('h2');
  artistAndVenue.classList.add('artist-venue');
  artistAndVenue.append(artistName + ' @ ' + venueName);
  eventCardBottom.append(artistAndVenue);
 

  
  eventCardLeft.append(eventDescription);
  
  eventCardRight.append(venueName);
  eventCardRight.append(venueDescription);
  // eventCardBottom.append(artistName);

  // Add Artist Poster to the aside with description
  const aside = document.getElementsByTagName('aside')[0];
  const artistPoster = document.createElement('img');
  artistPoster.classList.add('artist-poster');
  artistPoster.src = event.artistimageurl;
  aside.append(artistPoster);

  // Add ticket info to the aside
  const ticketContainer = document.createElement('div');
  ticketContainer.classList.add('ticket-container');
  aside.append(ticketContainer);

  const ticketHeader = document.createElement('h3');
  ticketHeader.textContent = 'Ticket Price';
  ticketContainer.append(ticketHeader);

  // Ticket Pricing
  const ticketInfo = document.createElement('div');
  ticketInfo.classList.add('ticket-info');
  ticketInfo.textContent = `$${event.ticketprice}`;
  ticketContainer.append(ticketInfo);

  
}


// TODO: Incorporate this into an init function (as Alexander had done previously)