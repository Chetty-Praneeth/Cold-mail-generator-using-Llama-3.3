import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]
    

    def write_mail(self, job, links):
        # Ensure that links are formatted correctly as a string for easier display in the email
        formatted_links = "\n".join([f"- {link}" for link in links])

        prompt_email = PromptTemplate.from_template(
            """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Chetty Praneeth, a Third-year undergraduate pursuing Computer science in data science from Vignana Bharati Institute of Technologu , Hyderabad. 
        seeking an Internship opportunity with the esteemed [Company Name] a an aspiring AI and software developer with experience in 
        Python, Machine Learning, and Deep learning.
        
        Your job is to write a cold email for an internship application based on the candidate’s profile, skills, and the company’s focus.
        The email should be professional yet personalized, concise, and engaging. Use a tone that makes the recipient feel in control while
        subtly showcasing the candidate’s strengths.
        
        Structure to Follow:
        Greeting: Address the recipient professionally
        Introduction: Briefly introduce the candidate, their degree, university, and the internship they’re seeking. If they have a 
        preference, phrase it in a way that gives the company authority.
        Experience Highlights:
        Mention a major relevant experience (company name, role, key responsibilities).
        Highlight leadership roles, achievements, and projects that align with the company’s focus.
        Call to Action: Express interest in discussing further.
        Resume:
        Give Linkedin link at the end by saying Linkedin and nothing else: www.linkedin.com/in/praneeth-chetty

        End with thank you give your name.
        
        Incorporate the most relevant ones from the following links to showcase the candidate’s portfolio, resume, and LinkedIn:{link_list}
        
        Remember, you are Praneeth Chetty, a developer specializing in AI-driven automation. Do not provide a preamble.
        
        """, unsafe_allow_html=True)
        
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": formatted_links})

        # Now, display the generated email content inside a scrollable container with a maximum width to avoid overflow.
        email_content = res.content  # Store the result

        # Clear output to prevent it from being shown twice
        st.empty()  # Clears the previous content that might have been displayed

        # Add styles to ensure the email content fits inside a scrollable container
        st.markdown(
            """
            <style>
            .email-output {
                max-width: 800px;
                word-wrap: break-word;
                overflow-wrap: break-word;
                white-space: pre-wrap;
                overflow-y: auto;
            }
            </style>
            """, unsafe_allow_html=True)

        # Display the email content inside a scrollable container
        st.markdown(f'<div class="email-output">{email_content}</div>', unsafe_allow_html=True)

        return email_content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
