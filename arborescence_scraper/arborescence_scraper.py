import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

# Set to keep track of visited URLs
visited_urls = set()


# Function to scrape the website recursively
def scrape_website(url, max_depth=2, current_depth=0):
    if current_depth > max_depth:
        return

    if url in visited_urls:
        return

    try:
        # Get the content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        visited_urls.add(url)

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the body content and return it
        body_content = soup.body.get_text(strip=True) if soup.body else ""
        st.write(f"Scraped Content from {url} (Depth: {current_depth}):")
        st.text(body_content[:500])  # Display only first 500 chars as a preview
        time.sleep(1)  # 1 second delay between requests

        # Extract all links on the page and recursively scrape
        links = set(a['href'] for a in soup.find_all('a', href=True))
        for link in links:
            # Build the absolute URL
            abs_link = urljoin(url, link)
            # Only follow links that start with the base URL
            if abs_link.startswith(url):
                scrape_website(abs_link, max_depth, current_depth + 1)

    except requests.RequestException as e:
        st.error(f"Failed to request {url}: {e}")


# Streamlit UI
st.title("Recursive Web Scraper")
st.write("This app scrapes an entire website arborescence starting from a given URL.")

# Input fields for the URL and depth
url = st.text_input("Enter Website URL to start scraping", value="https://example.com")
max_depth = st.slider("Select the depth of recursion", min_value=1, max_value=5, value=2)

# Button to start scraping
if st.button("Start Scraping"):
    # Clear the set of visited URLs to start fresh each time
    visited_urls.clear()

    # Validate the input URL
    if not url.startswith("http"):
        st.error("Please enter a valid URL that starts with 'http' or 'https'.")
    else:
        st.write(f"Starting scraping from: {url} (Max Depth: {max_depth})")

        # Call the scraper function
        scrape_website(url, max_depth)

        # Show a message when finished
        st.success("Scraping completed!")

