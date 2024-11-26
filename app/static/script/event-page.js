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
  fetch(`http://127.0.0.1:5000/api/events/${eventID}`)
      .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok ' + response.statusText);
          }
          return response.json();
      })
      .then(event => {
          
        console.log(`${event}`); // This should log the events data
        // loop throuh the events
        generateEvent(event); // This function renders the list of events
          

        // Example: Render the events in the HTML
        // Can I move this to another function to be called?
          
          
      })
      .catch(error => console.error('Error:', error));
});

// Make the event page
const generateEvent = (event) => {
  const eventContainer = document.getElementById('event-container');
  // Create HTML elements for event data
  const eventDiv = document.createElement('div');
  const eventName = document.createElement('h2');
  const artistName = document.createElement('h3');
  const dateTime = document.createElement('p');
  const eventDescription = document.createElement('p');
  const eventPoster = document.createElement('img');
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

  eventContainer.append(eventDiv);
  eventDiv.append(eventName);
  eventDiv.append(eventDescription);
  eventDiv.append(artistName);
  eventDiv.append(venueName);
  eventDiv.append(venueDescription);
  eventDiv.append(dateTime);
  eventDiv.append(eventPoster);
  
  
}


// TODO: Incorporate this into an init function (as Alexander had done previously)