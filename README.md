# Cold Email Generator using Llama 3.3

This project is a Cold Email Generator designed to automate and streamline the process of generating personalized cold emails for job/internship applications. By leveraging advanced natural language models, including Llama 3.3, along with tools like **Gorqclud**, **Streamlit**, **uuid**, and **Langchain**, this tool extracts relevant details from a job listing URL and creates a tailored email. Additionally, it maps your portfolio to relevant job opportunities to improve the chances of landing an internship.

## Features

- **Job Detail Extraction**: Automatically scrapes relevant information (skills, role, experience, etc.) from job listing URLs.
- **Cold Email Generation**: Uses Llama 3.3 for creating personalized cold emails tailored to the job description.
- **Portfolio Mapping**: Maps your portfolio items to the relevant job opportunities, enhancing your chances of getting noticed.
- **Streamlit Deployment**: The application is deployed using Streamlit, providing an easy-to-use interface for users.

## Technologies Used

- **Llama 3.3**: A state-of-the-art language model for generating natural, context-aware cold emails.
- **Gorqclud**: A web scraping tool used to extract job details from URLs.
- **Streamlit**: Framework for deploying the application and providing a user-friendly interface.
- **uuid**: Used for generating unique identifiers for each session or email generation request.
- **Langchain**: Helps in orchestrating complex chains of operations and logic for natural language processing.

## Installation

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.7+
- pip (Python package installer)

### Step-by-Step Guide

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cold-email-generator.git

2. Navigate to the project directory:

    ```bash
    cd cold-email-generator

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

4. Run the application locally:
    ```bash
    streamlit run ./app/main.py

5. Open the provided local URL (usually http://localhost:8501) in your web browser to use the application.

## Usage

Enter Job URL: Provide the URL of the job listing (internship or full-time role).
Portfolio Mapping: Upload your portfolio or resume link, and the tool will map your portfolio to the job description.
Generate Cold Email: Once the details are extracted, click the "Submit" button, and a personalized cold email will be created for you.
Send: Copy the generated email and send it to the hiring manager or recruiter.


## Deployment
This application is deployed using Streamlit, and you can easily deploy it to your own server or cloud service like Heroku or AWS for production.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

