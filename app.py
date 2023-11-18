from flask import Flask, render_template, request, Response, jsonify  # Import render_template and jsonify
from supabase_py import create_client, Client

url: str = 'https://hlmyhwperjzxvtfhdbkw.supabase.co'
key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsbXlod3Blcmp6eHZ0ZmhkYmt3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTYxMTk0NTcsImV4cCI6MjAxMTY5NTQ1N30.bHzzlJycNv_PWk_s7_PEvYY3HPqRbf83TrnklLAVMYk'
supabase: Client = create_client(url, key)

table = 'time_temp_humidity_1'
lim = 1000
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():

    # Get the 'limit' parameter from the query string (default to 100 if not provided)
    limit = int(request.args.get('limit', 100))

    # Fetch data from Supabase or your database and return it as JSON
    response = supabase.table(table).select('*').order('id', desc= True).limit(limit).execute()
    # print(response)

    # Extract the "moist" values
    m1 = []
    m2 = []
    m1.extend([item['moist'] for item in response['data']])
    m2.extend([item['moist2'] for item in response['data']])

    # Run data smoothing so that everything looks nice
    alpha = 0.2  # Adjust the smoothing factor as needed
    ema = None
    ema2 = None
    smoothed_m1 = []
    smoothed_m2 = []

    # Assuming moisture_data is a list of your raw moisture data
    for data_point in m1:
        if ema is None:
            ema = data_point  # Initialize EMA with the first data point
        else:
            ema = (alpha * data_point) + (1 - alpha) * ema
            ema = int(ema)
        smoothed_m1.append(ema)

    for data_point in m2:
        if ema2 is None:
            ema2 = data_point
        else:
            ema2 = (alpha * data_point) + (1 - alpha) * ema2
            ema2 = int(ema2)
        smoothed_m2.append(ema2)

    # Replace "moist" values in the JSON data with the EMA values
    for i in range(len(response['data'])):
        response['data'][i]['moist'] = smoothed_m1[i]
        response['data'][i]['moist2'] = smoothed_m2[i]


    return response

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True, port=3000)

