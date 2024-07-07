from flask import Flask, render_template, redirect, url_for
import requests
import redis

app = Flask(__name__)

# Redis setup
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def index():
    # Fetch a joke from the joke API
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke = response.json()

    # Increment visit count in Redis
    redis_client.incr('visit_count')

    # Get the visit count
    visit_count = redis_client.get('visit_count')

    return render_template('index.html', joke=joke, visit_count=visit_count)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
