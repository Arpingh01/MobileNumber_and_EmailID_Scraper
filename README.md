# MobileNumber_&_EmailID_Scraper

This project is a Python script designed to extract email addresses and phone numbers from a specified webpage and save them into a CSV file for easy access and organization.

## Features
- Fetches webpage content using the `requests` library.
- Parses and extracts text using `BeautifulSoup`.
- Utilizes regular expressions to identify email addresses and phone numbers.
- Saves extracted information to a `contacts.csv` file.

## Libraries Used
- **Requests**: To make HTTP requests and retrieve webpage content.
- **BeautifulSoup**: To parse and extract data from HTML content.
- **Regex**: To detect patterns like email addresses and phone numbers.
- **CSV**: To store the extracted data in a structured format.

## Usage
1. Update the `url` variable in the script with the URL of the webpage you want to scrape.
2. Run the script:
   ```bash
   python extract_contacts.py
   ```
3. If emails or phone numbers are found, they will be printed on the console and saved in a `contacts.csv` file.

## File Description
- **extract_contacts.py**: The main script to scrape and save contact information.
- **contacts.csv**: The output file containing the extracted email addresses and phone numbers.

## Regular Expressions Used
- **Email Pattern**: 
  ```regex
  [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
  ```
- **Phone Number Pattern**: 
  ```regex
  \+?\d{1,4}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}
  ```

## Example Output
**Console Output:**
```
Found Emails: ['example1@mail.com', 'example2@mail.com']
Found Phone Numbers: ['+1-800-123-4567', '123-456-7890']
Data successfully saved to contacts.csv
```

**contacts.csv:**
| Email                | Phone Number     |
|----------------------|------------------|
| example1@mail.com   | +1-800-123-4567  |
| example2@mail.com   | 123-456-7890     |
