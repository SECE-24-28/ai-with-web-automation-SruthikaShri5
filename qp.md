AI Question Paper Generator using Gemini & ChromaDB
Overview

AI Question Paper Generator is an intelligent system that automatically generates university-level question papers from a syllabus PDF. The system analyzes the uploaded syllabus, extracts relevant topics, and generates a complete question paper following the examination pattern specified by the institution.

This project is designed to reduce the manual effort involved in preparing examinations while ensuring proper syllabus coverage and balanced question distribution.

Features
Core Features
Upload syllabus PDF
Automatic syllabus text extraction
AI-powered question generation using Gemini
Generates question papers according to Sri Eshwar College examination pattern
Automatic PDF generation
Downloadable question paper
Coverage of all syllabus units
Duplicate question avoidance
Advanced Features (Future Scope)
ChromaDB integration for syllabus retrieval
Multiple question paper sets (Set A, Set B, Set C)
Difficulty selection (Easy, Medium, Hard)
Bloom's Taxonomy Mapping
Course Outcome (CO) Mapping
Answer Key Generation
Marking Scheme Generation
Faculty Login System
Question Bank Management
Problem Statement

Creating university examination question papers manually is a time-consuming process. Faculty members must ensure:

Complete syllabus coverage
Proper mark distribution
Appropriate difficulty levels
No duplicate questions
Compliance with institutional examination patterns

This project automates the entire process using Artificial Intelligence.

System Architecture

Syllabus PDF
↓
PDF Text Extraction
↓
Text Processing
↓
ChromaDB Knowledge Storage
↓
Relevant Topic Retrieval
↓
Gemini AI
↓
Question Paper Generation
↓
PDF Creation
↓
Download

Examination Pattern Supported
Sri Eshwar College of Engineering

Duration: 3 Hours

Maximum Marks: 100

PART A – (10 × 2 = 20 Marks)
10 Questions
2 Marks Each
PART B – (5 × 16 = 80 Marks)

Questions 11–15

Internal Choice Pattern
OR Questions
Descriptive University-Level Questions

Total Marks = 100

Technologies Used
Programming Language
Python
Artificial Intelligence
Google Gemini API
Vector Database
ChromaDB
PDF Processing
PyPDF
PDF Generation
ReportLab
Development Environment
Google Colab
Installation

Install required packages:

pip install google-genai
pip install chromadb
pip install pypdf
pip install reportlab
Usage
Step 1

Upload syllabus PDF.

Step 2

Extract syllabus content.

Step 3

Generate question paper using Gemini AI.

Step 4

Create PDF.

Step 5

Download generated question paper.

Project Workflow
User uploads syllabus PDF.
System extracts text from PDF.
Syllabus content is processed and stored.
Relevant topics are retrieved.
Gemini generates questions according to the examination pattern.
Generated questions are formatted.
Question paper PDF is created.
User downloads the final question paper.
Folder Structure
AI-Question-Paper-Generator
│
├── syllabus/
│   └── syllabus.pdf
│
├── output/
│   └── Question_Paper.pdf
│
├── main.py
├── README.md
│
└── requirements.txt
Future Enhancements
Faculty Dashboard
Subject-wise Question Bank
Automatic Answer Key Generation
Multiple University Pattern Support
Difficulty-Based Question Selection
AI Evaluation Rubrics
Student Assessment Analytics
Advantages
Saves faculty time
Reduces manual work
Ensures syllabus coverage
Generates university-standard questions
Supports automated examination preparation
Easy to use and scalable
Applications
Universities
Engineering Colleges
Schools
Online Learning Platforms
Coaching Centers
Competitive Examination Institutes
