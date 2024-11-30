///////////////////////////
// Artist Page Javascript
// Handles the data for an invidual artist page
//
//
// Functions Used:
//
//
///////////////////////////

document.addEventListener('DOMContentLoaded', () => {
    // Get the artist ID from the URL
    // update the URL for launching the page currently just local
    const rootURL = window.location.origin;
    fetch('${rootURL}/api/artists/username/${artistUsername}/info-and-events')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(artist => {
            
          console.log(`${artist}`); // This should log the events data
          // loop throuh the events
          generateArtist(artist); // This function renders the list of events
          generateFutureEvents(artist);
            
  
          // Example: Render the events in the HTML
          // Can I move this to another function to be called?
            
            
        })
        .catch(error => console.error('Error:', error));
  });
  
  // Make the artist page
  const generateArtist = (artist) => {
    const artistContainer = document.getElementById('artist-container');
    // Create HTML elements for event data
    const artistDiv = document.createElement('div');
    const artistName = document.createElement('h2');
    console.log(artist.name);
    artistName.textContent = artist.name;
    console.log(artist.bio);

    artistContainer.append(artistDiv);
    artistDiv.append(artistName);
    
  }

  const generateFutureEvents = (artist) => {
    const artistContainer = document.getElementById('artist-container');
    // Create HTML elements for event data
    const futureEventsDiv = document.createElement('div');
    const futureEventsHeader = document.createElement('h2');
    futureEventsHeader.textContent = "Upcoming Events";
    artistContainer.append(futureEventsDiv);
    futureEventsDiv.append(futureEventsHeader);
    console.log(artist.events);

    // Loop through the events and render to HTML
    artist.events.forEach(event => {
      const eventName = document.createElement('h3');
      futureEventsDiv.append(eventName);


  
      // pass the event data into HTML element
      eventName.textContent = event.name;
    }); 
  }
  
