import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

class TestLoopProgram(unittest.TestCase):
    def setUp(self):
        self.expected_output = [1, 2, 3, 4, 5]
    
    def get_output(self, input_value):
        # Redirect stdout to capture print outputs
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value=input_value):
                # Import and run the script
                with open('kolay.py') as f:
                    exec(f.read())
            return fake_output.getvalue().strip()

    def test_for_loop(self):
        expected_numbers = "\n".join(map(str, self.expected_output))
        
        # Test with "For" input
        output = self.get_output("For").lower()  # Make comparison case-insensitive
        self.assertIn(expected_numbers, output)

        # Test with lowercase "for" input
        output = self.get_output("for").lower()
        self.assertIn(expected_numbers, output)

    def test_while_loop(self):
        expected_numbers = "\n".join(map(str, self.expected_output))
        
        # Test with "While" input
        output = self.get_output("While").lower()  # Make comparison case-insensitive
        self.assertIn(expected_numbers, output)

        # Test with lowercase "while" input
        output = self.get_output("while").lower()
        self.assertIn(expected_numbers, output)

    def test_invalid_input(self):
        # Test with invalid input
        output = self.get_output("invalid")
        self.assertEqual(output, "Geçersiz döngü seçildi, lütfen For veya While seçiniz")

if __name__ == '__main__':
    unittest.main() 