# MovieLove

MovieLove is a Django-based movie catalog for browsing films and exploring the
people and media connected to them. It provides a clean public-facing website
with movie listings, search, detail pages, contact messages, and Django admin
support for managing the catalog.

## Features

- Browse the MovieLove home page and complete movie catalog.
- Search movies by title, production house, genre, or cast member.
- Open a detail page for a movie using its unique slug.
- Store movie banners and thumbnails with Django media support.
- Model genres, production houses, cast, choreographers, music workers,
  trailers, songs, and reviews.
- Collect visitor messages through the contact form.
- Manage catalog data through the Django admin site.

## Tech Stack

- Python 3.10+
- Django
- SQLite for local development
- Pillow for image fields
- Django templates, CSS, and vanilla JavaScript

## Quick Start

### 1. Clone the repository

```powershell
git clone https://github.com/om54/MovieLove.git
cd MovieLove
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser.

## Useful Commands

Run Django's system checks:

```bash
python manage.py check
```

Run the test suite:

```bash
python manage.py test
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

Build static files for deployment:

```bash
python manage.py collectstatic
```

## Main Routes

| Route | Purpose |
| --- | --- |
| `/` | MovieLove home page |
| `/all-movies/` | Browse all movies |
| `/search/?q=query` | Search the movie catalog |
| `/movie/<slug>/` | View movie details |
| `/contact/` | Send a contact message |
| `/admin/` | Manage content as an administrator |

## Project Structure

```text
movieLove/
├── main/                       # MovieLove application
│   ├── migrations/             # Database migrations
│   ├── static/                 # CSS, JavaScript, and image assets
│   ├── templates/main/         # Django HTML templates
│   ├── admin.py                # Admin registrations
│   ├── form.py                 # Contact form
│   ├── models.py               # Movie catalog data models
│   ├── urls.py                 # Application routes
│   └── views.py                # Request handlers
├── movieLove/                  # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── db.sqlite3                  # Local development database
├── manage.py                   # Django command-line entry point
└── requirements.txt            # Python dependencies
```

## Media and Static Files

Static assets are served from `main/static/`. Uploaded images use the
`MEDIA_ROOT` directory configured in `movieLove/settings.py`. During local
development, keep uploaded media in the project environment and do not commit
private or production-generated files.

## Production Checklist

Before deploying, update the Django configuration to:

- Set `DEBUG = False`.
- Move `SECRET_KEY` into an environment variable and rotate the development key.
- Configure `ALLOWED_HOSTS` for the deployment domain.
- Use a production database and configure secure database credentials.
- Configure persistent media storage and run `collectstatic`.
- Review CSRF, HTTPS, cookie, and security settings.

## License

No license has been specified yet. Add a license file before distributing the
project publicly.
