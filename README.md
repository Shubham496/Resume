# Shubham Singh — Data Analyst & BI Portfolio

A responsive, production-ready Django portfolio website built to showcase business intelligence, analytics, and data modeling work (Power BI, Tableau, Advanced Excel, and SQL). 

Designed for low memory footprint and simple deployment on [PythonAnywhere](https://www.pythonanywhere.com/).

---

## 🌟 Key Features

- **Personalized Showcase Projects:**
  - **Power BI:** Interactive reports or embeds, DAX measures, and retail sales analytics.
  - **Tableau:** Visual dashboards, calculated fields, and demographic storytelling.
  - **Excel Models:** Multi-scenario financial forecasts, dynamic arrays, and executive slicers.
- **Project Detail Pages (`/projects/<slug>/`):**
  - Live interactive `<iframe>` dashboard embeds (Power BI / Tableau Public / OneDrive Excel).
  - One-click source file downloads (`.pbix`, `.twbx`, `.xlsx`).
  - Technical methodology and highlight bullet points.
- **Dynamic Résumé (`/resume/`):**
  - Experience timeline (Ducat Jaipur, LNP Infotech, Netmax Technologies, JKM Amusements).
  - Education & Certifications (Udemy, Coursera).
  - Categorized proficiency bars across BI tools, databases, SQL, and automation.
- **Direct Contact Hub (`/contact/`):** Pre-linked phone, email, LinkedIn, and GitHub.
- **Django Admin Source of Truth:** Manage projects, upload cover images, add file downloads, and update experience entries directly via `/admin/`.

---

## 🗂️ Project Structure

```text
resume/
│
├── portfolio_hub/              # Project settings & root routing
│   ├── settings.py             # Development settings (DEBUG=True)
│   ├── deployment.py           # Production settings for PythonAnywhere (DEBUG=False, SSL)
│   ├── urls.py                 # URL dispatcher
│   └── wsgi.py                 # Default WSGI entrypoint
│
├── portfolio/                  # Core portfolio app
│   ├── models.py               # Project, Skill, Experience, Education, Certification
│   ├── views.py                # Landing, Resume, Projects List, Project Detail, Contact
│   ├── urls.py                 # Routes: /, /resume/, /projects/, /projects/<slug>/, /contact/
│   ├── admin.py                # Django admin configuration
│   └── tests.py                # Automated test suite
│
├── templates/                  # HTML templates (Bootstrap 5)
│   ├── base.html               # Shared navbar, footer, scripts
│   └── portfolio/
│       ├── landing.html        # Home / hero section / featured project cards
│       ├── resume.html         # Full interactive resume
│       ├── projects_list.html  # Gallery with Power BI / Tableau / Excel filters
│       ├── project_detail.html # Case study with dashboard iframe & download button
│       └── contact.html        # Contact coordinates
│
├── static/                     # Static files (CSS, images, icons, PDF resume)
│   ├── css/main.css
│   ├── images/                 # Put your profile.jpg here
│   └── files/                  # Put your resume.pdf here
│
├── media/                      # Uploaded files via Django Admin
│   ├── projects/               # Project screenshots / thumbnails
│   └── project_files/          # Downloadable .pbix, .twbx, .xlsx files
│
├── .env                        # Local secrets (gitignored)
├── .env.example                # Example environment file
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
└── wsgi_pythonanywhere.py      # WSGI configuration snippet for PythonAnywhere
```

---

## 🚀 Quickstart (Local Development)

### 1. Prerequisites
- Python 3.10+
- Git

### 2. Setup Virtual Environment & Install Dependencies
```bash
# Optional: create a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Ensure `SECRET_KEY` is present.

### 4. Database Migrations & Superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the Local Server
```bash
python manage.py runserver
```
Visit:
- Website: `http://127.0.0.1:8000/`
- Admin Panel: `http://127.0.0.1:8000/admin/`

---

## 📊 How & Where to Put Your Projects

You don't need to touch template code to add or update your projects. Everything is managed via the **Django Admin Panel** at `http://127.0.0.1:8000/admin/portfolio/project/`.

### What to Fill in for Each Project:

| Field | What to Put | Example / Instructions |
| :--- | :--- | :--- |
| **Title** | The project name | `Adidas Retail Sales Performance Dashboard` |
| **Slug** | URL-friendly identifier | `adidas-retail-dashboard` (auto-filled) |
| **Project Type** | Choose from dropdown | `Power BI`, `Tableau`, or `Excel Model` |
| **Summary** | 2–3 sentences about the business goal | What business problem did this solve? |
| **Key Highlights** | Bullet points (1 per line) | Methodology, DAX formulas, Star Schema, XLOOKUP logic |
| **Image** *(Optional)* | Dashboard screenshot | Click **Choose File** & upload `.png` or `.jpg` |
| **Embed URL** *(Optional)* | `<iframe>` URL for interactive view | See the embed guide below |
| **Download File** *(Optional)* | The actual project file | Attach your `.pbix`, `.twbx`, or `.xlsx` file |
| **External URL** *(Optional)* | Direct link | Link to Tableau Public, GitHub repo, or Drive |
| **Is Featured** | Check the box | Shows it on the main landing page |

---

### How to Get the `Embed URL` for Each Tool:

#### 1. Power BI
- In Power BI Service: **File** &rarr; **Embed report** &rarr; **Publish to web (public)**.
- Copy the URL inside `src="..."` (e.g., `https://app.powerbi.com/view?r=eyJrIj...`).
- Paste that URL into the **Embed URL** field in Django Admin.

#### 2. Tableau
- Publish your workbook to **Tableau Public**.
- Open the dashboard, click **Share**, and copy the link.
- Add `?:showVizHome=no&:embed=true` to the end of the URL (e.g. `https://public.tableau.com/views/WorkbookName/DashboardName?:showVizHome=no&:embed=true`).
- Paste that URL into the **Embed URL** field in Django Admin.

#### 3. Excel
- Upload the `.xlsx` file to **OneDrive** or **SharePoint**.
- Open the file in Excel Online &rarr; **File** &rarr; **Share** &rarr; **Embed**.
- Copy the `src="..."` link from the embed code and paste it into the **Embed URL** field.
- *Alternatively:* Simply upload the file to **Download File** in Django Admin so recruiters can download and inspect it directly.

---

### Where to Put Static Assets:
- **Profile Photo:** Place your photo in `static/images/profile.jpg`.
- **Downloadable PDF Résumé:** Place your resume PDF in `static/files/resume.pdf`.

---

## ☁️ Deployment on PythonAnywhere

1. **Push your code to GitHub:**
   ```bash
   git remote add origin https://github.com/Shubham469/<repo-name>.git
   git branch -M main
   git push -u origin main
   ```
2. **On PythonAnywhere:**
   - Open a **Bash Console**:
     ```bash
     git clone https://github.com/Shubham469/<repo-name>.git portfolio_hub
     cd portfolio_hub
     mkvirtualenv myenv --python=python3.10
     pip install -r requirements.txt
     python manage.py migrate
     python manage.py createsuperuser
     python manage.py collectstatic
     ```
   - In the **Web** tab:
     - Set Virtualenv: `/home/yourusername/.virtualenvs/myenv`
     - Open the **WSGI configuration file** and replace contents with `wsgi_pythonanywhere.py` (update `yourusername` and `SECRET_KEY`).
     - Under **Static files**, add mappings:
       - URL: `/static/` &rarr; Directory: `/home/yourusername/portfolio_hub/staticfiles/`
       - URL: `/media/` &rarr; Directory: `/home/yourusername/portfolio_hub/media/`
   - Click **Reload**!
