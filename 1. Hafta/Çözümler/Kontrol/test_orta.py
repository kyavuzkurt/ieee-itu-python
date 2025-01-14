import io
import sys
import unittest
from unittest.mock import patch

class TestCalculator(unittest.TestCase):
    def test_normal_operations(self):
        # Test with regular numbers
        test_inputs = ['10', '5']
        expected_output = """Toplam: 15.0
Çarpım: 50.0
Fark: 5.0
Bölüm: 2.0
"""
        
        with patch('sys.stdin', io.StringIO('\n'.join(test_inputs))), \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            
            with open('orta.py') as f:
                exec(f.read())
            
            actual_output = mock_stdout.getvalue()
            actual_output = actual_output.split("2. Sayıyı giriniz: ")[-1]
            
            self.assertEqual(actual_output, expected_output)
    
    def test_negative_numbers(self):
        # Test with negative numbers
        test_inputs = ['-10', '-5']
        expected_output = """Toplam: -15.0
Çarpım: 50.0
Fark: -5.0
Bölüm: 2.0
"""
        
        with patch('sys.stdin', io.StringIO('\n'.join(test_inputs))), \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            
            with open('orta.py') as f:
                exec(f.read())
            
            actual_output = mock_stdout.getvalue()
            actual_output = actual_output.split("2. Sayıyı giriniz: ")[-1]
            
            self.assertEqual(actual_output, expected_output)
    
    def test_division_by_zero(self):
        # Test division by zero handling
        test_inputs = ['10', '0']
        expected_output = """Toplam: 10.0
Çarpım: 0.0
Fark: 10.0
Bölüm işlemi yapılamaz
"""
        
        with patch('sys.stdin', io.StringIO('\n'.join(test_inputs))), \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            
            with open('orta.py') as f:
                exec(f.read())
            
            actual_output = mock_stdout.getvalue()
            actual_output = actual_output.split("2. Sayıyı giriniz: ")[-1]
            
            self.assertEqual(actual_output, expected_output)

    def test_decimal_numbers(self):
        # Test with decimal numbers
        test_inputs = ['2.5', '1.5']
        expected_output = """Toplam: 4.0
Çarpım: 3.75
Fark: 1.0
Bölüm: 1.6666666666666667
"""
        
        with patch('sys.stdin', io.StringIO('\n'.join(test_inputs))), \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            
            with open('orta.py') as f:
                exec(f.read())
            
            actual_output = mock_stdout.getvalue()
            actual_output = actual_output.split("2. Sayıyı giriniz: ")[-1]
            
            self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()