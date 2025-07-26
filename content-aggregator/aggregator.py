import requests
from bs4 import BeautifulSoup

def fetch_hacker_news():
    """Fetches top stories from Hacker News."""
    print("Fetching Hacker News stories...")
    url = 'https://news.ycombinator.com/'
    stories = []
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Raises an exception for bad status codes (4xx or 5xx)

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all story links, limit to top 10
        for item in soup.find_all('span', class_='titleline')[:10]:
            title_element = item.find('a')
            if title_element:
                title = title_element.get_text(strip=True)
                link = title_element['href']
                stories.append({'title': title, 'link': link})

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Hacker News: {e}")

    return stories

def fetch_reddit_programming():
    """Fetches top stories from Reddit's r/programming."""
    print("Fetching Reddit r/programming stories...")
    url = 'https://old.reddit.com/r/programming/top/?t=day'
    headers = {'User-Agent': 'My Content Aggregator 1.0'}
    stories = []

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all story links, limit to top 10
        for item in soup.find_all('p', class_='title')[:10]:
            title_element = item.find('a')
            if title_element:
                title = title_element.get_text(strip=True)
                link = title_element['href']
                # Make relative links absolute
                if not link.startswith('http'):
                    link = 'https://old.reddit.com' + link
                stories.append({'title': title, 'link': link})

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Reddit: {e}")

    return stories

def main():
    """Main function to run the aggregator."""
    
    # --- Fetch all stories ---
    hn_stories = fetch_hacker_news()
    reddit_stories = fetch_reddit_programming()

    # --- Display Hacker News stories ---
    print("\n" + "="*40)
    print(" Hacker News - Top 10 Stories ")
    print("="*40)
    if hn_stories:
        for i, story in enumerate(hn_stories, 1):
            print(f"{i}. {story['title']}")
            print(f"   Link: {story['link']}\n")
    else:
        print("Could not retrieve stories.")

    # --- Display Reddit stories ---
    print("\n" + "="*40)
    print(" Reddit r/programming - Top 10 Stories ")
    print("="*40)
    if reddit_stories:
        for i, story in enumerate(reddit_stories, 1):
            print(f"{i}. {story['title']}")
            print(f"   Link: {story['link']}\n")
    else:
        print("Could not retrieve stories.")

# This ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()