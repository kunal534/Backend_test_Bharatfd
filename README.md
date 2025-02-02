# FAQ Management System

A Django-based FAQ management system that supports multilingual content, caching with Redis, and a REST API for fetching FAQs in different languages. The project integrates CKEditor for rich-text formatting in answers and uses Google Translate API for automatic translations.

## Features

- **Django Models** to store and manage FAQs with multilingual support.
- **CKEditor** integration for rich-text answers.
- **REST API** to fetch FAQs with language selection.
- **Caching** with Redis for improved performance.
- **Automatic Translations** using Google Translate API or googletrans with fallback to English.
- **Admin Panel** for easy FAQ management.

## Completed Tasks

1. **Implemented Django models** to manage FAQs, with multilingual support for questions and answers.
2. **Integrated CKEditor** for rich-text editing of FAQs in the admin panel.
3. **Created a REST API** to fetch FAQs with the option to select the language (`en`, `hi`, etc.).
4. **Added Redis caching** for improved performance in FAQ fetching.
5. **Configured automatic translations** using Google Translate API or `googletrans`, with fallback to English when translation is unavailable.
6. **Set up a superuser** for easy management of FAQs in the admin panel.
7. **Wrote unit tests** for ensuring code quality and functionality.
8. **Used `pytest`** for testing and integrated it with the Django project.
9. **Implemented clear cache functionality** before returning data in the API to ensure fresh content.

## Installation

### Prerequisites

- Python 3.x
- Redis (For caching)
- Google Cloud API Key (For translation, optional if using googletrans)

### Steps to Set Up Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kunal534/Backend_test_Bharatfd.git
   cd repository-name
   python3 -m venv venv
   
2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows

3. **Install dependencies:**
    ```bash
   pip install -r requirements.txt

4. **Set up Redis (Make sure Redis is installed and running on your local machine):**
   Start Redis server:
   ```bash
   redis-server
5. **Configure settings:**
   ```bash
   Add your Google API key to the settings or install googletrans if you choose to use the free version of Google Translate.
   In faq_project/settings.py, ensure the caching configuration is set up with Redis.

6. **Apply migrations:**
   ```bash
   python manage.py migrate

7. **Create a superuser to access the Django admin:**
   ```bash
   python manage.py createsuperuser

8.**Start the development server:**
   ```bash
  python manage.py runserver


