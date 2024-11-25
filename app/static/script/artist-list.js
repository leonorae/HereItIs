/**
 * Fetches all the events from the API and calls the generateEventList function
 */
document.addEventListener('DOMContentLoaded', () => {
    fetch('http://127.0.0.1:5000/api/artists')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(artists => {
            console.log(artists); // This should log the events data
            
            generateArtistList(artists); // This function renders the list of events

            // Example: Render the events in the HTML
            // Can I move this to another function to be called?
            
            
        })
        .catch(error => console.error('Error:', error));
});

/**
 * generateArtistList --> Generates the list of events from the API call to HTML
 * @param {Array} artists
 * @returns {HTMLElement} eventsContainer
 */
const generateArtistList = (artists) => {
    const artistsContainer = document.getElementById('artists-container');

    // Loop over the artists from the API call
    artists.forEach(artist => {
        // Create HTML elements for artist data
        const artistDiv = document.createElement('div');
        // Create a link to the individual artist page
        const artistName = document.createElement('h2');
        const artistLink = document.createElement('a');
        const artistDescription = document.createElement('p');

        // what other things do we need to display?

        // Set the inner text of the elements
        artistName.textContent = artist.name;
        artistDescription.textContent = artist.description;

        // Set the href attribute of the link
        artistLink.href = `/artists/${artist.artistid}`;

        // Append the elements to the container
        artistsContainer.append(artistDiv);
        artistDiv.append(artistLink);
        artistLink.append(artistName);
        artistDiv.append(artistDescription);
    });
}