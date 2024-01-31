import requests
from bs4 import BeautifulSoup

def scrape_statcan_api():
    url = "https://open.canada.ca/en/search/inventory/fcd24f4158b89c00a0a2aa6893065d45"

    # Send a GET request to the API page
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the relevant information about how to obtain the API
        content_div = soup.find('div', class_='view-content')
        if content_div:
            api_info = content_div.find_all('p')
            # Extract and print the information
            for paragraph in api_info:
                print(paragraph.get_text(strip=True))
                print("----")
        else:
            print("Could not find the 'content' div on the page.")

    else:
        print(f"Failed to retrieve the API page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_statcan_api()