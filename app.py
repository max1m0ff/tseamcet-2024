from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the Excel data into a pandas DataFrame
data_file = 'college_allotment_data.xlsx'  # Path to your Excel file
data_df = pd.read_excel(data_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the request
    user_input = request.json
    user_rank = int(user_input['rank'])
    user_category = user_input['category']
    user_gender = user_input['gender']

    # Filter the DataFrame based on user input
    filtered_data = data_df[
        (data_df['Rank'] <= user_rank) &
        (data_df['Category'] == user_category) &
        (data_df['Gender'] == user_gender)
    ]

    # Convert the filtered data to a list of dictionaries
    eligible_colleges = filtered_data.to_dict(orient='records')

    # Return the data as JSON
    return jsonify(eligible_colleges)

if __name__ == '__main__':
    app.run(debug=True)
