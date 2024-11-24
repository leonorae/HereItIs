
document.addEventListener('DOMContentLoaded', () => {
    fetch('http://127.0.0.1:5000/api/events')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(events => {
            console.log(events); // This should log the events data

            generateEventList(events); // This function renders the list of events

            // Example: Render the events in the HTML
            // Can I move this to another function to be called?
            const eventsContainer = document.getElementById('events-container');
            
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
 * generateEventList -->
 * @param {Array} events
 * @returns {HTMLElement} eventsContainer
 */
const generateEventList = (events) => {
    // Loop over the events from the API call
    events.forEach(event => {
        // Create HTML elements for event data
        const eventDiv = document.createElement('div');
        const eventName = document.createElement('h2');
        const eventWeekday = document.createElement('p');
        const eventDay = document.createElement('p');
        const eventMonth = document.createElement('p');
        const eventTime = document.createElement('p');
        const eventDescription = document.createElement('p');
        const eventPoster = document.createElement('img');
        const eventTicketPrice = document.createElement('p');       

        eventName.textContent = event.name; // Adjust according to your event object structure

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

        console.log(event.datetime);

        eventsContainer.appendChild(eventDiv);
        eventDiv.appendChild(eventName);
        eventDiv.appendChild(eventWeekday);
        eventDiv.appendChild(eventMonth);
        eventDiv.appendChild(eventDay);
        eventDiv.appendChild(eventTime);
        eventDiv.appendChild(eventDescription);
        eventDiv.appendChild(eventPoster);
        eventDiv.appendChild(eventTicketPrice);
        
    });
}