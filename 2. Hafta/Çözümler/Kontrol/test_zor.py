import subprocess
import json
import shutil
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(BASE_DIR, 'test_data')
ZOR_PY_PATH = os.path.join(BASE_DIR, 'zor.py')

# Backup original JSON files if necessary
def setup_test_environment():
    # Ensure test_data directory exists
    if not os.path.exists(TEST_DATA_DIR):
        os.makedirs(TEST_DATA_DIR)
    
    # Define paths
    original_files = ['kitaplar.json', 'uyeler.json', 'oduncler.json']
    for file in original_files:
        shutil.copy(os.path.join(BASE_DIR, file), os.path.join(TEST_DATA_DIR, file))

def reset_test_environment():
    # Reset JSON files to original state before each test
    original_files = ['kitaplar.json', 'uyeler.json', 'oduncler.json']
    for file in original_files:
        shutil.copy(os.path.join(TEST_DATA_DIR, file), os.path.join(BASE_DIR, file))

def test_add_kitap():
    try:
        reset_test_environment()
        
        # Define the inputs for adding a new kitap
        inputs = [
            '1',    # Main menu: Kitap Yönetimi
            '1',    # Kitap Yönetimi menu: Kitap Ekle
            'New Test Kitap',  # Kitap İsmi
            'New Test Yazar',  # Yazar
            'New Test Tür',    # Tür
            '10',              # Stok Sayısı
            '5',               # Kitap Yönetimi menu: Geri Dön
            '5'                # Main menu: Çıkış
        ]
        
        # Prepare the input string
        input_str = '\n'.join(inputs) + '\n'
        
        # Run zor.py with test JSON files
        process = subprocess.Popen(
            ['python3', ZOR_PY_PATH, 
             os.path.join(BASE_DIR, 'kitaplar.json'),
             os.path.join(BASE_DIR, 'uyeler.json'),
             os.path.join(BASE_DIR, 'oduncler.json')],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(input=input_str)
        
        # Check for errors in stderr
        if stderr:
            print("Error during test_add_kitap execution:", stderr)
            return
        
        # Load the updated kitaplar.json to verify
        with open(os.path.join(BASE_DIR, 'kitaplar.json'), 'r', encoding='utf-8') as f:
            kitaplar = json.load(f)
        
        # Assert the new kitap is added
        new_kitap = next((k for k in kitaplar if k['isim'] == 'New Test Kitap'), None)
        assert new_kitap is not None, "New Test Kitap was not added."
        assert new_kitap['yazar'] == 'New Test Yazar', "Yazar does not match."
        assert new_kitap['turu'] == 'New Test Tür', "Tür does not match."
        assert new_kitap['stok'] == 10, "Stok sayısı does not match."
        
        print("test_add_kitap passed.")
    except AssertionError as ae:
        print(f"Assertion failed in test_add_kitap: {ae}")
    except Exception as e:
        print(f"An unexpected error occurred in test_add_kitap: {e}")

def test_remove_kitap():
    try:
        reset_test_environment()
        
        # First, add a kitap to remove
        with open(os.path.join(BASE_DIR, 'kitaplar.json'), 'r+', encoding='utf-8') as f:
            kitaplar = json.load(f)
            kitap_id = 1 if not kitaplar else kitaplar[-1]['id'] + 1
            yeni_kitap = {
                "id": kitap_id,
                "isim": "Remove Kitap",
                "yazar": "Remove Yazar",
                "turu": "Remove Tür",
                "stok": 5
            }
            kitaplar.append(yeni_kitap)
            f.seek(0)
            json.dump(kitaplar, f, ensure_ascii=False, indent=4)
            f.truncate()
        
        # Define the inputs for removing the kitap
        inputs = [
            '1',    # Main menu: Kitap Yönetimi
            '2',    # Kitap Yönetimi menu: Kitap Sil
            str(kitap_id),  # Silinecek kitabın ID'si
            '5',    # Kitap Yönetimi menu: Geri Dön
            '5'     # Main menu: Çıkış
        ]
        
        # Prepare the input string
        input_str = '\n'.join(inputs) + '\n'
        
        # Run zor.py with test JSON files
        process = subprocess.Popen(
            ['python3', ZOR_PY_PATH, 
             os.path.join(BASE_DIR, 'kitaplar.json'),
             os.path.join(BASE_DIR, 'uyeler.json'),
             os.path.join(BASE_DIR, 'oduncler.json')],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(input=input_str)
        
        # Check for errors in stderr
        if stderr:
            print("Error during test_remove_kitap execution:", stderr)
            return
        
        # Load the updated kitaplar.json to verify removal
        with open(os.path.join(BASE_DIR, 'kitaplar.json'), 'r', encoding='utf-8') as f:
            kitaplar = json.load(f)
        
        # Assert the kitap is removed
        removed_kitap = next((k for k in kitaplar if k['id'] == kitap_id), None)
        assert removed_kitap is None, "Kitap was not removed."
        
        print("test_remove_kitap passed.")
    except AssertionError as ae:
        print(f"Assertion failed in test_remove_kitap: {ae}")
    except Exception as e:
        print(f"An unexpected error occurred in test_remove_kitap: {e}")

def test_add_kitap_invalid_stok():
    try:
        reset_test_environment()
        
        # Define the inputs with invalid stok
        inputs = [
            '1',    # Main menu: Kitap Yönetimi
            '1',    # Kitap Yönetimi menu: Kitap Ekle
            'Invalid Kitap',  # Kitap İsmi
            'Invalid Yazar',  # Yazar
            'Invalid Tür',    # Tür
            'abc',            # Invalid Stok Sayısı
            '5',              # Kitap Yönetimi menu: Geri Dön
            '5'               # Main menu: Çıkış
        ]
        
        input_str = '\n'.join(inputs) + '\n'
        
        process = subprocess.Popen(
            ['python3', ZOR_PY_PATH, 
             os.path.join(BASE_DIR, 'kitaplar.json'),
             os.path.join(BASE_DIR, 'uyeler.json'),
             os.path.join(BASE_DIR, 'oduncler.json')],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(input=input_str)
        
        # Check for errors in stderr
        if stderr:
            print("Error during test_add_kitap_invalid_stok execution:", stderr)
        
        # The test should ensure that the kitap was not added
        with open(os.path.join(BASE_DIR, 'kitaplar.json'), 'r', encoding='utf-8') as f:
            kitaplar = json.load(f)
        
        invalid_kitap = next((k for k in kitaplar if k['isim'] == 'Invalid Kitap'), None)
        assert invalid_kitap is None, "Invalid Kitap was incorrectly added."
        
        print("test_add_kitap_invalid_stok passed.")
    except AssertionError as ae:
        print(f"Assertion failed in test_add_kitap_invalid_stok: {ae}")
    except Exception as e:
        print(f"An unexpected error occurred in test_add_kitap_invalid_stok: {e}")

if __name__ == "__main__":
    setup_test_environment()
    test_add_kitap()
    test_remove_kitap()
    test_add_kitap_invalid_stok()
