from flask import Flask, render_template, request, Blueprint, url_for, redirect, session,Response, flash,jsonify,request


import os
import requests




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')

@app.route('/api/knowledge-base', methods=['GET'])
def knowledge_base_response():
    if request.method == 'GET':
        user_message = request.args.get('message')
        print(user_message)
        # Call Your External API
        api_url = "https://wtlck3y8dh.execute-api.us-west-2.amazonaws.com/prod" 
        api_params = {'prompt': user_message}

        try:
            response = requests.get(api_url, params=api_params)
            response.raise_for_status()  # Raise an exception for bad status codes

            # Process the API response
            api_response_data = response.json()  # Assuming JSON response
            # ... (Extract data, format, etc.) ...
            # Extract the 'body' and remove extra quotes
            body_content = api_response_data['body'].strip('"')

            return jsonify({'response': body_content}) 

        except requests.exceptions.RequestException as e:
            return jsonify({'error': f"API Request Error: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
