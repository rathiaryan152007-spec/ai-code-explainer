import sys
import os
from google import genai
from google.genai import errors

def explain_code(code_snippet):
    client = genai.Client()
    
    prompt = f"""
    You are an expert software engineer and code reviewer. 
    Please review the following code snippet, explain how it works step-by-step, 
    and suggest any performance improvements or bug fixes if necessary:

    {code_snippet}
    """
    
    try:
        print("\nAnalyzing code with Gemini 3.8 Flash...")
        # Updated to the Gemini 3.8 Flash model endpoint
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        print("\n=== Code Explanation & Review ===\n")
        print(response.text)
        
    except errors.APIError as e:
        print(f"API Error occurred: {e}")

if __name__ == "__main__":
    # Check if a filename was provided as a command-line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if os.path.exists(filename):
            print(f"Reading code from '{filename}'...")
            with open(filename, 'r') as file:
                user_code = file.read()
            explain_code(user_code)
        else:
            print(f"Error: File '{filename}' not found.")
    else:
        # Fallback to interactive mode if no file is specified
        print("========================================")
        print("    AI CODE EXPLAINER & REVIEWER        ")
        print("========================================")
        print("Paste your code below (type 'END' on a new line when done):\n")
        
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
            
        user_code = "\n".join(lines)
        if user_code.strip():
            explain_code(user_code)
        else:
            print("No code was provided!")