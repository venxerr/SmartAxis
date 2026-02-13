"""
Simple test script to verify the pygame project setup works correctly.
"""

import subprocess
import sys
import os

def test_project():
    """Test if the project runs without errors."""
    print("Testing PyGame Controller Project Setup...")
    print("=" * 50)
    
    # Check if virtual environment exists
    if not os.path.exists("venv"):
        print("❌ Virtual environment not found")
        return False
    print("✅ Virtual environment exists")
    
    # Check if all required files exist
    required_files = [
        "main.py",
        "controller_input.py", 
        "ui_display.py",
        "config.py",
        "requirements.txt",
        "README.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    print("✅ All required files exist")
    
    # Check if pygame is installed in virtual environment
    try:
        result = subprocess.run(
            ["venv\\Scripts\\python", "-c", "import pygame; print(f'Pygame version: {pygame.version.ver}')"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if "version" in result.stdout:
            print(f"✅ PyGame installed: {result.stdout.strip()}")
        else:
            print(f"❌ PyGame not properly installed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error checking PyGame: {e}")
        return False
    
    # Try to run the application briefly to check for import errors
    print("\nTesting application imports...")
    try:
        result = subprocess.run(
            ["venv\\Scripts\\python", "-c", """
import sys
sys.path.insert(0, '.')
from main import ControllerApp
print('✅ All imports successful')
            """],
            capture_output=True,
            text=True,
            timeout=5
        )
        if "successful" in result.stdout:
            print("✅ Application imports work correctly")
        else:
            print(f"❌ Import error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error testing imports: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("✅ Project setup completed successfully!")
    print("\nTo run the application:")
    print("1. Activate virtual environment: venv\\Scripts\\activate")
    print("2. Run: python main.py")
    print("3. Connect a controller and see the input visualization")
    print("4. Press ESC to exit")
    
    return True

if __name__ == "__main__":
    success = test_project()
    sys.exit(0 if success else 1)