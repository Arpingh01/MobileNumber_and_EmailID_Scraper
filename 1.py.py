# Library - Requests: To make HTTP requests to a website and retrieve the content
# Library - BeautifulSoup: used to extract information from the webpage
# Library - Regex : To extract patterns like email and phone numbers
# Library - Csv : To save the extracted emails and phone numbers

import requests
from bs4 import BeautifulSoup
import re
import csv

# Step 1: Fetch webpage
url = "https://grievances.maharashtra.gov.in/en/officer-contact"
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")

# Step 2: Extract text or specific elements
text = soup.get_text()

# Regex patterns
email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
phone_pattern = r"\+?\d{1,4}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}"

emails = re.findall(email_pattern, text)
phone_numbers = re.findall(phone_pattern, text)

# Step 3: Print and Save Results
if emails or phone_numbers:
    print(f"Found Emails: {emails}")
    print(f"Found Phone Numbers: {phone_numbers}")

    with open("contacts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Phone Number"])

        # Write paired rows for emails and phone numbers
        for email, number in zip(emails, phone_numbers):
            writer.writerow([email, number])

        # Handle remaining unmatched entries
        for email in emails[len(phone_numbers):]:
            writer.writerow([email, ""])
        for number in phone_numbers[len(emails):]:
            writer.writerow(["", number])

    print("Data successfully saved to contacts.csv")
else:
    print("No emails or phone numbers found on the webpage.")













