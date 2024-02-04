# Motivational Quote Sender

## Overview
This Python program sends a motivational quote to specified email recipients using the SMTP protocol. It randomly selects a quote from a provided text file and sends it via the Outlook mail server.

## Prerequisites
- Python 3.x
- An active internet connection
- An Outlook email account with valid credentials
- JSON file ("data.json") containing Outlook email credentials and recipient email addresses
- Text file ("quotes.txt") containing motivational quotes

## Setup Instructions
1. Ensure you have Python installed on your system.
2. Make sure you have an active internet connection.
3. Prepare a JSON file named `data.json` containing the following structure:

```json
{
  "outlook": {
    "email": "your_email@outlook.com",
    "password": "your_outlook_password"
  },
  "recipients": [
    {
      "email": "recipient1@example.com"
    },
    {
      "email": "recipient2@example.com"
    }
  ]
}
```
Replace `"your_email@outlook.com"` with your Outlook email and `"your_outlook_password"` with your email password. Add recipient email addresses as needed.

4. Prepare a text file named `quotes.txt` containing a list of motivational quotes, each on a separate line.

## Program Functionality
- The program reads Outlook email credentials and recipient email addresses from the `data.json` file.
- It randomly selects a motivational quote from the `quotes.txt` file.
- The selected quote is then emailed to all specified recipients using the Outlook SMTP server.

## Usage
1. Ensure that `data.json` and `quotes.txt` files are in the same directory as the Python script.
2. Run the Python script.
3. The program will select a random quote and send it to the specified recipients via email.

## Error Handling
- If the program encounters errors such as missing files or invalid JSON data, appropriate error messages will be displayed.
- Please ensure that all required files (`data.json` and `quotes.txt`) are present in the program directory and have the correct format.

## Note
- Ensure that you use this program responsibly and comply with email sending policies to avoid being flagged as spam.
- You may need to adjust SMTP server settings if you're using an email service other than Outlook.
- It is recommended to secure your JSON file containing email credentials and avoid sharing it publicly.
