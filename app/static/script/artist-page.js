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
    fetch(`http://127.0.0.1:5000/api/artists/username/${artistUsername}`)
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
  