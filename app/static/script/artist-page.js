document.addEventListener('DOMContentLoaded', () => {
    // Use Flask's route instead of calling API directly
    fetch(`/api/artists/username/${artistUsername}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(artist => {
            // Generate the main artist content
            generateArtistPage(artist);

            // Then fetch their events using the ArtistID
            return fetch(`/api/artists/${artist.artistid}/events`);
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(eventsData => {
            // API returns {events: [...], event_count: number}
            if (eventsData.events) {
                generateEvents(eventsData.events);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            // TODO: Add error state handling
        });
});

const generateArtistPage = (artist) => {
    // Update page title
    document.title = `Artist Profile: ${artist.name}`;

    // Header content
    const headerContent = document.querySelector('.header-content');
    headerContent.innerHTML = `
        ${artist.name} 
        <span class="date">${new Date().toLocaleDateString()}</span>
    `;

    // Artist image
    const artistImage = document.querySelector('.artist-image');
    if (artist.imageurl) {
        artistImage.innerHTML = `<img src="${artist.imageurl}" alt="${artist.name}">`;
    }

    // Artist info/bio
    const infoSection = document.querySelector('.info-section');
    infoSection.innerHTML = `
        <h3>Artist Info</h3>
        <p>${artist.bio || 'Biography coming soon...'}</p>
        ${artist.location ? `<p>Location: ${artist.location}</p>` : ''}
    `;

    // Social links
    const socialLinks = document.querySelector('.social-links ul');
    const socialPlatforms = [
        { key: 'facebookurl', label: 'Facebook' },
        { key: 'instagramurl', label: 'Instagram' },
        { key: 'soundcloudurl', label: 'SoundCloud' }
    ];

    socialLinks.innerHTML = socialPlatforms
        .map(({ key, label }) => {
            if (artist[key]) {
                return `<li><a href="${artist[key]}" target="_blank">${label}</a></li>`;
            }
            return '';
        })
        .join('');
};

const generateEvents = (events) => {
    if (!events || events.length === 0) {
        const upcomingEventsContainer = document.querySelector('.upcoming-events');
        const pastEventsContainer = document.querySelector('.past-events');

        upcomingEventsContainer.innerHTML = `
            <h3>Upcoming Events</h3>
            <div class="event-box">No upcoming events</div>
        `;

        pastEventsContainer.innerHTML = `
            <h3>Past Events</h3>
            <div class="event-box">No past events</div>
        `;
        return;
    }

    const currentDate = new Date();
    const upcomingEvents = [];
    const pastEvents = [];

    // Sort events into upcoming and past
    events.forEach(event => {
        const eventDate = new Date(event.datetime);
        if (eventDate >= currentDate) {
            upcomingEvents.push(event);
        } else {
            pastEvents.push(event);
        }
    });

    // Sort events by date
    upcomingEvents.sort((a, b) => new Date(a.datetime) - new Date(b.datetime));
    pastEvents.sort((a, b) => new Date(b.datetime) - new Date(a.datetime));

    // Generate upcoming events (limit to 3)
    const upcomingEventsContainer = document.querySelector('.upcoming-events');
    upcomingEventsContainer.innerHTML = `
        <h3>Upcoming Events</h3>
        ${upcomingEvents.slice(0, 3).map(event => generateEventBox(event)).join('')}
    `;

    // Generate past events (limit to 3)
    const pastEventsContainer = document.querySelector('.past-events');
    pastEventsContainer.innerHTML = `
        <h3>Past Events</h3>
        ${pastEvents.slice(0, 3).map(event => generateEventBox(event)).join('')}
    `;
};

const generateEventBox = (event) => {
    const eventDate = new Date(event.datetime).toLocaleDateString();
    const ticketPrice = event.ticketprice ? `$${event.ticketprice.toFixed(2)}` : 'Price TBA';

    return `
        <div class="event-box">
            <p>${event.name}</p>
            <p>@ ${event.venuename} - ${eventDate}</p>
            <p>${event.location}</p>
            ${event.description ? `<p>${event.description}</p>` : ''}
            <p>Tickets: ${ticketPrice}</p>
        </div>
    `;
};
  
  
