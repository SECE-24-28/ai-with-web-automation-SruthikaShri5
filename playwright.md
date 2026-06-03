Quote Scraper Using Playwright
Project Overview

This project demonstrates web scraping using the Playwright library in Python. The program automatically visits the "Quotes to Scrape" website, extracts quotes and their corresponding authors, and displays the first 50 quotes in the console.

The scraper navigates through multiple pages until 50 quotes have been collected.

Objectives
Learn web scraping using Playwright.
Automate browser interactions.
Extract data from web pages.
Handle pagination automatically.
Store and display scraped information.
Technologies Used
Python 3.x
Playwright
Chromium Browser
Website Used

The scraper collects data from:

https://quotes.toscrape.com

This website is specifically designed for practicing web scraping techniques.

Project Structure
QuoteScraper/
│
├── quote_scraper.py
├── requirements.txt
└── README.md
Prerequisites

Before running the project, ensure the following are installed:

Python 3.8 or higher
Internet connection
Playwright package
Installation
Step 1: Install Playwright
pip install playwright
Step 2: Install Browser Dependencies
playwright install

This command downloads the Chromium browser used by Playwright.

Program Workflow

The program performs the following steps:

Launches a Chromium browser.
Opens the Quotes to Scrape website.
Extracts quote text.
Extracts author names.
Displays the quote and author.
Moves to the next page.
Repeats until 50 quotes are collected.
Closes the browser.
Code Explanation
Importing Playwright
from playwright.sync_api import sync_playwright

Imports Playwright's synchronous API.

Initializing Counter
count = 0

Tracks the total number of quotes scraped.

Starting Playwright
with sync_playwright() as p:

Creates a Playwright session.

Launching Browser
browser = p.chromium.launch(headless=True)

Launches Chromium browser in headless mode.

Headless Mode
Browser runs in the background.
No graphical window appears.
Faster execution.
Creating a New Page
page = browser.new_page()

Opens a new browser tab.

Page Counter
page_num = 1

Tracks the current page number.

Loop Until 50 Quotes
while count < 50:

Keeps scraping until 50 quotes are collected.

Navigating to a Page
page.goto(f"https://quotes.toscrape.com/page/{page_num}/")

Opens the specified page.

Example:

https://quotes.toscrape.com/page/1/
https://quotes.toscrape.com/page/2/
Waiting for Page Load
page.wait_for_load_state("networkidle")

Waits until all network activity has finished.

Extracting Quotes
quotes = page.locator(".quote .text").all_text_contents()

Collects all quote texts from the page.

Example:

"The world as we have created it is a process of our thinking."
Extracting Authors
authors = page.locator(".quote .author").all_text_contents()

Collects author names.

Example:

Albert Einstein
Processing Data
for quote, author in zip(quotes, authors):

Pairs each quote with its corresponding author.

Incrementing Counter
count += 1

Updates total quote count.

Displaying Results
print(f"Author: {author}")
print(f"Quote : {quote}")

Shows scraped data in the console.

Stop After 50 Quotes
if count >= 50:
    break

Prevents collecting more than 50 quotes.

Moving to Next Page
page_num += 1

Loads the next page of quotes.

Closing Browser
browser.close()

Releases browser resources.

Sample Output
Quote 1

Author: Albert Einstein

Quote: "The world as we have created it is a process of our thinking."

------------------------------------------------------------

Quote 2

Author: J.K. Rowling

Quote: "It is our choices, Harry, that show what we truly are..."

------------------------------------------------------------
Features
Automated browser control
Dynamic page navigation
Multi-page scraping
Headless execution
Easy-to-understand code
Beginner-friendly project
Advantages of Playwright
Fast execution
Supports modern websites
Handles JavaScript-rendered content
Cross-browser support
Reliable automation framework
Applications
Data collection
Market research
Content aggregation
Educational projects
Automation testing
Web data analysis
Possible Enhancements
Save quotes to CSV file
Save quotes to Excel file
Save data to a database
Export to JSON
Add error handling
Scrape all quotes instead of only 50
Build a GUI interface
Create a web dashboard
Troubleshooting
Module Not Found Error
ModuleNotFoundError: No module named 'playwright'

Solution:

pip install playwright
Browser Not Installed
Executable doesn't exist

Solution:

playwright install
Internet Connection Error

Ensure that the system is connected to the internet and the target website is accessible.

Conclusion

This project demonstrates the use of Playwright for web scraping by automatically navigating through multiple pages and extracting quote information. It serves as an excellent beginner project for learning browser automation, data extraction, and web scraping techniques using Python.
