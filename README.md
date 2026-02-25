# Sort Integers by The Number of 1 Bits

This application sorts an array of integers by the number of 1s in their binary representation. In case of ties, it sorts them in ascending order.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Problem Link

[https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)

## Architecture

The application consists of a React frontend and a Python/Flask backend.
The frontend provides a user interface for inputting an array of integers.
The backend provides a RESTful API for sorting the integers.

## Setup

### Backend

1.  Clone the repository.
2.  Navigate to the `backend` directory.
3.  Create a virtual environment: `python3 -m venv venv`
4.  Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
5.  Install the dependencies: `pip install -r requirements.txt`
6.  Run the Flask application: `python app.py`

### Frontend

1.  Navigate to the `frontend` directory.
2.  Install the dependencies: `npm install`
3.  Start the React development server: `npm start`

## Usage

1.  Open the React application in your browser (usually at `http://localhost:3000`).
2.  Enter a comma-separated list of integers in the input field.
3.  Click the "Sort" button.
4.  The sorted array will be displayed in the output area.

## References

*   LeetCode: [https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)
*   React: [https://react.dev/](https://react.dev/)
*   Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

This is an open-source project, and contributions are welcome!
