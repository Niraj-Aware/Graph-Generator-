import streamlit as st
import requests
import json

def generate_quickchart_url(data):
    # Construct the API URL for quickchart.io
    url = "https://quickchart.io/chart?c=" + data
    return url

def main():
    st.title("Graph Generator using quickchart.io API")
    
    # Get user statements as input
    user_statements = st.text_area("Enter your statements here:")
    
    # Get the graph type from the user
    graph_type = st.selectbox("Select Graph Type", ["bar", "line", "area"])
    
    # Add a Submit button
    if st.button("Generate Graph"):
        # Process user statements and create data for the graph
        # (Replace this with your data processing logic)
        data_for_graph = {
            "type": graph_type,
            "data": {
                "labels": user_statements.splitlines(),
                "datasets": [{
                    "label": "Data",
                    "data": [10, 20, 15]  # Replace this with your data based on user statements
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
