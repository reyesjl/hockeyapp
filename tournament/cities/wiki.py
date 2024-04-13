import wikipediaapi
import requests

def get_city_image_url(city_name):
    # Prepare the request parameters
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "images",
        "titles": city_name,
    }

    # Send a GET request to the MediaWiki API
    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract image title from the response
    pages = data.get("query", {}).get("pages", {})
    for page_id, page_data in pages.items():
        image_info = page_data.get("images", [])
        for info in image_info:
            image_title = info.get("title", "")

            # Check if the image title ends with a supported image extension
            supported_extensions = (".jpg", ".jpeg", ".png", ".gif", ".svg")
            if image_title.lower().endswith(supported_extensions):
                # Construct the URL for the image using the image title
                image_url = f"https://en.wikipedia.org/wiki/File:{image_title}"
                return image_url

    return None

def get_city_summary(city_name):
    # Create a Wikipedia object
    wiki_wiki = wikipediaapi.Wikipedia('CitySummaries (jose.reyes.9@Outlook.com)', 'en')
    
    # Get the page for the city
    page = wiki_wiki.page(city_name)
    
    # Check if the page exists
    if page.exists():
        # Return the summary
        return page.summary
    else:
        return None
    
def get_city_image(city_name):
    # Create a Wikipedia object with a custom user agent
    wiki_wiki = wikipediaapi.Wikipedia('CityImages (jose.reyes.9@Outlook.com)', 'en')

    # Get the page for the city
    page = wiki_wiki.page(city_name)

    # Check if the page exists
    if page.exists():
        # Get the first image in the page images
        image_info = page.images
        if image_info:
            # Get the first image URL
            image_url = next(iter(image_info.values()))
            return image_url
    return None