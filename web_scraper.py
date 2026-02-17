import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "http://quotes.toscrape.com"

# Send request
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes_data = []

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text")
        author = quote.find("small", class_="author")

        quote_text = text.get_text() if text else "No quote"
        author_name = author.get_text() if author else "No author"

        quotes_data.append([quote_text, author_name])

    # Save to CSV
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])
        writer.writerows(quotes_data)

    print("Data successfully saved to quotes.csv")

else:
    print("Failed to retrieve website")
