from flask import Flask
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    response = str(response)

    return response


@app.route('/categories', methods=['GET','POST'])
def categories():

    api_url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(api_url).json()
    response = str(response)
    return response


if __name__ == "__main__":
    app.debug = True
    app.run()
