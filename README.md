# 🚀 DevBox - FastAPI Utilities API

DevBox is a modular FastAPI project that provides utility APIs to boost productivity. Currently, it includes:

* 🧩 JSON Formatter API
* 🔗 URL Shortener API with redirect support and hit tracking
* 📔 SQLite database with SQLAlchemy ORM
* 📦 Environment configuration via `.env`



## 🏗️ Features

### ✅ JSON Formatter

* Formats raw JSON into readable, indented JSON.
* Useful for developers and debugging.

**Endpoint:**

```
POST /utils/format-json
```

**Request:**

```json
{
  "data": "{\"key\": \"value\"}"
}
```

**Response:**

```json
{
  "formatted_json": "{\n  \"key\": \"value\"\n}"
}
```

---

### ✅ URL Shortener

* Converts long URLs into short, hash-based URLs.
* Redirects users to the original URL.
* Tracks hit count and last accessed time.

**Endpoints:**

* `POST /url/shorten` — Shortens a URL
* `GET /url/s/{code}` — Redirects to original URL

**Example Request:**

```json
{
  "url": "https://example.com/some/very/long/link"
}
```

**Example Response:**

```json
{
  "short_url": "http://localhost:8000/url/s/abc123"
}
```



## 🧐 Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/) for API backend
* [Pydantic](https://docs.pydantic.dev/) for data validation
* [SQLAlchemy](https://www.sqlalchemy.org/) as ORM
* [SQLite](https://www.sqlite.org/) as development DB
* [python-dotenv](https://pypi.org/project/python-dotenv/) for environment variables



## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Ellvius/DevBox.git
cd DevBox
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up `.env`

Create a `.env` file in the root directory:

```ini
DATABASE_URL=sqlite:///./devbox.db
```

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

Access the interactive docs at:
📍 `http://localhost:8000/docs`



## 📌 TODO / Future Improvements

* [ ] Add expiry date for shortened URLs
* [ ] Add authentication (JWT or OAuth)
* [ ] Track analytics (user agent, IP)
* [ ] Switch to PostgreSQL in production
* [ ] Add a frontend interface


