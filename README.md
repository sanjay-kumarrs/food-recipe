# 🍽️ Delicious — Food Recipe Web Application

A full-featured **Django-based food recipe web application** that allows users to explore recipes, discover professional chefs, calculate nutritional information for any food item, and interact with a vibrant culinary community.

---

## 📖 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features)
- [Architecture & Design](#-architecture--design)
  - [High-Level Architecture](#high-level-architecture)
  - [Project Structure](#project-structure)
  - [Database Design](#database-design)
  - [URL Routing](#url-routing)
  - [Template Architecture](#template-architecture)
- [Technology Stack](#-technology-stack)
- [Requirements](#-requirements)
  - [Software Requirements](#software-requirements)
  - [Hardware Requirements](#hardware-requirements)
  - [Functional Requirements](#functional-requirements)
  - [Non-Functional Requirements](#non-functional-requirements)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [API Integration](#-api-integration)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Introduction

**Delicious** is a modern food recipe web application designed to inspire culinary passion and make cooking accessible to everyone. The platform serves as a comprehensive hub where food enthusiasts — from beginners to seasoned chefs — can:

- Browse and search an extensive collection of recipes from diverse cuisines
- View detailed step-by-step cooking instructions with rich media
- Explore professional chef profiles and their specialties
- Calculate calorie and nutritional information for any food item
- Submit feedback and engage with the community

Built with **Django 4.2** and **Bootstrap 5**, the application follows the **MVT (Model-View-Template)** architectural pattern and emphasizes a responsive, visually appealing user experience with smooth animations and modern design elements.

---

## ✨ Features

| Feature | Description |
|---|---|
| **User Authentication** | Secure signup, login, logout with admin-based account approval system |
| **Recipe Browsing** | Browse all available recipes with images, ingredients, and cooking instructions |
| **Recipe Search** | Search recipes by name with case-insensitive partial matching |
| **Recipe Details** | View detailed recipe pages with prep time, cook time, total time, servings, nutritional info, and step-by-step instructions |
| **Chef Profiles** | View professional chef profiles including experience, cuisine specialty, and nationality |
| **Calorie Calculator** | Search any food item and get comprehensive nutritional breakdown powered by the API-Ninjas Nutrition API |
| **Exercise Recommendations** | See how long you need to jog, do yoga, lift weights, or walk to burn the calories for any food |
| **Nutritional Charts** | Interactive bar charts (Chart.js) visualizing nutritional values |
| **Health Alerts** | Automatic warnings for high sodium (>1000 mg) and high sugar (>100 g) foods |
| **Contact & Feedback** | Built-in contact form to submit feedback directly from the homepage |
| **Admin Panel** | Enhanced admin interface with Jazzmin for managing recipes, chefs, users, and feedback |
| **Responsive Design** | Fully responsive UI that works across desktop, tablet, and mobile devices |
| **Rich Text Editing** | TinyMCE integration for rich HTML content in recipe instructions and chef bios |
| **Image Carousel** | Animated hero carousel with multiple slides on the homepage |
| **Testimonials** | Swiper.js-powered testimonial slider showcasing user reviews |

---

## 🏗️ Architecture & Design

### High-Level Architecture

The application follows Django's **MVT (Model-View-Template)** architecture:

```
┌─────────────────────────────────────────────────────────┐
│                      CLIENT (Browser)                   │
│              HTML / CSS / JS / Bootstrap 5               │
└───────────────────────┬─────────────────────────────────┘
                        │  HTTP Request / Response
                        ▼
┌─────────────────────────────────────────────────────────┐
│                    URL DISPATCHER                        │
│                  food_recipe/urls.py                      │
└───────────────────────┬─────────────────────────────────┘
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
   ┌─────────────┐ ┌──────────┐ ┌──────────────┐
   │   modules/  │ │chef_info/│ │  Django Admin │
   │   views.py  │ │ models.py│ │  (Jazzmin)   │
   └──────┬──────┘ └────┬─────┘ └──────────────┘
          │              │
          ▼              ▼
   ┌─────────────────────────────┐
   │        MODELS (ORM)         │
   │   recipes │ chef │ UserProfile │ feedBack
   └──────────────┬──────────────┘
                  │
                  ▼
   ┌─────────────────────────────┐
   │     SQLite3 Database        │
   │       db.sqlite3            │
   └─────────────────────────────┘

   External:
   ┌─────────────────────────────┐
   │  API-Ninjas Nutrition API   │
   │  (Calorie Calculator)      │
   └─────────────────────────────┘
```

### Project Structure

```
food_recipe/                    # Project Root
│
├── manage.py                   # Django management utility
├── db.sqlite3                  # SQLite database file
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── food_recipe/                # Main Django project configuration
│   ├── __init__.py
│   ├── settings.py             # Project settings (apps, DB, middleware, etc.)
│   ├── urls.py                 # Root URL configuration
│   ├── wsgi.py                 # WSGI entry point for deployment
│   └── asgi.py                 # ASGI entry point for async deployment
│
├── modules/                    # Core application (recipes, chefs, users)
│   ├── __init__.py
│   ├── models.py               # Data models: recipes, chef, UserProfile
│   ├── views.py                # View functions (home, auth, recipes, calorie, etc.)
│   ├── admin.py                # Admin registrations with custom list displays
│   ├── apps.py                 # App configuration
│   ├── tests.py                # Test cases
│   └── migrations/             # Database migration files
│
├── chef_info/                  # Feedback & chef info application
│   ├── __init__.py
│   ├── models.py               # Data model: feedBack
│   ├── views.py                # (Currently unused — feedback handled in modules)
│   ├── admin.py                # Admin registration for feedBack
│   ├── apps.py                 # App configuration
│   ├── tests.py                # Test cases
│   └── migrations/             # Database migration files
│
├── templates/                  # HTML templates
│   ├── base.html               # Base template (block structure)
│   ├── header.html             # Navigation header with auth-aware links
│   ├── footer.html             # Site footer with social links
│   ├── index.html              # Homepage (hero, about, why-us, chefs, testimonials, contact)
│   ├── register.html           # User registration page
│   ├── login.html              # User login page
│   ├── search.html             # Recipe search & listing page
│   ├── recipe_details.html     # Individual recipe detail page
│   ├── chef_details.html       # Chef listing page
│   ├── calorie.html            # Calorie calculator with nutritional charts
│
├── static/                     # Static assets
│   └── assets/
│       ├── css/                # Stylesheets (style.css, style1.css, recipe.css)
│       ├── js/                 # JavaScript files (main.js)
│       ├── img/                # Images (slides, chefs, testimonials, favicon)
│       ├── calorie/            # Calorie page icons (running, yoga, walking, etc.)
│       ├── scss/               # SCSS source files
│       └── vendor/             # Third-party libraries (Bootstrap, Swiper, etc.)
│
├── media/                      # User-uploaded media files
│   ├── chefs/                  # Chef profile images
│   ├── recipess/               # Recipe images & nutritional info images
│   └── profile_pics/           # User profile pictures
│
└── venv/                       # Python virtual environment (not committed)
```

### Database Design

The application uses **SQLite3** with four core models:

```
┌────────────────────────┐     ┌─────────────────────────┐
│       recipes          │     │         chef             │
├────────────────────────┤     ├─────────────────────────┤
│ id (PK, BigAutoField)  │     │ id (PK, BigAutoField)   │
│ recipe_name (Char 100) │     │ chef_name (Char 100)    │
│ recipe_image (Image)   │     │ chef_age (PositiveInt)  │
│ intro (HTMLField)      │     │ chef_exp (Char 500)     │
│ ingredients (HTMLField)│     │ chef_info (HTMLField)    │
│ making (HTMLField)     │     │ chef_img (FileField)    │
│ nut (ImageField)       │     │ cusine (Char 100)       │
│ prep_time (Char 50)    │     │ nation (Char 100)       │
│ cook_time (Char 50)    │     └─────────────────────────┘
│ total_time (Char 50)   │
│ servings (Integer)     │     ┌─────────────────────────┐
└────────────────────────┘     │      UserProfile        │
                               ├─────────────────────────┤
┌────────────────────────┐     │ id (PK, BigAutoField)   │
│       feedBack         │     │ user (FK → auth.User)   │
├────────────────────────┤     │ is_approved (Boolean)   │
│ id (PK, BigAutoField)  │     └─────────────────────────┘
│ name (Char 100)        │
│ email (Char 100)       │
│ subject (Char 200)     │
│ message (TextField)    │
└────────────────────────┘
```

**Key Relationships:**
- `UserProfile` has a **OneToOne** relationship with Django's built-in `User` model
- Admin approval workflow: new users have `is_approved = False` until an admin approves them

### URL Routing

| URL Path | View Function | Name | Auth Required | Description |
|---|---|---|---|---|
| `/` | `MyHtml` | `home` | No | Homepage |
| `/signup/` | `Signup` | `signup` | No | User registration |
| `/login/` | `logins` | `login` | No | User login |
| `/logout/` | `LogoutPage` | `logout` | No | User logout |
| `/recipe/` | `food` | `recipe` | Yes | Recipe search & listing |
| `/details/` | `recipes_details` | `recipe_details` | No | Individual recipe detail |
| `/chef/` | `chef_details` | `chefdetails` | Yes | Chef listing |
| `/ch/` | `chef_info` | `chef_info` | Yes | Individual chef detail |
| `/cal/` | `cal` | `cal` | Yes | Calorie calculator |
| `/rec` | `addfeed` | `feedbacks` | Yes | Submit feedback |
| `/approve/` | `approve_user` | — | Staff only | Approve user accounts |
| `/admin/` | Django Admin | — | Staff | Admin panel (Jazzmin) |
| `/tinymce/` | TinyMCE URLs | — | — | Rich text editor endpoints |

### Template Architecture

The templates use Django's template inheritance system:

```
header.html (HTML head, navigation bar)
    └── base.html (block content)
            ├── index.html (homepage sections)
            ├── login.html (login form)
            ├── register.html (registration form)
            ├── search.html (recipe listing)
            ├── recipe_details.html (recipe detail)
            └── chef_details.html (chef listing)

calorie.html (standalone with inline header/footer)
footer.html (included as partial)
```

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Backend Framework** | Django 4.2.1 |
| **Language** | Python 3.x |
| **Database** | SQLite3 |
| **Frontend Framework** | Bootstrap 5.3.0 |
| **CSS Animations** | Animate.css |
| **Rich Text Editor** | TinyMCE (django-tinymce) |
| **Admin Theme** | Django Jazzmin |
| **Template Filters** | django-mathfilters, django.contrib.humanize |
| **Image Slider** | Swiper.js |
| **Lightbox** | GLightbox |
| **Charts** | Chart.js |
| **Icons** | Bootstrap Icons, Boxicons |
| **Fonts** | Google Fonts (Poppins, Satisfy, Comic Neue) |
| **External API** | API-Ninjas Nutrition API |
| **Deployment** | WSGI / ASGI compatible |

---

## 📋 Requirements

### Software Requirements

| Requirement | Version |
|---|---|
| Python | 3.8 or higher |
| Django | 4.2.1 |
| pip | Latest |
| Web Browser | Chrome / Firefox / Edge (modern) |
| Operating System | Windows / macOS / Linux |

### Hardware Requirements

| Component | Minimum |
|---|---|
| Processor | Dual-core 1.6 GHz |
| RAM | 2 GB |
| Disk Space | 500 MB |
| Network | Internet connection (for API & CDN resources) |

### Functional Requirements

1. **User Registration & Authentication**
   - Users can register with name, email, username, and password
   - Duplicate email detection and password confirmation validation
   - Admin-based account approval before login is permitted
   - Session-based authentication with login/logout capability

2. **Recipe Management**
   - Admin can add, edit, and delete recipes via the admin panel
   - Each recipe includes image, name, introduction, ingredients, cooking instructions, nutritional image, prep/cook/total time, and servings
   - Users can search recipes by name (case-insensitive, partial match)
   - Users can view detailed recipe information on a dedicated page

3. **Chef Management**
   - Admin can add, edit, and delete chef profiles
   - Each chef profile includes name, age, experience, bio, image, cuisine specialty, and nationality
   - Users can browse all chefs and view individual chef details

4. **Calorie Calculator**
   - Users can search for any food item to get nutritional information
   - Displays calories, carbohydrates, cholesterol, fats, fiber, potassium, protein, sodium, and sugar
   - Shows exercise recommendations (jogging, yoga, weightlifting, walking) to burn the calories
   - Visualizes nutritional data via interactive Chart.js bar charts
   - Provides health alerts for high sodium and high sugar content

5. **Feedback System**
   - Authenticated users can submit feedback via the contact form
   - Admin can view all feedback entries in the admin panel

6. **Admin Panel**
   - Enhanced with Jazzmin theme for modern UI
   - Search functionality for recipes and chefs
   - Full CRUD operations on all models

### Non-Functional Requirements

1. **Usability** — Intuitive navigation with responsive design across all devices
2. **Performance** — Fast page loads with optimized static asset delivery
3. **Security** — CSRF protection, password hashing, session management, admin approval workflow
4. **Maintainability** — Modular app structure following Django conventions
5. **Scalability** — Can be migrated to PostgreSQL/MySQL for production workloads
6. **Accessibility** — Semantic HTML with ARIA labels on interactive elements
7. **Compatibility** — Works on all modern browsers (Chrome, Firefox, Edge, Safari)

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/food_recipe.git
cd food_recipe
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Access the Application

- **Homepage:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📖 Usage

1. **Register** a new account at `/signup/`
2. Wait for **admin approval** — log in to the admin panel and approve the user
3. **Login** with approved credentials at `/login/`
4. **Browse recipes** at `/recipe/` — use the search bar to filter by name
5. **View recipe details** by clicking on any recipe card
6. **Explore chefs** at `/chef/` — click on a chef to view their full profile
7. **Calculate calories** at `/cal/` — enter a food item (e.g., "1 pizza") and view the nutritional breakdown
8. **Submit feedback** via the contact form on the homepage

---

## 🔌 API Integration

The **Calorie Calculator** feature uses the [API-Ninjas Nutrition API](https://api-ninjas.com/api/nutrition):

- **Endpoint:** `https://api.api-ninjas.com/v1/nutrition?query=`
- **Method:** GET
- **Authentication:** API key via `X-Api-Key` header
- **Response:** JSON array containing nutritional data (calories, macros, vitamins, etc.)

> **Note:** To use the calorie calculator, you need a valid API key from [API-Ninjas](https://api-ninjas.com/). Replace the key in `modules/views.py` with your own.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project uses the [Delicious Bootstrap Template](https://bootstrapmade.com/delicious-free-restaurant-bootstrap-theme/) by BootstrapMade. Please refer to their [license](https://bootstrapmade.com/license/) for template-specific terms.

---

<p align="center">
  Made with ❤️ by the Delicious Team
</p>
..
