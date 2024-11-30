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
            console.log(events); // This should log the events data
            
            generateEventsGrid(events); // This function renders the list of events
            
        })
        .catch(error => console.error('Error:', error));
});

// Get event data from the API and render it to the HTML


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

        // Create a link to the individual event page

        // Event Name
        const eventName = document.createElement('h2');
        eventName.classList.add('event-name');
        const eventLink = document.createElement('a');
        eventDiv.appendChild(eventLink);


        const eventWeekday = document.createElement('p');
        const eventDay = document.createElement('p');
        const eventMonth = document.createElement('p');
        const eventTime = document.createElement('p');
        const eventDescription = document.createElement('p');
        const eventPoster = document.createElement('img');
        const eventTicketPrice = document.createElement('p');       

        eventName.textContent = event.name;
        // gets the url of the current page (index) and appends
        eventLink.href = `${window.location.href}events/${event.idevent}`;
        eventLink.textContent = event.name;

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
        
        
        eventDiv.appendChild(eventWeekday);
        eventDiv.appendChild(eventMonth);
        eventDiv.appendChild(eventDay);
        eventDiv.appendChild(eventTime);
        eventDiv.appendChild(eventDescription);
        eventDiv.appendChild(eventPoster);
        eventDiv.appendChild(eventTicketPrice);
        
    });
}

// TODO: INIT function to call everything