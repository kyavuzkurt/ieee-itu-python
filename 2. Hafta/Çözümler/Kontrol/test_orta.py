import unittest
from unittest.mock import patch
from io import StringIO
import sys

class TestGradeManagementSystem(unittest.TestCase):
    def setUp(self):
        # Initial state of the class
        self.initial_data = {
            "Ali": [85.0, 90.0, 78.0],
            "Zehra": [92.0, 88.0, 95.0],
            "Efe": [75.0, 80.0, 68.0]
        }

    def simulate_input(self, inputs):
        # Helper method to simulate multiple inputs and capture output
        inputs = iter(inputs)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', lambda _: next(inputs)):
                with open('orta.py') as f:
                    # Create a local namespace to avoid global variable conflicts
                    local_ns = {}
                    exec(f.read(), local_ns)
            return fake_output.getvalue().strip()

    def test_add_student(self):
        # Test adding a new student
        output = self.simulate_input(['1', 'Ayse', '9'])
        self.assertIn('Ayse sınıfa eklendi', output)

        # Test adding an existing student
        output = self.simulate_input(['1', 'Ali', '9'])
        self.assertIn('Ali zaten mevcut', output)

    def test_remove_student(self):
        # Test removing an existing student
        output = self.simulate_input(['2', 'Ali', '9'])
        self.assertIn('Ali sınıftan silindi', output)

        # Test removing a non-existent student
        output = self.simulate_input(['2', 'Mehmet', '9'])
        self.assertIn('Mehmet bulunamadı', output)

    def test_add_grade(self):
        # Test adding a valid grade
        output = self.simulate_input(['3', 'Ali', '95', '9'])
        self.assertIn('Ali isimli öğrenciye 95.0 notu eklendi', output)

        # Test adding grade for non-existent student
        output = self.simulate_input(['3', 'Mehmet', '95', '9'])
        self.assertIn('Mehmet bulunamadı', output)

        # Test adding invalid grade
        output = self.simulate_input(['3', 'Ali', 'abc', '9'])
        self.assertIn('Geçerli bir not değeri girin', output)

    def test_view_grades(self):
        # Test viewing existing student's grades
        output = self.simulate_input(['4', 'Ali', '9'])
        self.assertIn('Ali isimli öğrencinin notları:', output)
        self.assertIn('85.0', output)
        self.assertIn('90.0', output)
        self.assertIn('78.0', output)

        # Test viewing non-existent student's grades
        output = self.simulate_input(['4', 'Mehmet', '9'])
        self.assertIn('Mehmet bulunamadı', output)

    def test_calculate_average(self):
        # Test calculating average for existing student
        output = self.simulate_input(['5', 'Ali', '9'])
        self.assertIn('Ali isimli öğrencinin ortalaması: 84.33', output)

        # Test calculating average for non-existent student
        output = self.simulate_input(['5', 'Mehmet', '9'])
        self.assertIn('Mehmet için not bulunamadı veya liste boş', output)

    def test_check_pass_status(self):
        # Test pass status for passing student
        output = self.simulate_input(['6', 'Zehra', '9'])
        self.assertIn('Zehra isimli öğrenci, 91.67 ortalama ile geçti', output)

        # Test pass status for failing student
        output = self.simulate_input(['6', 'Efe', '9'])
        self.assertIn('Efe isimli öğrenci, 74.33 ortalama ile geçti', output)

    def test_class_average(self):
        # Test calculating class average
        output = self.simulate_input(['7', '9'])
        self.assertIn('Sınıfın genel ortalaması:', output)

    def test_highest_lowest_grades(self):
        # Test finding highest and lowest grades
        output = self.simulate_input(['8', '9'])
        self.assertIn('Sınıftaki en yüksek not: 95.0', output)
        self.assertIn('Sınıftaki en düşük not: 68.0', output)

    def test_invalid_choice(self):
        # Test invalid menu choice
        output = self.simulate_input(['10', '9'])
        self.assertIn('Geçersiz seçim', output)

    def test_exit(self):
        # Test exit functionality
        output = self.simulate_input(['9'])
        self.assertIn('Çıkış yapılıyor', output)

if __name__ == '__main__':
    unittest.main() 