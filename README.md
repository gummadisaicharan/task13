# 🕸️ Task 13 – Web Scraping Using BeautifulSoup

## 📌 Project Overview

This project was completed as part of my Python Developer Internship (Task 13).  
The objective of this task is to understand and implement web scraping using Python.

Web scraping is the process of extracting data from websites automatically using code.  
In this task, I used Python along with the `requests` and `BeautifulSoup` libraries to collect data from a public website and store it in a CSV file.

---

## 🎯 Objective

- Fetch HTML content from a website
- Parse the HTML structure
- Extract specific data (text, attributes, links, etc.)
- Handle missing elements safely
- Store extracted data into a CSV file
- Follow ethical scraping practices

---

## 🛠️ Tools & Technologies Used

- Python
- requests
- BeautifulSoup (bs4)
- CSV module
- VS Code

---

## 🌐 Website Used for Scraping

Website: http://quotes.toscrape.com  
(This is a scrape-friendly website designed for learning web scraping.)

---

## ⚙️ How the Script Works

### 1️⃣ Sending HTTP Request
The script uses the `requests` library to send a GET request to the website and retrieve its HTML content.

```python
response = requests.get(url)
````

---

### 2️⃣ Parsing HTML Content

The retrieved HTML content is parsed using BeautifulSoup.

```python
soup = BeautifulSoup(response.text, "html.parser")
```

BeautifulSoup allows us to navigate and search the HTML structure easily.

---

### 3️⃣ Identifying HTML Elements

Using browser Developer Tools, I inspected the website to identify:

* HTML tags
* Class names
* Attributes

Example:

```python
quotes = soup.find_all("div", class_="quote")
```

---

### 4️⃣ Extracting Data

From each quote block, I extracted:

* Quote text
* Author name

Example:

```python
text = quote.find("span", class_="text").get_text()
author = quote.find("small", class_="author").get_text()
```

To avoid errors from missing tags, safe extraction methods were used.

---

### 5️⃣ Storing Data into CSV

The extracted data was stored in a CSV file using Python's built-in `csv` module.

```python
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(quotes_data)
```

---

## 📂 Project Structure

```
Task-13-Web-Scraping/
│
├── web_scraper.py
├── quotes.csv
├── README.md
```

---

## 📊 Output

The script generates a CSV file containing:

| Quote      | Author      |
| ---------- | ----------- |
| Quote text | Author name |

This file can be opened in Excel or any spreadsheet application.
## 🧠 Key Concepts Learned

* What is Web Scraping
* Difference between HTML and DOM
* How to inspect a website structure
* Using BeautifulSoup to navigate HTML
* Extracting text and attributes
* Handling missing elements safely
* Saving structured data to CSV
* Ethical scraping practices

## ⚖️ Ethical Considerations

While performing web scraping:

* I used a public practice website.
* I did not overload the server.
* I avoided scraping private or copyrighted data.
* I ensured scraping was done responsibly.
  
## 🚀 Future Improvements

* Implement pagination to scrape multiple pages
* Add error handling using try-except blocks
* Export data to Excel format
* Add logging for debugging


## 📝 Conclusion

This task helped me understand how websites are structured and how data can be programmatically extracted.
As someone who is still learning Python, this project strengthened my understanding of HTTP requests, HTML parsing, and data handling.

I am continuing to explore more advanced scraping techniques and real-world applications.
