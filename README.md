# Hackathon Tracker

A Flask-based web application designed for students of VIT to track hackathon participation, showcase achievements, and help solo users find teams. The platform allows users to register, log in, and view personal or other users' hackathon records.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Folder Structure](#folder-structure)
- [Contributors](#contributors)
- [License](#license)

## Project Description
Hackathon Tracker is a student-focused platform where users can:
- Register using email, username, and password.
- Log in to access a home page that features subpages showcasing hackathon participation.
- Browse other users' hackathon achievements and records.
- Solo users can also find teams to participate in future hackathons.

This project is particularly designed for VIT students who want to track and display their hackathon activities in a centralized way.

## Features
- **User Registration**: Secure user registration using email and password.
- **User Dashboard**: Each user has a dashboard showing their hackathon achievements.
- **Find Teams**: Solo users can search for potential teammates.
- **Hackathon Records**: Users can view their own and others' hackathon histories and accomplishments.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hxzardd/hackathon-tracker.git

## Folder Structure
## Folder Structure

hackathon-tracker/
│
├── backend/             
│   ├── app.py              # Main Flask app
│   ├── database.db         # SQLite database
│   ├── dashboard.py        # Backend logic for dashboard
│   ├── home.py             # Backend logic for home page
│   ├── index.py            # Main index logic
│   ├── login.py            # Backend logic for user login
│   ├── logout.py           # Backend logic for user logout
│   ├── models.py           # Database models
│   └── register.py         # Backend logic for user registration
│
└── frontend/           
    ├── dashboard.html      # Dashboard page
    ├── home.html           # Home page
    ├── login.html          # Login page
    └── register.html       # Registration page


