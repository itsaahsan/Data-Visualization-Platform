# 📊 Data Visualization Dashboard

[![Flask](https://img.shields.io/badge/Flask-3.0.0-red)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.x-green)](https://plotly.com/python/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](#license)
[![Maintenance](https://img.shields.io/badge/Maintenance-Active-brightgreen)](#contributing)

A powerful, **professional-grade data visualization dashboard** built with Flask and Plotly. Create stunning, interactive charts from your data with an intuitive interface similar to Tableau or Google Data Studio.

**Live Demo**: Run `python app.py` and visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

![Dashboard Preview](https://via.placeholder.com/800x400/007bff/ffffff?text=Interactive+Data+Dashboard)

## ✨ Key Features

### 📁 **Multiple Data Sources**
- **CSV Files**: Standard comma-separated values
- **Excel Files**: .xlsx and .xls formats (via OpenPyXL)
- **JSON Files**: JavaScript Object Notation

### 📊 **Interactive Chart Types**
- **Bar Charts**: Compare categorical data visually
- **Line Charts**: Display trends over time or categories
- **Scatter Plots**: Reveal correlations between variables
- **Pie Charts**: Show proportional data distribution
- **Histograms**: Analyze data distribution and frequency

### 🎯 **Professional Features**
- **Real-time Chart Generation**: AJAX-powered instant visualization
- **Multi-chart Dashboards**: Combine multiple charts per session
- **Responsive Design**: Bootstrap-powered mobile-friendly interface
- **Smart Data Analysis**: Automatic column type detection
- **Custom Favicon**: Professional chart icon for branding

### 🔧 **Technical Excellence**
- **Secure File Upload**: Validated file types and size limits (16MB)
- **Error Handling**: Graceful failure messages and recovery
- **Clean URLs**: RESTful API endpoints
- **Cross-browser Compatibility**: Works on all modern browsers

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
  ```bash
  # Check Python version
  python --version
  ```

- **pip** package manager
  ```bash
  # Upgrade pip to latest version
  python -m pip install --upgrade pip
  ```

### Installation

1. **Clone or Download** this repository:
   ```bash
   cd your-projects-directory
   # Copy files from this project
   ```

2. **Create Virtual Environment** (recommended):
   ```bash
   python -m venv .venv
   # Activate on Windows
   .venv\Scripts\activate
   # Activate on macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   # Or install individually for reliability:
   pip install Flask>=2.3.0 Plotly>=5.19.0 Pandas>=1.5.0 OpenPyXL>=3.1.2
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```
   You'll see: `* Running on http://127.0.0.1:5000`

5. **Open in Browser**:
   Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📋 Usage Guide

### Step 1: Upload Your Data
- Click **"Choose File"** and select your dataset
- Supported formats: .csv, .xlsx, .xls, .json
- Maximum file size: 16MB
- File is validated before processing

### Step 2: Explore Your Data
After upload, you'll see:
- **File Summary**: Dataset dimensions and filename
- **Row Count**: Total number of data rows
- **Column Count**: Total number of data columns
- **Data Types**: Breakdown of numeric vs categorical columns

### Step 3: Create Visualizations

#### Chart Configuration Options:
- **Chart Type**: Select from 5 available chart types
- **X-Axis**: Choose your primary data column
- **Y-Axis**: Select measurement column (if applicable)
- **Color By**: Optional categorical grouping for color coding

#### Interactive Features:
- **Hover Information**: Detailed data on mouse hover
- **Zoom & Pan**: Click and drag to explore chart areas
- **Legend Control**: Show/hide data series
- **Download Options**: Export charts as images

### Step 4: Build Multi-Chart Dashboards
- Add multiple charts to analyze different data aspects
- Each chart maintains independent configuration
- Remove unwanted charts with the "×" button
- Clear all charts with the "Clear All" button

## 🔍 API Reference

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Homepage with file upload form |
| `POST` | `/upload` | Process and validate uploaded files |
| `GET` | `/dashboard/<filename>` | Visualization dashboard for uploaded data |
| `POST` | `/api/generate_chart/<filename>` | Generate interactive charts via AJAX |

### Sample API Request

```javascript
// Generate a bar chart
const response = await fetch('/api/generate_chart/yourdata.csv', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        chart_type: 'bar',
        x_column: 'Category',
        y_column: 'Sales',
        color_column: 'Region'
    })
});
```

## 🏗️ Architecture

### Backend Architecture

```
Flask Web Server (app.py)
├── Flask Routes
│   ├── Static Files (CSS, JS, Favicon)
│   ├── HTML Templates (Jinja2)
│   └── API Endpoints
├── Data Processing
│   ├── Pandas DataFrames
│   ├── File Type Detection
│   └── Data Validation
└── Chart Generation
    ├── Plotly Graph Objects
    ├── JSON Response
    └── Interactive Widgets
```

### Frontend Architecture

```
HTML5 Pages
├── index.html (Landing Page)
├── dashboard.html (Visualization Hub)
└── Bootstrap Framework

JavaScript Components
├── AJAX Chart Generation
├── Dynamic Form Controls
└── Interactive Chart Management
```

## 📁 Project Structure

```
data-viz-dashboard/
├── app.py                    # 🚀 Main Flask application & API
├── requirements.txt          # 📦 Python dependencies
├── test_data.csv            # 🧪 Sample dataset for testing
├── comprehensive_test.py    # ✅ Full application testing suite
├── verify.py               # 🔍 Basic verification script
├── README.md              # 📖 This documentation
├── pyrightconfig.json     # ⚙️ Python type checking config
├── templates/             # 🎨 Frontend templates
│   ├── index.html         # 🏠 Main upload page
│   └── dashboard.html     # 📊 Visualization interface
├── static/                # 🗄️ Static assets
│   ├── favicon.svg        # 🎨 Professional favicon
│   ├── css/
│   │   └── style.css      # 🎨 Responsive styling
│   └── js/
│       └── dashboard.js   # ⚡ Chart generation logic
└── data/                  # 💾 Uploaded files (auto-generated)
    └── uploads/           # 📁 Timestamped uploaded files
```

## 🧪 Testing & Quality Assurance

### Run All Tests
```bash
python comprehensive_test.py
```

### Test Results ✨
- ✅ **Dependencies**: All packages verified and working
- ✅ **Application Startup**: Flask routes and configuration
- ✅ **Frontend Assets**: All HTML, CSS, and JS files
- ✅ **Data Processing**: CSV/Excel/JSON handling
- ✅ **File Upload**: Security and validation
- ✅ **Chart Generation**: All chart types functional
- ✅ **Error Handling**: Proper failure management
- ✅ **HTTP Endpoints**: API availability

### Sample Test Data
Use `test_data.csv` (included) to test all features:
- 10 rows × 5 columns
- Mixed data types (string, numeric)
- Regional sales data with categories

## 🔒 Security Features

- **File Type Validation**: Only allowed extensions processed
- **Secure Filename Generation**: Timestamp + random naming
- **Size Limits**: 16MB maximum file upload
- **XSS Protection**: Flask's built-in CSRF protection
- **Input Sanitization**: Automatic file path safety

## 🎨 Customization

### Change Theme Colors
Edit `static/css/style.css`:
```css
.hero-section {
    background: linear-gradient(135deg, #your-color 0%, #another-color 100%);
}
```

### Add New Chart Types
Extend `app.py` API endpoint for new visualization types.

### Customize Favicon
Replace `static/favicon.svg` with your own design.

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/new-chart-type`)
3. **Commit** your changes (`git commit -am 'Add new chart type'`)
4. **Push** to the branch (`git push origin feature/new-chart-type`)
5. **Create** a Pull Request

### Development Requirements
```bash
pip install -r requirements.txt
pip install pyright flake8 # For code quality
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask** - Light-weight WSGI web application framework
- **Plotly** - Interactive, publication-quality graphs
- **Bootstrap** - Responsive front-end framework
- **Pandas** - Powerful data manipulation library
- **OpenPyXL** - Excel file handling
- **Font Awesome** - Beautiful icons

## 📞 Support

- **Issues**: [Report bugs or request features](https://github.com/username/data-viz-dashboard/issues)
- **Documentation**: Read the full guides above
- **Performance**: Tested with datasets up to 100k rows
- **Browser Support**: Chrome 70+, Firefox 65+, Safari 12+, Edge 79+

---

<div align="center">

**Built with ❤️ using Flask, Plotly, and Python**

⭐ Star this repo if you found it useful!

[⬆️ Back to Top](#data-visualization-dashboard)

</div>