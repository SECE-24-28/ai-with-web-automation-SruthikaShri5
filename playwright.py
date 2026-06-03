from playwright.sync_api import sync_playwright

count = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page_num = 1

    while count < 50:
        page.goto(f"https://quotes.toscrape.com/page/{page_num}/")
        page.wait_for_load_state("networkidle")

        quotes = page.locator(".quote .text").all_text_contents()
        authors = page.locator(".quote .author").all_text_contents()

        for quote, author in zip(quotes, authors):
            count += 1

            print(f"\nQuote {count}")
            print(f"Author: {author}")
            print(f"Quote : {quote}")
            print("-" * 60)

            if count >= 50:
                break

        page_num += 1

    browser.close()

print("\nFinished scraping 50 quotes!")
