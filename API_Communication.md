# HereItIs API Usage Guide

This document provides instructions for interacting with the `HereItIs` API to manage `Artist`, `Venue`, and `Event` data.


## Adding Data

The API allows adding new entries to each table (Artist, Venue, and Event) via `POST` requests.

### 1. Add a New Artist

To add a new artist, use the following command:

```bash
curl -X POST https://hereitis-aomy.onrender.com/api/artist -H "Content-Type: application/json" -d '{
    "ArtistUserName": "artist3",
    "Name": "Artist Three",
    "Bio": "Bio for artist three",
    "ImageURL": "http://image.url",
    "Location": "New York"
}'
```

### 2. Add a New Venue
```bash
curl -X POST https://hereitis-aomy.onrender.com/api/venue -H "Content-Type: application/json" -d '{
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

## Adding Data

Use `GET` requests to retrieve all entries in each category.

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
