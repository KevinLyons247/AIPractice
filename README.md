# AI Chat Assistant

A simple yet powerful AI chat application that I built to interact with OpenAI's GPT-3.5 model. This project features a clean, modern web interface where users can have natural conversations with an AI assistant.

## Features

-  Clean and modern user interface
-  Real-time AI responses using GPT-3.5
-  Fast and responsive design
-  Loading states and error handling
-  Mobile-friendly layout

## Tech Stack

- Python 3.13
- Flask for the web framework
- OpenAI API for AI capabilities
- HTML/CSS/JavaScript for the frontend
- Python-dotenv for environment management

## Getting Started

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
   You can get an API key from [OpenAI's platform](https://platform.openai.com/api-keys)

4. Run the application:
   ```bash
   python main.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000`

## How It Works

The application uses Flask to serve a web interface where users can input their messages. When a message is submitted, it's sent to the OpenAI API using GPT-3.5-turbo model, which processes the input and returns a response. The response is then displayed to the user in real-time.

## Future Improvements

- [ ] Add conversation history
- [ ] Implement different AI models
- [ ] Add user authentication
- [ ] Support for file uploads
- [ ] Add voice input/output
