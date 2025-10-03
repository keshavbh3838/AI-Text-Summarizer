# AI-Text-Summarizer
AI-powered Text Summarizer
Goal
This project demonstrates my motivation, effort, and creativity in building a simple AI-powered application. The app takes any article or text and generates a concise, 3-sentence summary using a powerful pre-trained AI model.

Part 1: Setup
To get this project running on your local machine, follow these steps:

Install Python: Python was already installed on my system

Create a GitHub Repo: A new repository was created on GitHub named AI-Text-Summarizer to track all my progress and code changes.

Install Dependencies: All necessary libraries are listed in a requirements.txt file. Install them by running the following command in your terminal:

pip install -r requirements.txt
(Note: The requirements.txt file includes transformers, torch, and streamlit.)

Part 2: Task
This project provides two ways to summarize text: a simple command-line tool and a web-based UI.

Command-line App
To run the command-line application, execute this command in your terminal: python text_summarizer.py
The program will prompt you to paste the text you want to summarize.

Web UI (Stretch Goal)
For an even more user-friendly experience, I built a web interface using Streamlit.
To run the web app, use this command: streamlit run app.py
This will open a new tab in your web browser with a simple UI where you can paste text and get an instant summary.

What We're Looking For: My Journey
Did you try hard and document your journey?
Yes, I did. I started with a basic idea of using rule-based summarization but quickly realized that an AI-powered model would provide far superior results. This led me to explore Hugging Face's transformers library. I documented my code and wrote detailed comments to explain each part of the process.

Did you Google/ChatGPT things and figure it out?
Absolutely. I used Google and ChatGPT to understand how to correctly implement the pipeline for summarization, specifically learning about the various models and how to fine-tune parameters like max_length and min_length to achieve a 3-sentence summary as required. This process helped me learn how to find and use the right tools for the job.

Did you go beyond the minimum?
Yes, I went beyond the minimum requirements. In addition to the requested command-line app, I developed a simple but effective web UI using Streamlit. This not only makes the application more accessible to users who aren't familiar with the command line but also demonstrates my ability to take a core concept and build a full, creative application around it.
