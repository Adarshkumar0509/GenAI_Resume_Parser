# 🤖 GenAI Resume Parser
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/bhanukumardev/GenAI_Resume_Parser) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/) [![Groq](https://img.shields.io/badge/Groq-00AEEF?logo=databricks&logoColor=white)](https://groq.ai/) [![Stars](https://img.shields.io/github/stars/bhanukumardev/GenAI_Resume_Parser?style=social)](https://github.com/bhanukumardev/GenAI_Resume_Parser/stargazers)

> AI-powered resume parser using Flask and Groq — Extract structured insights from PDF resumes with a Groq LLM backend.

## 🚀 Overview

A cutting-edge resume parsing solution that leverages **Generative AI** to extract structured information from PDF resumes. Built as part of Pinnacle Labs Internship, this project demonstrates:

- **AI Backend** - Use Groq API for model inference
- **Intelligent Parsing** - Extracts name, email, skills, experience, education
- **Flexible Deployment** - Cloud or on-premises AI models
- **Simple Interface** - Clean Flask web application

## 💻 Live Demo

🌐 **Try it now:** [https://genai-resume-parser.onrender.com/](https://genai-resume-parser.onrender.com/)

Test the resume parser directly in your browser! Upload your PDF resume and get structured insights instantly.

## ✨ Features

- 📄 **PDF Resume Upload** - Drag & drop or select files
- 🤖 **AI Extraction** - Intelligent parsing using LLMs
- 🌐 **AI Model**
  - ☁️ Groq API (cloud)
- **Structured Output** - JSON format with key resume fields
- ⚡ **Fast Processing** - Optimized for quick results
- 🔒 **Privacy Options** - Use hosted Groq or replace with a private/on-prem model depending on your privacy needs

## 🛠️ Tech Stack

### Backend
- **Framework:** Flask (Python)
- **PDF Processing:** PyPDF2 / pdfplumber
**AI Models:**
  - Groq API (recommended for this fork)

### Frontend
- **HTML/CSS/JavaScript**
- **Bootstrap** for responsive design
- **AJAX** for async file uploads

### AI Integration
- **LangChain** - AI orchestration
- **Prompt Engineering** - Optimized extraction prompts
- **Error Handling** - Robust fallback mechanisms

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Groq API key

### 1. Clone Repository
```bash
git clone https://github.com/bhanukumardev/GenAI_Resume_Parser.git
cd GenAI_Resume_Parser
```

### 2. Install Dependencies
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Configure AI Models (Groq)
This fork uses Groq's inference API as the LLM provider. You'll need a Groq API key.

Create a `.env` file with the following variables (you can also set these in your environment):

```bash
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3-8b  # or another model you have access to
MODEL_TYPE=groq
```

Optional: if you need to override the API endpoint (e.g., private deployment):

```bash
GROQ_API_ENDPOINT=https://api.groq.com/v1/chat/completions
```

### 4. Run the Application
```bash
# Start Flask app
python app.py
# Access at http://localhost:8000
```

## 🎯 Usage Example

### Web Interface
1. Open `http://localhost:8000` in your browser
2. Upload a PDF resume
3. Click "Parse Resume"
4. View extracted information in structured JSON format

### API Usage
```python
import requests

# Upload and parse resume
with open('resume.pdf', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/parse', files=files)
    resume_data = response.json()
    print(resume_data)
```

### Example Output
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+1-234-567-8900",
  "skills": ["Python", "Machine Learning", "Flask", "AI"],
  "experience": [
    {
      "company": "Tech Corp",
      "position": "Software Engineer",
      "duration": "2020-2023"
    }
  ],
  "education": [
    {
      "degree": "B.Tech in Computer Science",
      "institution": "University Name",
      "year": "2020"
    }
  ]
}
```

## 📊 Supported Fields
- 👤 Personal Information (Name, Email, Phone, LinkedIn)
- 🎓 Education (Degree, Institution, Year, GPA)
- 💼 Work Experience (Company, Role, Duration, Responsibilities)
- 🛠️ Technical Skills (Programming, Tools, Frameworks)
- 🏆 Certifications and Awards
- 📋 Projects and Publications

## 📁 Project Structure
```
GenAI_Resume_Parser/
├── app.py                 # Main Flask application
├── ai_parser.py           # Resume parsing logic (Groq integration)
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── uploads/               # Temporary resume storage
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # Project documentation
```

## 🔒 Privacy & Security
- **Local Processing:** This fork uses Groq's hosted API; for on-prem alternatives adapt the parser accordingly.
- **No Data Storage:** Uploaded resumes are processed and deleted
- **Secure API Keys:** Environment variables for credentials
- **GDPR Compliant:** No personal data retention

## 🤝 Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

### Adarsh Kumar
- GitHub: [@Adarshkumar0509](https://github.com/Adarshkumar0509)
- LinkedIn: [Adarsh Kumar](https://www.linkedin.com/in/adarshkumar0509)

## 🌟 Acknowledgments
- **Groq** - For hosted LLM inference used in this fork
- **Ollama Team** - (original project) local AI deployment tools — removed in this fork
- **Flask Community** - For excellent documentation

## 📈 Future Enhancements
- [ ] Support for DOCX and other formats
- [ ] Batch processing capabilities
- [ ] Advanced resume scoring
- [ ] Integration with ATS systems
- [ ] Multi-language support
- [ ] Resume comparison features

---

⭐ Star this repo if you find it helpful!

Empowering recruitment with AI-driven insights

Made with ❤️ by Adarsh Kumar
