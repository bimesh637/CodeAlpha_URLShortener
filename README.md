# CodeAlpha URL Shortener

A simple URL shortening service built using Flask. It stores original long URLs and provides short aliases for redirection.

##  Features
- Shorten long URLs with a unique short code
- Redirect from short code to original URL
- View all stored URLs (if endpoint enabled)
- Built with Flask and SQLite

##  Technologies
- Python
- Flask
- SQLite

##  API Endpoints

| Method | Endpoint     | Description                  |
|--------|--------------|------------------------------|
| POST   | `/shorten`   | Submit a long URL to shorten |
| GET    | `/<short>`   | Redirect to original URL     |

##  How to Run
```bash
python app.py
