from flask import Flask, render_template
import requests

app = Flask('app')


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route('/')
def home():
    #Weather API
    city = 'toronto'
    key = ''
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    response = requests.get(url)
    data = response.json()
    temp_c = round(data['main']['temp'] - 273.15, 2)
    temp_description = data['weather'][0]['description']

    url1 = "https://body-mass-index-bmi-calculator.p.rapidapi.com/metric"

    querystring = {"weight": "150", "height": "1.83"}

    headers = {
        "x-rapidapi-key": "dcdc417494mshb9fc248ec109429p188b7ejsn256904294d3a",
        "x-rapidapi-host": "body-mass-index-bmi-calculator.p.rapidapi.com"
    }

    bmi_response = requests.get(url1, headers=headers, params=querystring)
    bmi_data = bmi_response.json()  # Assuming JSON response
    bmi_value = bmi_data.get("bmi")  # Adjust to match actual API response

    return render_template('index.html',
                           temp_c=temp_c,
                           temp_description=temp_description,
                           bmi_value=bmi_value)


@app.route('/CER')
def cer():
    return render_template('CER.html')


@app.route('/about-me')
def aboutme():
    return render_template('about-me.html')


@app.route('/Python')
def python():
    return render_template('Python.html')


@app.route('/Retail_database')
def retail():
    return render_template('Retail_database.html')


@app.route('/dashboards')
def dashboards():
    return render_template('dashboard.html')


@app.route('/r-project')
def r_project():
    return render_template('R-Project.html')


@app.route('/basketball')
def basketball():
    return render_template('basketball.html')


@app.route('/rcasestudy')
def rcasestudy():
    return render_template('RCaseStudy.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
