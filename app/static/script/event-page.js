///////////////////////////
// Event Page Javascript
// Handles the data for an invidual event page
//
//
// Functions Used:
//
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
  eventName.textContent = event.name;
  console.log(event);

  eventContainer.append(eventDiv);
  eventDiv.append(eventName);
  
}
