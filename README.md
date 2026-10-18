# AI Code Explainer & Reviewer

A Python CLI tool powered by the Google Gemini API (gemini-2.5-flash) that analyzes, explains, and reviews code snippets.

## Features
- Direct file analysis via command-line arguments.
- Interactive mode for pasting code directly in the terminal.
- Step-by-step code explanations, bug identification, and performance optimizations.

## Setup & Usage

1. **Install dependencies:**
   ```bash
   pip install google-genai
   ```
   ```bash
   2. Set your Gemini API Key:
   Windows (CMD): set GEMINI_API_KEY=your_api_key
   Linux/Mac: export GEMINI_API_KEY=your_api_key
   ```
   ```bash
   3. Run the tool:
   Analyze a file:
   python main.py test.py
   Interactive mode:
   python main.py
   ```

   **Author:** Aryan Rathi
   **CU ID:** CU26220292
   **Branch:** AI/ML
