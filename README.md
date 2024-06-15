# csv_data_visualization_django_ML

## Overview

This project is a Django-based web application designed for performing data analysis on CSV files uploaded by users. It utilizes pandas and numpy for data processing tasks and matplotlib for generating basic visualizations. The application provides a user-friendly interface to upload CSV files, analyze data, and visualize insights directly on the web interface.

## Features

- File upload feature for CSV files.
- Data analysis capabilities:
  - Displaying initial rows of data.
  - Calculating summary statistics (mean, median, standard deviation).
  - Handling missing values.
- Data visualization using matplotlib integrated with pandas:
  - Histograms for numerical columns.
- Simple and intuitive web interface using Django templates.

## Setup Instructions

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/PsyCProgrammer/csv_data_visualization_django_ML.git
   cd projectname
   ```

2. **Set up virtual environment (optional but recommended):**

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. **Install dependencies:**

```bash
pip install Django pandas numpy matplotlib
```

4. **Apply database migrations:**

```bash
python manage.py migrate
```

5. **Run the development server:**

```bash
python manage.py runserver
```
