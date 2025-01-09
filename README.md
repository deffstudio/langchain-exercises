# LangChain Exercises Collection

This repository contains a collection of exercises demonstrating various concepts and models using LangChain. Each exercise showcases different features and capabilities of LangChain, such as text translation, prompt templates, and streaming responses.

## Features

- **Environment Setup**: Load environment variables using `dotenv`.
- **Language Model Usage**: Utilize the `ChatOpenAI` model for text translation.
- **Prompt Templates**: Create and use prompt templates for structured input to the language model.
- **Streaming**: Stream responses from the language model.

## Getting Started

1. **Clone the repository**:

   ```sh
   git clone https://github.com/deffstudio/langchain-exercises.git
   cd langchain-exercises
   ```

2. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory and add your API keys:

   ```env
   OPEN_API_KEY=your_openai_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   ```

4. **Run the Jupyter Notebook**:
   ```sh
   jupyter notebook 1.simple_llm_app.ipynb
   ```

## Usage

- Follow the steps in the Jupyter Notebooks to learn how to use different language models and prompt templates.
- Modify the prompt templates and messages to customize the exercises for different use cases.

## License

This project is licensed under the MIT License.
