import requests
import json
import flask
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/retrieve_tweet_embed', methods=['GET'])
def main():
    """
    Retrieves the HTML embed code for a tweet given its ID.
    :return: HTML embed code for the tweet
    """
    status_id = flask.request.args.get('status_id')
    if status_id is None:
        return 'Invalid request - Missing status ID', 400
    url = f"https://publish.twitter.com/oembed?url=https://twitter.com/_/status/{status_id}"
    response = requests.get(url)
    processed_result = json.loads(response.text)['html']
    return processed_result


if __name__ == "__main__":
    app.run()
