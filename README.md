# AI-Powered Patient Management System
Project Overview

An AI-powered Patient Management System developed using FastAPI, Streamlit, and open-source Hugging Face Large Language Models (LLMs).
The application enables CRUD operations, BMI-based health analysis, and AI-driven medical recommendations using locally cached open-source models with offline inference support.

## Technical Stack

Backend
- FastAPI
- Python
- Pydantic (data validation, computed fields)
- REST API architecture

Frontend
- Streamlit
- HTTP client integration (requests)

AI / Machine Learning
- Hugging Face Transformers
- Open-source LLM (Phi-3 Mini)
- Prompt-based inference
- Local model caching
- Offline inference capability

Data Storage
- JSON-based persistence

## System Architecture

![image alt](https://github.com/Chintan1545/Patient-Management-System/blob/4d80792d61f0625975af29afcafccb3a9e8bc740/Image.png)

## Core Functionalities

Patient Management
- Create patient records
- Read and view patient details
- Update patient information
- Delete patient records
- Input validation using Pydantic

Health Metrics
- Automatic BMI calculation
- Health verdict classification
- Dynamic recalculation on data updates

AI Health Advisor
- AI-driven health risk analysis
- Personalized diet recommendations
- Exercise suggestions
- Medical caution indicators
- Prompt engineering for healthcare context

AI Model Implementation
- Model Name: microsoft/phi-3-mini-4k-instruct
- Framework: Hugging Face Transformers
- Deployment Type: Local inference
- Optimization: Model loaded once at application startup
- Caching: Persistent local cache to prevent repeated downloads
- Cost: Free (no paid APIs)

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /view | Retrieve all patient records |
| GET | /patient/{id} | Retrieve a single patient |
| POST | /create | Create new patient |
| PUT | /edit/{id} | Update patient data |
| DELETE | /delete/{id} | Delete patient |
| GET | /ai/health-advice/{id} | AI-based health recommendations |

## Installation and Execution

Clone Repository
- git clone https://github.com/your-username/ai-patient-management-system.git
 cd ai-patient-management-system

Install Dependencies
- pip install fastapi uvicorn streamlit transformers torch requests

Run Backend (FastAPI)
- cd backend - uvicorn main:app

Run Frontend (Streamlit)
- cd frontend - streamlit run app.py

## Performance Optimization
- Local caching of Hugging Face model
- Global model initialization
- Reduced inference latency
- Offline execution support
