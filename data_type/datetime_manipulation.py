from datetime import datetime, timedelta
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def datetime_view():
    current_datetime = datetime.now()
    
    # Manipulating datetime
    future_datetime = current_datetime + timedelta(days=7)
    past_datetime = current_datetime - timedelta(hours=3)
    
    # Formatting datetime
    formatted_current = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    formatted_future = future_datetime.strftime('%Y-%m-%d %H:%M:%S')
    formatted_past = past_datetime.strftime('%Y-%m-%d %H:%M:%S')
    
    # Creating a dictionary
    data = {
        'current_datetime': formatted_current,
        'future_datetime': formatted_future,
        'past_datetime': formatted_past
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run()
