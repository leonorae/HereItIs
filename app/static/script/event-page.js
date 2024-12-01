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
  const eventContainer = document.getElementById('event-container');

  // Create the 3 containers for the event page
  const eventCardLeft = document.createElement('div');
  const eventCardRight = document.createElement('div');
  const eventCardBottom = document.createElement('div');

  eventCardLeft.classList.add('event-card-left');
  eventCardRight.classList.add('event-card-right');
  eventCardBottom.classList.add('event-card-bottom');

  eventContainer.append(eventCardLeft);
  eventContainer.append(eventCardRight);
  eventContainer.append(eventCardBottom);


  // Create HTML elements for event data
  const eventName = document.createElement('h2');
  const artistName = document.createElement('h3');
  const dateTime = document.createElement('p');
  const eventDescription = document.createElement('p');

  // Create event poster
  const eventPoster = document.createElement('img');
  eventPoster.classList.add('event-poster');

  // Venue Information
  const venueName = document.createElement('h3');
  const venueDescription = document.createElement('p');

  // pass the event data into HTML element
  eventName.textContent = event.name;
  artistName.textContent = event.artistname;
  // TODO: break up the date time into separate elements for display
  dateTime.textContent = event.datetime;
  eventDescription.textContent = event.description;
  venueDescription.textContent = event.venuedescription;
  eventPoster.src = event.posterurl;
  // TODO: get the venue name from the venue ID
  venueName.textContent = event.venuename;

  console.log(event);

  eventCardLeft.append(eventName);
  eventCardLeft.append(artistName);
  
  eventCardLeft.append(eventPoster);
  eventCardLeft.append(eventDescription);
  
  eventCardRight.append(venueName);
  eventCardRight.append(venueDescription);
  eventCardBottom.append(dateTime);
  
}


// TODO: Incorporate this into an init function (as Alexander had done previously)