# HereItIs API Usage Guide

This document provides instructions for interacting with the `HereItIs` API to manage `Artist`, `Venue`, and `Event` data.


## Adding Data

The API allows new entries (Artist, Venue, and Event) to be added to each table via `POST` requests.

### 1. Add a New Artist

To add a new artist, use the following command:

```bash
curl -X POST https://hereitis-v3.onrender.com/api/artist -H "Content-Type: application/json" -d '{
    "ArtistUserName": "artist3",
    "Name": "Artist Three",
    "Bio": "Bio for artist three",
    "ImageURL": "http://image.url",
    "Location": "New York"
    "FacebookURL": "http://facebook.com"
    "InstagramURL": "http://instagram.com"
    "SoundCloudURL" "http://soundcloud.com"
}'
```

### 2. Add a New Venue
```bash
curl -X POST https://hereitis-v3.onrender.com/api/venue -H "Content-Type: application/json" -d '{
    "Name": "Venue One",
    "Location": "Los Angeles",
    "Description": "A popular concert venue"
}'
```

### 3. Add a New Event
```bash
curl -X POST https://hereitis-aomy.onrender.com/api/event -H "Content-Type: application/json" -d '{
    "Name": "Concert One",
    "DateTime": "2025-01-01 19:00:00",
    "Description": "New Year concert",
    "ArtistID": 1,   // replace with actual ArtistID
    "VenueID": 1,    // replace with actual VenueID
    "TicketPrice": 49.99,
    "PosterURL": "http://poster.url"
}'
```

## Retrieving Data in a Table

### 1. Get All Artists
```bash
curl https://hereitis-aomy.onrender.com/api/artists
```
### 2. Get All Venues
```bash
curl  https://hereitis-aomy.onrender.com/api/venues
```

### 3. Get All Events
```bash
curl https://hereitis-aomy.onrender.com/api/events
```

## Retrieving Specific Data

### 1. Get Event Details by ID
Retrieves detailed information about a specific event, including associated artist and venue details.

```bash
curl https://hereitis-aomy.onrender.com/api/events/<event_id>
```

Example response:
```json
{
    "idEvent": 1,
    "Name": "Concert One",
    "DateTime": "2025-01-01 19:00:00",
    "Description": "New Year concert",
    "ArtistName": "Artist Three",
    "ArtistUserName": "artist3",
    "ArtistImageURL": "http://image.url",
    "VenueName": "Venue One",
    "VenueLocation": "Los Angeles",
    "VenueDescription": "A popular concert venue"
}
```

### 2. Get Artist Details by Username
Retrieves detailed information about a specific artist, including their social media links.

```bash
curl https://hereitis-aomy.onrender.com/api/artists/username/<username>
```

Example response:
```json
{
    "ArtistID": 1,
    "ArtistUserName": "artist3",
    "Name": "Artist Three",
    "Bio": "Bio for artist three",
    "ImageURL": "http://image.url",
    "Location": "New York",
    "FacebookURL": "http://facebook.com/artist3",
    "InstagramURL": "http://instagram.com/artist3",
    "SoundCloudURL": "http://soundcloud.com/artist3"
}
```

### 3. Get Upcoming Events by Artist ID
Retrieves all future events for a specific artist, including venue details.

```bash
curl https://hereitis-aomy.onrender.com/api/artists/<artist_id>/events
```

Example response:
```json
{
    "events": [
        {
            "idEvent": 1,
            "Name": "Concert One",
            "DateTime": "2025-01-01 19:00:00",
            "Description": "New Year concert",
            "TicketPrice": 49.99,
            "PosterURL": "http://poster.url",
            "VenueName": "Venue One",
            "Location": "Los Angeles",
            "Description": "A popular concert venue"
        }
    ],
    "event_count": 1
}
```

## Response Codes

All new endpoints follow these status codes:
- `200`: Success
- `404`: Resource not found
- `500`: Server error
