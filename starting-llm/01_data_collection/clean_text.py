"""
Data cleaning and text normalization for Shakespeare corpus.
Processes the raw Shakespeare text and prepares it for tokenization.
"""

import os
import re

def load_raw_text(file_path):
    """Load the raw text from file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def clean_text(text):
    """
    Clean and normalize the text:
    - Remove excessive whitespace
    - Normalize newlines
    - Keep basic punctuation and structure
    - Handle character names and stage directions appropriately
    """
    # Normalize line breaks and excessive whitespace
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\r', '', text)
    
    # Remove excessive spaces while preserving single spaces
    text = re.sub(r'[ \t]+', ' ', text)
    
    # Clean up spacing around punctuation
    text = re.sub(r'\s+([,.!?;:])', r'\1', text)
    text = re.sub(r'([,.!?;:])\s+', r'\1 ', text)
    
    # Remove leading/trailing whitespace from lines
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    text = '\n'.join(lines)
    
    return text

def save_cleaned_text(text, output_path):
    """Save the cleaned text to file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

def main():
    # Paths
    raw_file = os.path.join(os.path.dirname(__file__), 'raw', 'input.txt')
    processed_dir = os.path.dirname(os.path.dirname(__file__))
    processed_dir = os.path.join(processed_dir, '03_dataset', 'processed')
    
    # Create processed directory if it doesn't exist
    os.makedirs(processed_dir, exist_ok=True)
    
    output_file = os.path.join(processed_dir, 'shakespeare_clean.txt')
    
    # Process the text
    print(f"Loading raw text from: {raw_file}")
    raw_text = load_raw_text(raw_file)
    print(f"Raw text length: {len(raw_text)} characters")
    
    print("Cleaning text...")
    clean = clean_text(raw_text)
    print(f"Clean text length: {len(clean)} characters")
    
    print(f"Saving cleaned text to: {output_file}")
    save_cleaned_text(clean, output_file)
    
    # Display sample of cleaned text
    print("\n--- Sample of cleaned text (first 500 chars) ---")
    print(clean[:500])
    print("\n--- Processing complete! ---")

if __name__ == "__main__":
    main()