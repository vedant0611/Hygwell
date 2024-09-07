# FastAPI Backend Service & Data Analysis

## Overview

This project includes two main components:

1. **Backend Service**: Built using FastAPI, it provides three APIs for processing web URLs, PDF documents, and querying stored content using embeddings.
2. **Data Analysis**: Analyzes web traffic data provided in the `traffic.csv` dataset to gain insights into pageviews, event distribution, geographical data, click-through rates (CTR), and correlation between clicks and pageviews.

## FastAPI Backend Service

### API Endpoints

1. **Process Web URL API**

    - **Endpoint**: `POST /process_url`
    - **Request Body**:
      ```json
      {
        "url": "https://example.com"
      }
      ```
    - **Functionality**: Scrapes content from the given URL and stores it in the database.
    - **Response**:
      ```json
      {
        "message": "URL content processed and stored successfully"
      }
      ```

2. **Process PDF Document API**

    - **Endpoint**: `POST /process_pdf`
    - **Request Body**: Form-data with file upload
    - **Functionality**: Extracts text from the uploaded PDF document and stores it in the database.
    - **Response**:
      ```json
      {
        "message": "PDF content processed and stored successfully"
      }
      ```

3. **Chat API**

    - **Endpoint**: `POST /chat`
    - **Request Body**:
      ```json
      {
        "query": "What is the main idea of the document?",
        "chat_id": "unique_chat_id"
      }
      ```
    - **Functionality**: Uses embeddings to find and return the most relevant response based on the user's query.
    - **Response**:
      ```json
      {
        "best_match": "The main idea of the document is...",
        "source": "document_source",
        "similarity_score": 0.95
      }
      ```

### Setup & Installation

1. **Clone the Repository**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**

    ```bash
    alembic upgrade head
    ```

5. **Start the FastAPI Application**

    ```bash
    uvicorn main:app --reload
    ```

6. **Use Docker for Deployment**

    Build and run the Docker container:

    ```bash
    docker build -t fastapi-service .
    docker run -d -p 8000:8000 fastapi-service
    ```

## Data Analysis

### Dataset

The dataset `traffic.csv` contains web traffic data, including:

- Pageviews
- Event types
- Geographical information

### Analysis Objectives

1. **Total and Daily Pageview Events**

    - Calculate total pageview events.
    - Determine average pageviews per day.

2. **Analysis of Other Events**

    - Count and distribution of other events.

3. **Geographical Distribution**

    - Identify countries contributing to pageviews.

4. **Click-Through Rate (CTR) Analysis**

    - Calculate overall CTR.
    - Analyze CTR variations across different links.

5. **Correlation Analysis**

    - Assess correlation between clicks and pageviews.
    - Perform statistical tests for linear and categorical relationships.

### Requirements

Ensure the following Python libraries are installed:

- pandas
- scipy

Install them using:

```bash
pip install pandas scipy
