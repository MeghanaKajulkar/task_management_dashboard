import requests

def test_streamlit_app():
    url = "http://localhost:8501"
    
    # Make a GET request to the Streamlit app
    response = requests.get(url)

    # Check if the response is successful (status code 200)
    assert response.status_code == 200, f"Expected 200 OK, but got {response.status_code}"

    # Check if the content contains specific text or element
    assert "Streamlit" in response.text, "Streamlit page did not load correctly"
