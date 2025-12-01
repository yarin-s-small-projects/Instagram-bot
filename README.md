# Instagram Bot

An automated Instagram bot built with Selenium that finds and follows users from similar accounts.

## Features

- Automated login to Instagram
- Search for similar accounts
- Find and follow suggested users
- Handles popups and click interceptions
- Rate limiting to avoid detection

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file from the example:
```bash
copy .env.example .env
```

5. Edit `.env` with your Instagram credentials:
```env
SIMILAR_ACCOUNT="target_account_username"
EMAIL="your_email@example.com"
PASSWORD="your_password"
URL="https://www.instagram.com/accounts/login/"
```

## Usage

Run the bot:
```bash
python main.py
```

## Important Notes

⚠️ **Use at your own risk**: Automated actions on Instagram may violate their Terms of Service and could result in account suspension or ban.

- The bot follows a maximum of 10 users per run to avoid rate limiting
- Instagram's UI changes frequently, so selectors may need updates
- Use delays between actions to mimic human behavior

## Requirements

- Python 3.x
- Chrome browser
- ChromeDriver (managed by Selenium)

## License

This project is for educational purposes only.
