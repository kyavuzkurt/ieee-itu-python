import io
import sys
import unittest
from unittest.mock import patch

class TestStudentInfo(unittest.TestCase):
    def test_normal_input(self):
        # Test input values
        test_inputs = ['Ahmet Yılmaz', '12345', 'Matematik', '85']
        expected_output = "Okulumuz 12345 no'lu öğrencisi Ahmet Yılmaz, bu dönem sonunda Matematik dersinden 85 ortalama başarmıştır.\n"
        
        # Simulate user input and capture output
        with patch('sys.stdin', io.StringIO('\n'.join(test_inputs))), \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            
            # Import and run the student's script
            with open('kolay.py') as f:
                exec(f.read())
            
            # Get the actual output and extract only the final result
            actual_output = mock_stdout.getvalue()
            actual_output = actual_output.split("Ortalamanızı giriniz: ")[-1]
            
            # Compare expected and actual output
            self.assertEqual(actual_output, expected_output)
    
    def test_special_characters(self):
        # Test with special characters and spaces
        test_inputs = ['İşıl Öztürk', '98765', 'Türkçe', '90.5']
        expected_output = "Okulumuz 98765 no'lu öğrencisi İşıl Öztürk, bu dönem sonunda Türkçe dersinden 90.5 ortalama başarmıştır.\n"
        
        with patch('sys.stdin', io.StringIO('\n'.join(test_inputs))), \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            
            with open('kolay.py') as f:
                exec(f.read())
            actual_output = mock_stdout.getvalue()
            actual_output = actual_output.split("Ortalamanızı giriniz: ")[-1]
            self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()