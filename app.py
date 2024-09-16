from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Weather-checking function
def get_weather(city):
    api_key = '8ff75ba50df6ce0c5e226df397720061'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        temp = round(weather_data['main']['temp'] - 273.15, 2)
        description = weather_data['weather'][0]['description']
        return {'temp': temp, 'description': description}
    else:
        return None

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/get_weather', methods=['POST'])
def get_weather_route():
    city = request.form['city']
    weather = get_weather(city)
    
    if weather:
        return render_template('index.html', weather=weather, city=city)
    else:
        return render_template('index.html', error="City not found", city=city)

# Ensure the app listens on all interfaces
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
