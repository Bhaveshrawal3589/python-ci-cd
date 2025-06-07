import sys
import os

# Add project root to Python path so 'app' module can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add

def test_add():
    assert add(2, 3) == 5

