import requests
from bs4 import BeautifulSoup

# Specify the URL
url = "https://example.com"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find and print all <h1> tags on the page
    for h1_tag in soup.find_all("h1"):
        print(h1_tag.text.strip())
    
    # Example: Find and print all links on the page
    for link in soup.find_all("a"):
        href = link.get("href")
        text = link.text.strip()
        print(f"Link text: {text}, URL: {href}")
else:
    print("Failed to retrieve the page.")
