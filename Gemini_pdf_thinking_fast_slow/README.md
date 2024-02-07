# Chat with your documents

This folder contains an example of how to make an application to chat with your documents, using Chroma and Google Gemini's API.
It uses the 'Thinking, fast and slow' book by Daniel Kahneman. 

## How it works

The basic flow is as follows:

0. The pdf document in the `documents` folder is loaded page by page, then embedded and stored in a Chroma collection.
1. When the user submits a question, it gets embedded using the same model as the document, and the lines most relevant to the query are retrieved by Chroma.
2. The user-submitted question is passed to Google Gemini's API, along with the extra context retrieved by Chroma. The Google Gemini API generates a response.
3. The response is displayed to the user, along with the lines used as extra context.

## Running the code

You will need a Google API key to run this demo.

Install dependencies and run the example:

```bash
# Install dependencies
pip install -r requirements.txt

# Load the example documents into Chroma
python load_data.py

# Run the chatbot
python main.py
```

Example output:

```
Query: Tell me something about system 1 and system 2

Thinking...

System 1 and System 2 are two distinct modes of thinking that exist within our minds. 

System 1 is fast, automatic, effortless, intuitive, and operates outside of our conscious awareness. It's responsible for making quick judgments and associations based on limited information, relying on heuristics and biases. System 1 is often emotional and impulsive.

System 2, on the other hand, is slow, deliberate, controlled, rational, and requires conscious effort and attention. It's capable of complex logical reasoning, analyzing information systematically, and making well-thought-out decisions. System 2 is more analytical and reflective.

System 1 is constantly active, processing information and making judgments, while System 2 only engages when needed or when System 1 is uncertain or conflicted. System 2 can override the impulses and intuitions of System 1 through conscious effort and deliberate reasoning.

The interaction between System 1 and System 2 is dynamic and influences our thoughts, feelings, and actions. While System 1 often provides quick and efficient solutions, it can also lead to errors and biases due to its reliance on heuristics and limited information. System 2 can help correct these errors by applying more rigorous and analytical thinking.

Understanding the differences between System 1 and System 2 can help us make better decisions by being more aware of our cognitive biases, slowing down to engage System 2 when appropriate, and seeking out diverse perspectives to challenge our initial intuitions.
--------------------------------------------------------------------------------
Sources:
Thinking, Fast and Slow by Daniel Kahneman.pdf: page_number 80, ID: 73, Distance: 0.54
Thinking, Fast and Slow by Daniel Kahneman.pdf: page_number 522, ID: 505, Distance: 0.53
Thinking, Fast and Slow by Daniel Kahneman.pdf: page_number 60, ID: 53, Distance: 0.52
Thinking, Fast and Slow by Daniel Kahneman.pdf: page_number 23, ID: 16, Distance: 0.52
Thinking, Fast and Slow by Daniel Kahneman.pdf: page_number 92, ID: 85, Distance: 0.49
Thinking, Fast and Slow by Daniel Kahneman.pdf: page_number 24, ID: 17, Distance: 0.49
Thinking, Fast and Slow by Daniel Kahneman.pdf: page_number 27, ID: 20, Distance: 0.42
Thinking, Fast and Slow by Daniel Kahneman.pdf: page_number 51, ID: 44, Distance: 0.42
Thinking, Fast and Slow by Daniel Kahneman.pdf: page_number 32, ID: 25, Distance: 0.38
Thinking, Fast and Slow by Daniel Kahneman.pdf: page_number 40, ID: 33, Distance: 0.35
--------------------------------------------------------------------------------

```

You can replace the example pdf documents in the `documents` folder with your own documents, and the chatbot will use those instead.
