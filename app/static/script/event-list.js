/**
 * Fetches all the events from the API and calls the generateEventsGrid function
 */
document.addEventListener('DOMContentLoaded', () => {
    const rootURL = window.location.origin;
    fetch(`${rootURL}/api/events`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(events => {
            buildPage();
            generateEventsGrid(events); // This function renders the list of events
            createFilterEventsOptions(events);
            filterButtonFunction(events);
        })
        .catch(error => console.error('Error:', error));
});

// Get event data from the API and render it to the HTML

// Need to get the artist name and venue name from their IDs


/**
 * artistid
 * datetime
 * description
 * idevent
 * name
 * posterurl
 * ticketprice
 * venueid
 */

/**
 * Build the static HTML elements for the page
 * @returns {HTMLElement} header 
 */
const buildPage = () => {
    // Generates header for the index page
    const header = document.getElementsByClassName('header-content')[0];
    const dateTime = document.createElement('h2');
    dateTime.textContent = new Date().toDateString();
    header.appendChild(dateTime);
}

/**
 * generateEventsGrid --> Generates the list of events from the API call to HTML
 * @param {Array} events
 * @returns {HTMLElement} eventsGrid
 */
const generateEventsGrid = (events) => {
    // TODO: Organize the HTML elements and their class assignments

    // Create the events grid container
    const eventsGrid = document.getElementById('events-grid');
    eventsGrid.classList.add('events-grid');

    // Loop over the events from the API call
    events.forEach(event => {
        // Create HTML elements for event data
        const eventDiv = document.createElement('div');
        eventDiv.classList.add('event-card');
        eventsGrid.appendChild(eventDiv);

        // Creates the event poster card
        const eventPosterCard = document.createElement('div');
        eventPosterCard.classList.add('poster-container');
        eventDiv.appendChild(eventPosterCard);

        // Creates the event poster image
        const eventPosterImg = document.createElement('img');
        eventPosterImg.classList.add('event-poster');
        eventPosterImg.src = event.posterurl;
        eventPosterCard.appendChild(eventPosterImg);

        // Creates the event info card
        const eventContent = document.createElement('div');
        eventContent.classList.add('event-content');
        eventDiv.appendChild(eventContent);

        // Artist Div
        const artistDiv = document.createElement('div');
        artistDiv.classList.add('artists');
        eventContent.appendChild(artistDiv);

        // Artist Name
        const artistName = document.createElement('h2');
        artistName.classList.add('artist-name');
        // Replace artist ID with artist name
        artistLink = document.createElement('a');
        artistLink.href = `${window.location.href}artists/username/${event.artistusername}`;
        artistLink.textContent = event.artistname;
        artistDiv.appendChild(artistLink);

        // Event Details
        const eventDetails = document.createElement('div');
        eventDetails.classList.add('event-details');
        eventContent.appendChild(eventDetails);
        
        // Event Name
        const eventName = document.createElement('h3');
        eventName.classList.add('event-name');

        const eventLink = document.createElement('a');
        // eventName.textContent = event.name;
        eventLink.href = `${window.location.href}events/${event.idevent}`;
        eventLink.textContent = event.name + " @ " + event.venuename + " - " + event.datetime;

        eventName.appendChild(eventLink);
        eventDetails.appendChild(eventName);

        // Event Venue
        // TODO: Replace venue ID with venue name
        // const eventVenue = document.createElement('p');
        // eventVenue.classList.add('event-venue');
        // eventVenue.textContent = event.venuename;
        // eventDetails.appendChild(eventVenue);


        const eventWeekday = document.createElement('p');
        const eventDay = document.createElement('p');
        const eventMonth = document.createElement('p');
        const eventTime = document.createElement('p');
        const eventDescription = document.createElement('p');
        const eventPoster = document.createElement('img');
        const eventTicketPrice = document.createElement('p');       

        
        // gets the url of the current page (index) and appends
        

        // Split the datetime into array of strings to be used in HTML
        splitDateTime = event.datetime.split(" ");

        // 
        eventWeekday.textContent = splitDateTime[0].replace(",", "");
        eventDay.textContent = splitDateTime[1];
        eventMonth.textContent = splitDateTime[2];
        eventTime.textContent = splitDateTime[3];

        // 
        eventDescription.textContent = event.description;
        eventPoster.src = event.posterurl;
        eventTicketPrice.textContent = "$" + event.ticketprice;

        // Testing the datetime and obtaining proper formatting
        console.log(event.datetime);

        // Append elements to their respective parent elements
        
        
        // eventInfoCard.appendChild(eventWeekday);
        // eventInfoCard.appendChild(eventMonth);
        // eventInfoCard.appendChild(eventDay);
        // eventInfoCard.appendChild(eventTime);
        // eventInfoCard.appendChild(eventDescription);
        // eventInfoCard.appendChild(eventPoster);
        // eventInfoCard.appendChild(eventTicketPrice);
        
    });
}

// TODO: Build Filter Function
// const filterEvents = (events) => {
//   // Filter events by venue name

// }


/**
 * Creates the filter options for the events
 * @returns {HTMLElement} venueFilter
 * @returns {HTMLElement} artistFilter
 */
const createFilterEventsOptions = (events) => {
    const filterBox = document.getElementsByClassName('filter-box-container')[0];

    const filterOptions = document.createElement('div');
    const venueFilter = document.createElement('select');
    const artistFilter = document.createElement('select');

    // add venues to filter
    const venueTracker = {};
    venueTracker[0] = "All Venues";

    const option = document.createElement('option');
    option.value = 0;
    option.textContent = "All Venues";
    venueFilter.appendChild(option);

    events.forEach(event => {
        if (!(event.venueid in venueTracker)) {
            const option = document.createElement('option');
            venueTracker[event.venueid] = event.venuename;
            option.value = event.venueid;
            option.textContent = event.venuename;
            venueFilter.appendChild(option);
        }
    });

    // const artistTracker = {};

    // Add options to artist filter
    // events.forEach(event => {
    //     if (!(event.artistid in artistTracker)) {
    //         const option = document.createElement('option');
    //         artistTracker[event.artistid] = event.artistname;
    //         option.value = event.artistid;
    //         option.textContent = event.artistname;
    //         artistFilter.appendChild(option);
    //     }
    // });

    filterOptions.classList.add('filter-options');
    venueFilter.classList.add('venue-filter');
    // artistFilter.classList.add('artist-filter');

    filterBox.appendChild(filterOptions);
    filterOptions.appendChild(venueFilter);
    // filterOptions.appendChild(artistFilter);

    // create a submit button to filter events
    const submitButton = document.createElement('button');
    submitButton.textContent = 'Submit';
    submitButton.classList.add('submit-button');

    filterOptions.appendChild(submitButton);


    // initially hide the filter options on page load
    filterOptions.style.display = 'none';
}

/**
 * Select events based on filter results
 */
const filterEvents = (x) => {
    // TODO: filter events based on venue and artist
    const venueFilter = document.getElementsByClassName('venue-filter')[0];
    // const artistFilter = document.getElementsByClassName('artist-filter')[0];

    const selectedVenue = venueFilter.options[venueFilter.selectedIndex].value;
    // const selectedArtist = artistFilter.options[artistFilter.selectedIndex].value;

    const filteredEvents = [];

    // Filter events based on selected venue and artist
    x.forEach(event => {
        if (parseInt(selectedVenue) === 0) {
            filteredEvents.push(event);
        }
        // filteredEvents.push(event.venueid);
        if (event.venueid === parseInt(selectedVenue)) {
            filteredEvents.push(event);
        }

    // Clear the events grid
    const eventsGrid = document.getElementById('events-grid');
    eventsGrid.innerHTML = '';

    // Generate the filtered events grid
    generateEventsGrid(filteredEvents);

    });
}

/**
 * Hides and show the filter options when button is clicked
 */
const filterButtonFunction = (events) => {
    filterButton = document.getElementById('filter-button');
    filterButton.textContent = 'Filter Events';
    filterButton.addEventListener('click', () => {
    filterOptions = document.getElementsByClassName('filter-options')[0];
    if (filterOptions.style.display === 'none') {
        filterButton.textContent = 'Hide Filter';
        filterOptions.style.display = 'block';
        const submitButton = document.getElementsByClassName('submit-button')[0];
        submitButton.addEventListener('click', () => {
        filterEvents(events);
        });
    } else {
        filterOptions.style.display = 'none';
        filterButton.textContent = 'Filter Events';
    } 
});
}


// TODO: INIT function to call everything