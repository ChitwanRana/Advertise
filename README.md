<div align="center">

# 🏷️ Bottle Label Builder

### Transform Your FSSAI Authorization into Beautiful Custom Labels

[![Django](https://img.shields.io/badge/Django-5.0.6-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.2-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<img src="https://img.icons8.com/fluency/200/bottled-water.png" alt="Bottle Label Builder" width="150"/>

**A modern Django web application for food businesses to create, preview, and iterate on custom bottle labels with AI-powered design suggestions.**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) • [Contributing](#-contributing)

---

</div>

## 📖 About The Project

**Bottle Label Builder** is a streamlined platform designed specifically for small food and beverage businesses to convert their FSSAI (Food Safety and Standards Authority of India) authorization into professional, customizable bottle labels.

### 🎯 Problem It Solves

Small food businesses often struggle with:
- Creating professional branding materials from regulatory documents
- Visualizing how their logo and certification will look on actual products
- Getting team feedback before finalizing label designs
- Managing multiple design iterations efficiently

### 💡 Our Solution

Upload your FSSAI certificate and brand logo once, and instantly:
- ✨ Generate multiple AI-powered label design concepts
- 👁️ Preview realistic bottle label mockups
- 📝 Collect team reviews and feedback
- 🔄 Iterate quickly on your branding

---

## ✨ Features

### 🚀 Core Functionality

- **📤 Easy Upload System**
  - Upload FSSAI license number and certificate
  - Add business name and branding details
  - Upload logo with automatic optimization
  - Set delivery dates and order quantities

- **🎨 AI-Powered Design Ideas**
  - Automatically generates 3+ label design concepts
  - Suggestions for minimalist, premium, and eco-friendly styles
  - Visual preview with your actual logo and business details

- **👥 Collaborative Review System**
  - Team members can leave reviews and ratings (1-5 stars)
  - Comment on specific design aspects
  - Track feedback over time

- **📱 Responsive Design**
  - Works seamlessly on desktop, tablet, and mobile
  - Modern, intuitive interface with Bootstrap 5
  - Smooth animations and transitions

### 🎨 UI/UX Highlights

- **Modern Gradient Design** - Beautiful purple/indigo color scheme
- **Icon Integration** - Bootstrap Icons throughout for better visual communication
- **Card-Based Layouts** - Clean, organized information display
- **Hover Effects** - Interactive elements with smooth animations
- **Form Validation** - Real-time feedback on user inputs
- **Empty States** - Helpful guidance when no data exists

---

## 🖼️ Demo

### Landing Page
Beautiful hero section explaining the platform with clear CTAs

### Upload Form
Intuitive multi-step form with icons, helpful hints, and validation

### Label Preview
Realistic mockup showing how your label will look on bottles with AI-generated design ideas

### Review System
Star ratings and detailed feedback from team members

---

## 🛠️ Tech Stack

### Backend
- **Django 5.0.6** - High-level Python web framework
- **SQLite** - Lightweight database for development
- **Pillow** - Image processing library

### Frontend
- **Bootstrap 5.3.2** - Responsive CSS framework
- **Bootstrap Icons 1.11.1** - Comprehensive icon library
- **Vanilla JavaScript** - For interactive elements

### Key Django Apps
- `bottle` - Main application handling uploads, previews, and reviews

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ChitwanRana/Advertise.git
   cd Advertise/Label
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   ```
   Navigate to: http://127.0.0.1:8000/
   ```

🎉 **You're all set!** Start uploading your FSSAI certificates and creating labels.

---

## 🎯 Usage

### For End Users

1. **Navigate to the Upload Page**
   - Click "Upload Your FSSAI" from the landing page
   - Or use the navbar menu

2. **Fill in Your Details**
   - Business/Brand Name
   - FSSAI License Number (14 digits)
   - Expected Delivery Date (calendar picker)
   - Number of Bottles
   - Upload your logo (PNG, JPG, SVG)
   - Upload FSSAI certificate (PDF or image)

3. **Preview Your Label**
   - After submission, you'll be redirected to the preview page
   - See your logo and details in a realistic label mockup
   - Explore AI-generated design ideas

4. **Gather Feedback**
   - Share the preview link with your team
   - Collect reviews with star ratings
   - Read detailed feedback to iterate

### For Developers

```bash
# Run Django management commands
python manage.py makemigrations  # Create new migrations
python manage.py migrate         # Apply migrations
python manage.py createsuperuser # Create admin user
python manage.py runserver       # Start dev server

# Access admin panel
http://127.0.0.1:8000/admin/
```

---

## 📁 Project Structure

```
Advertise/
├── Label/                      # Django project root
│   ├── manage.py              # Django CLI tool
│   ├── db.sqlite3             # SQLite database
│   ├── media/                 # Uploaded files (logos, certificates)
│   ├── Label/                 # Project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── bottle/                # Main app
│   │   ├── models.py          # FSSAIEntry, Review models
│   │   ├── views.py           # landing, upload, detail views
│   │   ├── forms.py           # FSSAIEntryForm, ReviewForm
│   │   ├── urls.py            # App URL patterns
│   │   ├── admin.py           # Admin configuration
│   │   └── migrations/
│   └── templates/             # HTML templates
│       └── bottle/
│           ├── base.html      # Base template
│           ├── landing.html   # Home page
│           ├── upload.html    # Upload form
│           ├── home.html      # Entries list
│           ├── detail.html    # Preview & reviews
│           └── _reviews.html  # Review partial
└── README.md                  # This file
```

---

## 🗄️ Database Schema

### FSSAIEntry Model
| Field | Type | Description |
|-------|------|-------------|
| `id` | AutoField | Primary key |
| `fssai_code` | CharField(100) | FSSAI license number |
| `authorisation_name` | CharField(150) | Business/brand name |
| `date_of_delivery` | DateField | Expected delivery date |
| `number_of_orders` | PositiveIntegerField | Bottle quantity |
| `logo` | ImageField | Brand logo upload |
| `certificate` | FileField | FSSAI certificate upload |
| `submitted_at` | DateTimeField | Timestamp |

### Review Model
| Field | Type | Description |
|-------|------|-------------|
| `id` | AutoField | Primary key |
| `entry` | ForeignKey | Related FSSAIEntry |
| `name` | CharField(100) | Reviewer name |
| `rating` | IntegerField | 1-5 stars |
| `feedback` | TextField | Review text |
| `created_at` | DateTimeField | Timestamp |

---

## 🎨 Customization

### Change Color Scheme

Edit `templates/bottle/base.html`:

```css
.hero { 
  background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%); 
}
.btn-primary { 
  background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%); 
}
```

### Add More Design Ideas

Edit `bottle/views.py` in the `detail` function:

```python
ideas = [
    "Your custom design idea 1",
    "Your custom design idea 2",
    "Your custom design idea 3",
]
```

### Modify Form Fields

Edit `bottle/forms.py` to add/remove fields or change validation.

---

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG = False` in `settings.py`
- [ ] Configure `ALLOWED_HOSTS` in `settings.py`
- [ ] Use PostgreSQL/MySQL instead of SQLite
- [ ] Set up static file serving (WhiteNoise or CDN)
- [ ] Configure media file storage (AWS S3, Cloudinary)
- [ ] Set up environment variables for secrets
- [ ] Enable HTTPS/SSL
- [ ] Set up proper logging
- [ ] Configure email backend for notifications

### Deployment Platforms

- **Heroku** - Easy deployment with Git integration
- **PythonAnywhere** - Django-friendly hosting
- **DigitalOcean** - Flexible VPS hosting
- **AWS/GCP/Azure** - Enterprise-grade cloud platforms

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### How to Contribute

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Ideas

- 🎨 Add more AI design templates
- 📱 Improve mobile responsiveness
- 🔐 Add user authentication
- 📊 Create analytics dashboard
- 🖨️ Add PDF export for labels
- 🌐 Add multi-language support
- ♿ Improve accessibility (WCAG compliance)
- 🧪 Add unit and integration tests

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👥 Authors

**Chitwan Rana**
- GitHub: [@ChitwanRana](https://github.com/ChitwanRana)
- Project Link: [https://github.com/ChitwanRana/Advertise](https://github.com/ChitwanRana/Advertise)

---

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Bootstrap Icons](https://icons.getbootstrap.com/)
- Food Safety and Standards Authority of India (FSSAI)
- All contributors and users of this project

---

## 📞 Support

If you have any questions or run into issues, please:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the Django documentation

---

## 🗺️ Roadmap

- [x] Basic upload and preview functionality
- [x] Review and rating system
- [x] Responsive UI with Bootstrap
- [x] AI-generated design ideas
- [ ] User authentication and profiles
- [ ] PDF label export
- [ ] Advanced label customization tools
- [ ] Template marketplace
- [ ] Real-time collaboration
- [ ] Analytics dashboard
- [ ] Multi-language support
- [ ] Mobile app (React Native)

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

Made with ❤️ by [Chitwan Rana](https://github.com/ChitwanRana)

</div>