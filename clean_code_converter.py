import os
import sys

class CleanCodeConverter:
    def __init__(self, file_path):
        self.file_path = file_path

    def analyze(self):
        with open(self.file_path, 'r') as file:
            code = file.read()
            suggestions = self.get_suggestions(code)
            return suggestions

    def get_suggestions(self, code):
        # Analyze the code for clean code suggestions
        # This is a placeholder for actual analysis logic
        suggestions = []
        if 'print' in code:
            suggestions.append('Avoid using print statements for debugging.')
        if ' var ' in code:
            suggestions.append('Use let or const instead of var in JavaScript.')
        if code.strip().endswith(';'):
            suggestions.append('Remove unnecessary semicolons in JavaScript code.')
        return suggestions

    def display_suggestions(self, suggestions):
        print('Refactoring Suggestions:')
        for suggestion in suggestions:
            print(f'- {suggestion}')  # Updated for formatted string

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python clean_code_converter.py path/to/your/code_file.py')
        sys.exit(1)
    file_path = sys.argv[1]
    converter = CleanCodeConverter(file_path)
    suggestions = converter.analyze()
    converter.display_suggestions(suggestions)