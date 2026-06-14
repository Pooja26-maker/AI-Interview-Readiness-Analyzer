# 🚀 AI Interview Readiness & Skill Gap Analyzer

An AI-powered web application that analyzes resumes against job descriptions, identifies skill gaps, calculates interview readiness, and generates personalized interview preparation recommendations.

## 📌 Project Overview

The AI Interview Readiness & Skill Gap Analyzer helps job seekers evaluate their resumes against a target job description. The system identifies missing skills, calculates a readiness score, generates adaptive interview questions, and provides personalized learning recommendations.

## ✨ Features

- 📄 Resume Upload (PDF)
- 💼 Job Description Analysis
- 🔍 Skill Gap Detection
- 🎯 Interview Readiness Score (0–100)
- 🤖 AI-Powered Interview Questions
- 🧠 Technical Questions Generation
- 👥 Behavioral Questions Generation
- 💬 HR Interview Questions
- 📚 Personalized Learning Roadmap
- 💡 Improvement Suggestions
- 🌐 Interactive Web Interface

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Model
- Groq API
- Llama 3.3 70B Versatile

### Libraries
- PDFPlumber
- Streamlit
- Groq

## 📂 Project Structure

```text
AI-Interview-Readiness-Analyzer/
│
├── app.py
├── skills.py
├── prompts.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Pooja26-maker/AI-Interview-Readiness-Analyzer.git
```

### Move into Project Folder

```bash
cd AI-Interview-Readiness-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

## 🔑 API Configuration

Replace the placeholder API key inside `app.py`:

```python
client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)
```

Get your API key from:

https://console.groq.com

## 🚀 How It Works

1. Upload Resume (PDF)
2. Paste Job Description
3. System extracts skills from Resume
4. System extracts required skills from Job Description
5. Skill gaps are identified
6. Readiness Score is calculated
7. AI generates:
   - Technical Questions
   - Behavioral Questions
   - HR Questions
   - Learning Roadmap
   - Improvement Suggestions

## 📊 Example Output

### Readiness Score

```text
Readiness Score: 78%
```

### Missing Skills

```text
Docker
AWS
MongoDB
REST API
```

### Learning Roadmap

```text
Week 1: Learn Docker
Week 2: Learn AWS
Week 3: Learn MongoDB
Week 4: Learn REST API
```

## 🎯 Future Enhancements

- Resume ATS Score Analysis
- PDF Report Generation
- Skill Match Visualization Charts
- Job Recommendation System
- Multi-Resume Comparison
- Deployment on Streamlit Cloud

## 👩‍💻 Author

**Pooja S**

B.Tech Information Technology

Passionate about Full Stack Development, Artificial Intelligence, and Problem Solving.

## 📜 License

This project is developed for educational and learning purposes.
