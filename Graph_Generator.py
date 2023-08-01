import streamlit as st
import requests
import json

# Function to call the ChatGPT API
def call_chat_gpt_api(text):
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'sk-...OHEW'
    url = f'https://api.openai.com/v1/engines/davinci-codex/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    data = {
        'prompt': text,
        'max_tokens': 100,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['text']

def generate_quickchart_url(data):
    # Construct the API URL for quickchart.io
    url = "https://quickchart.io/chart?c=" + data
    return url

def main():
    st.title("Graph Generator using ChatGPT and quickchart.io API")
    
    # Get user statements as input
    user_statements = st.text_area("Enter your statements here:")
    
    # Call the ChatGPT API to make the statement more understandable
    processed_statements = call_chat_gpt_api(user_statements)
    
    # Process statements and create data for the graph
    # (Replace this with your data processing logic based on processed_statements)
    data_for_graph = {
        "type": "bar",
        "data": {
            "labels": ["Label 1", "Label 2", "Label 3"],
            "datasets": [{
                "label": "Data",
                "data": [10, 20, 15]
            }]
        }
    }
    
    # Convert data to JSON string
    data_json = json.dumps(data_for_graph)

    # Generate the quickchart.io URL for the graph
    graph_url = generate_quickchart_url(data_json)

    # Display the graph
    st.image(graph_url, use_column_width=True)

if __name__ == "__main__":
    main()
    
