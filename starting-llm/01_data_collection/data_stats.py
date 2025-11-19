"""
Data statistics for the Shakespeare corpus.
Provides insights into the dataset characteristics.
"""

import os
import string
from collections import Counter

def analyze_text(file_path):
    """Analyze the text and return various statistics."""
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Basic statistics
    stats = {
        'total_chars': len(text),
        'total_lines': len(text.split('\n')),
        'total_words': len(text.split()),
        'unique_chars': len(set(text)),
        'char_counts': Counter(text),
        'avg_line_length': len(text) / len(text.split('\n')),
        'avg_word_length': sum(len(word) for word in text.split()) / len(text.split())
    }
    
    # Character distribution
    letters = sum(c.isalpha() for c in text)
    digits = sum(c.isdigit() for c in text)
    spaces = sum(c.isspace() for c in text)
    punctuation = sum(c in string.punctuation for c in text)
    
    stats.update({
        'letters': letters,
        'digits': digits,
        'spaces': spaces,
        'punctuation': punctuation
    })
    
    return stats, text

def print_stats(stats, sample_text):
    """Print formatted statistics."""
    print("=" * 50)
    print("SHAKESPEARE CORPUS STATISTICS")
    print("=" * 50)
    
    print(f"Total characters: {stats['total_chars']:,}")
    print(f"Total lines: {stats['total_lines']:,}")
    print(f"Total words: {stats['total_words']:,}")
    print(f"Unique characters: {stats['unique_chars']}")
    print(f"Average line length: {stats['avg_line_length']:.1f} characters")
    print(f"Average word length: {stats['avg_word_length']:.1f} characters")
    
    print("\nCharacter Distribution:")
    print(f"  Letters: {stats['letters']:,} ({stats['letters']/stats['total_chars']*100:.1f}%)")
    print(f"  Digits: {stats['digits']:,} ({stats['digits']/stats['total_chars']*100:.1f}%)")
    print(f"  Spaces: {stats['spaces']:,} ({stats['spaces']/stats['total_chars']*100:.1f}%)")
    print(f"  Punctuation: {stats['punctuation']:,} ({stats['punctuation']/stats['total_chars']*100:.1f}%)")
    
    print(f"\nMost common characters:")
    for char, count in stats['char_counts'].most_common(10):
        if char == '\n':
            print(f"  '\\n' (newline): {count:,}")
        elif char == ' ':
            print(f"  ' ' (space): {count:,}")
        elif char == '\t':
            print(f"  '\\t' (tab): {count:,}")
        else:
            print(f"  '{char}': {count:,}")
    
    print(f"\nVocabulary (unique character set):")
    unique_chars = sorted(stats['char_counts'].keys())
    print(''.join(unique_chars))
    
    print(f"\nSample text (first 200 characters):")
    print(repr(sample_text[:200]))

def main():
    # Check both raw and processed files
    raw_file = os.path.join(os.path.dirname(__file__), 'raw', 'input.txt')
    processed_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                  '03_dataset', 'processed', 'shakespeare_clean.txt')
    
    if os.path.exists(raw_file):
        print("ANALYZING RAW DATA:")
        stats, text = analyze_text(raw_file)
        print_stats(stats, text)
        print("\n\n")
    
    if os.path.exists(processed_file):
        print("ANALYZING PROCESSED DATA:")
        stats, text = analyze_text(processed_file)
        print_stats(stats, text)

if __name__ == "__main__":
    main()