from flask import Flask, url_for, render_template, request, jsonify
from markupsafe import escape
import requests

app = Flask(__name__)

# Index Route
@app.route('/')
def home():
    return render_template('index.html')

# API Route for Index Page
@app.route('/api/events')
def get_events():
    print('Fetching events...')
    try:
        response = requests.get('https://hereitis-aomy.onrender.com/api/events')
        response.raise_for_status()  # Raise an exception for HTTP errors
        events = response.json()
        print('Events fetched successfully:', events)
    except requests.exceptions.RequestException as e:
        print('Error fetching events:', e)
        events = []
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)