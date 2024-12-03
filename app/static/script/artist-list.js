/*****
 ***** Fetches all the events from the API and calls the generateEventList function
 *****/
document.addEventListener('DOMContentLoaded', () => {
    const rootURL = window.location.origin;
    fetch(`${rootURL}/api/artists`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(artists => {
            console.log(artists); // This should log the events data

            generateArtistList(artists); // This function renders the list of events
        })
        .catch(error => console.error('Error:', error));
});

/**
 * generateArtistList --> Generates the list of events from the API call to HTML
 * @param {Array} artists
 * @returns {HTMLElement} artistsGrid
 */
const generateArtistList = (artists) => {
    const artistsgrid = document.getElementById('artists-grid');

    // Loop over the artists from the API call
    artists.forEach(artist => {
        // Create HTML elements for artist data
        const artistCard = document.createElement('div');
        artistCard.classList.add('artist-card');

        // Add Poster Container
        const posterContainer = document.createElement('div');
        posterContainer.classList.add('poster-container');
        artistCard.append(posterContainer);

        // Add Artist Poster
        const artistPoster = document.createElement('img');
        artistPoster.src = artist.imageurl;
        artistPoster.classList.add('artist-poster');
        posterContainer.append(artistPoster);

        // Create content container for text elements. Fixes issue where text appears over pictures.
        const contentContainer = document.createElement('div');
        contentContainer.classList.add('artist-card-content');
        artistCard.append(contentContainer);

        // Create a link to the individual artist page
        const artistName = document.createElement('h2');
        const artistLink = document.createElement('a');
        const artistDescription = document.createElement('p');

        // Set the inner text of the elements
        artistName.textContent = artist.name;
        artistDescription.textContent = artist.description;

        // Set the href attribute of the link
        artistLink.href = `/artists/username/${artist.artistusername}`;

        // Append the elements to the content container
        artistsgrid.append(artistCard);
        contentContainer.append(artistLink);
        artistLink.append(artistName);
        contentContainer.append(artistDescription);
    });
}