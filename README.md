# content-aggregator
A simple, command-line content aggregator built with Python. This script scrapes the top headlines from Hacker News and Reddit's r/programming and displays them in your terminal. This project is designed for beginners learning web scraping with Python.
## Features
Fetches the top 10 current stories from Hacker News.

Fetches the top 10 daily stories from Reddit's r/programming subreddit.

Clean, formatted output directly in the terminal.

Error handling for network issues.

No API keys required.

## Requirements
Python 3.x

requests library

beautifulsoup4 library

## Installation & Setup

Follow these steps to get the project running on your local machine.

Clone the repository (or download the code):
```sh
git clone https://github.com/YOUR_USERNAME/content-aggregator.git
cd content-aggregator
```

Install the required packages:
It's recommended to use a virtual environment.

```sh
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

```

(Note: You will need to create a requirements.txt file. See below.)

Creating the requirements.txt file
Create a file named requirements.txt in your project folder with the following content:

requests
beautifulsoup4
This allows others to install the necessary libraries easily using the pip install -r requirements.txt command.
```sh
pip install -r requirements.txt
```

### Usage
Once the setup is complete, run the script from your terminal:
```sh
python aggregator.py
```


