# URL Shortener

## Project Description
This project is a simple **URL Shortener** built using **Flask** and **FastAPI**. It allows users to enter a long URL and get a shortened version, with an optional feature to create a custom short URL. The backend stores these mappings in an **SQLite database**, and users can be redirected to the original URL by visiting the short URL.

## Features
- **Custom & Random Short URLs:** Users can provide a custom alias for their short URL or let the system generate a random one.
- **Database Storage:** Uses **SQLite** to persist long and short URLs.
- **FastAPI API for URL Shortening:** Provides a **REST API** for shortening URLs.
- **Flask Web Interface:** A simple frontend for user interaction.
- **Redirection Support:** Short URLs automatically redirect users to the original URL.

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask, FastAPI
- **Database:** SQLite
- **API Communication:** Fetch API (JavaScript)

## Installation & Setup
Follow these steps to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/URL-Shortener.git
cd URL-Shortener
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask App
```bash
python app.py
```
The Flask app will be running at **http://localhost:5000**.

### 5. Run the FastAPI API
In another terminal, run:
```bash
uvicorn api:api --host 0.0.0.0 --port 8000 --reload
```
The FastAPI API will be running at **http://localhost:8000**.

## API Endpoints
### 1. Shorten URL
**Endpoint:**
```
POST /shorten
```
**Request Body:**
```json
{
  "long_url": "https://example.com",
  "custom_url": "myalias" (optional)
}
```
**Response:**
```json
{
  "short_url": "http://localhost:5000/myalias"
}
```

## Usage Instructions
1. Open **http://localhost:5000** in a browser.
2. Enter a long URL and (optionally) a custom short URL.
3. Click "Shorten" to generate the shortened URL.
4. Click on the shortened URL to visit the original site.
5. If the URL is not found, an error message is displayed.

## Future Improvements
- Add support for **analytics** (e.g., number of clicks per shortened URL).
- Implement **user authentication** for managing shortened URLs.
- Deploy the application using **Docker** and cloud hosting services.

## License
This project is licensed under the **MIT License**.
