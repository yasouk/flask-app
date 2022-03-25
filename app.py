from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def home():

    buffer=[]

    request = requests.get('https://pokeapi.co/api/v2/pokemon-species/','limit=1000')
    data = request.json()['results']
    for i, pokemon in enumerate(data):
        buffer.append({'i':i+1,'name':pokemon['name']})
    return render_template('index.html', data= buffer)
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =='__main__':
    app.run()