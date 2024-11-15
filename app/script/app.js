// Mock structure representing events - to be replaced with actual API data
// Each event has: id, array of artists, event name, venue, and date
const mockEvents = [
    { id: 1, artists: ['Artist A', 'Artist B'], eventName: 'Event A', venue: 'Venue 1', date: '2024-03-15' },
    { id: 2, artists: ['Artist C'], eventName: 'Event B', venue: 'Venue 2', date: '2024-03-16' },
    { id: 3, artists: ['Artist D', 'Artist E'], eventName: 'Event C', venue: 'Venue 3', date: '2024-03-17' },
    { id: 4, artists: ['Artist F'], eventName: 'Event D', venue: 'Venue 4', date: '2024-03-18' },
    { id: 5, artists: ['Artist G', 'Artist H', 'Artist I'], eventName: 'Event E', venue: 'Venue 5', date: '2024-03-19' },
    { id: 6, artists: ['Artist J', 'Artist K'], eventName: 'Event F', venue: 'Venue 6', date: '2024-03-20' },
    { id: 7, artists: ['Artist L', 'Artist M', 'Artist N', 'Artist O'], eventName: 'Event G', venue: 'Venue 7', date: '2024-03-21' },
    { id: 8, artists: ['Artist P', 'Artist Q'], eventName: 'Event H', venue: 'Venue 8', date: '2024-03-22' },
    { id: 9, artists: ['Artist R', 'Artist S', 'Artist T'], eventName: 'Event I', venue: 'Venue 9', date: '2024-03-23' },
];

/** createEventCard --->
 * Creates a single event card element
 * @param {Object} event - Event data containing artists, eventName, venue, and date
 * @param {number} index - Position in the event list, used for alternating placeholder colors
 * @returns {HTMLElement} The constructed card element
 */
function createEventCard(event, index)
{
    // Create main card container
    const card = document.createElement('div');
    card.className = 'event-card';
    // Alternate placeholder background colors based on even/odd index
    card.classList.add(index % 2 === 0 ? 'cyan-card' : 'green-card');

    // Create container for text content
    const contentDiv = document.createElement('div');
    contentDiv.className = 'event-content';

    // Create and populate artists section
    const artistsText = document.createElement('p');
    artistsText.className = 'artists';
    artistsText.textContent = event.artists.join(', ');

    // Create and populate event details section
    const eventText = document.createElement('p');
    eventText.className = 'event-details';
    eventText.textContent = `${event.eventName} @ ${event.venue} - ${formatDate(event.date)}`;

    // Assemble the card structure
    contentDiv.appendChild(artistsText);
    contentDiv.appendChild(eventText);
    card.appendChild(contentDiv);

    return card;
}

/** formatDate --->
 * Ensures consistency with date formatting, used in artist cards
 * @param {string} dateString - Date in YYYY-MM-DD format
 * @returns {string} Formatted date in MM/DD/YYYY format
 */
function formatDate(dateString)
{
    const [year, month, day] = dateString.split('-');
    return `${month}/${day}/${year}`;
}

/** displayEvents ---->
 * Displays all events in the grid
 * Clears existing content and creates new cards for each event
 */
function displayEvents()
{
    const eventsGrid = document.querySelector('.events-grid');
    eventsGrid.innerHTML = ''; // Clear existing cards
    mockEvents.forEach((event, index) =>
    {
        const card = createEventCard(event, index);
        eventsGrid.appendChild(card);
    });
}

/** updateCurrentDate -->
 * Updates the header date to current date
 * Formats date as MM/DD/YYYY
 */
function updateCurrentDate()
{
    const dateElement = document.querySelector('.date');
    const currentDate = new Date();
    dateElement.textContent = currentDate.toLocaleDateString('en-US',
        {
        month: '2-digit',
        day: '2-digit',
        year: 'numeric'
    });
}

/**
 * Toggles the filter field to appear and disappear
 * @returns {void}
 */
function toggleFilter()
{
    const filter = document.querySelector('.filter');
    filter.classList.toggle('hidden');
    alert('Filter button clicked');
}

/** init() --->
 * Initializes the page
 * Sets current date and displays event cards
 */
function init()
{
    updateCurrentDate();
    displayEvents();
}

document.addEventListener('DOMContentLoaded', init);