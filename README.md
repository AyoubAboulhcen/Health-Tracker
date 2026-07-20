# 🏢 US Business Lead Scraper

<p align="center">
  <strong>Generate clean business leads using Google's official Places API.</strong>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Google Places API](https://img.shields.io/badge/API-Google%20Places-success)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-blue)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-Excel-green)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

</p>

---

## 📖 Overview

Finding business leads manually is time-consuming and inefficient.

This project automates the process by collecting business information directly from the **Google Places API (New)** and exporting clean, structured Excel files ready for sales outreach, CRM systems, or market research.

Unlike traditional web scrapers, this project uses Google's official Places API, making it reliable, scalable, and compliant with Google's Terms of Service.

---

# ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 Business Search | Search any business category |
| 🌎 Multi-City Support | Search businesses across multiple cities |
| 📄 Automatic Pagination | Retrieve complete search results |
| ♻ Duplicate Removal | Remove duplicate businesses automatically |
| 🔗 URL Cleaning | Remove unnecessary tracking parameters |
| 📊 Excel Export | Export clean XLSX files |
| 🔄 Retry Logic | Handle temporary network failures |

---

# 💼 Business Value

This tool helps users:

- Save hours of manual research
- Generate clean business lead lists
- Prepare outreach campaigns
- Build CRM-ready datasets
- Research local markets
- Collect verified business information

---

# 📦 Exported Data

Each business record may include:

- Business Name
- Address
- Phone Number
- Website
- Google Rating
- Review Count

---

# 🛠 Tech Stack

- Python
- Google Places API (New)
- Requests
- Pandas
- OpenPyXL

---

# 📁 Project Structure

```text
us-business-lead-scraper/

├── Alabama.py
├── California.py
├── debug.py
├── README.md
└── .gitignore
```

---

# 🚀 Quick Start

Clone the repository

```bash
git clone https://github.com/AyoubAboulhcen/us-business-lead-scraper.git
```

Install dependencies

```bash
pip install requests pandas openpyxl
```

Set your Google Places API key

```text
GOOGLE_PLACES_API_KEY=your_api_key
```

Run the scraper

```bash
python Alabama.py
```

---

# 🔄 Workflow

```text
Business Category
        │
        ▼
Google Places API
        │
        ▼
Automatic Pagination
        │
        ▼
Data Cleaning
        │
        ▼
Duplicate Removal
        │
        ▼
Excel Export
```

---

# 💡 Technical Highlights

This project demonstrates experience with:

- REST API integration
- JSON data processing
- Pagination handling
- Data cleaning
- Excel report generation
- Error handling
- Retry mechanisms
- Modular Python development

---

# 🔮 Future Improvements

- CSV export
- Multi-state execution
- Command-line arguments
- Configuration file support
- Logging
- Parallel requests

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Ayoub Aboulhcen**

Python Developer specializing in:

- Python Automation
- Data Processing
- Excel Automation
- Business Automation
- API Integration

GitHub: https://github.com/AyoubAboulhcen
