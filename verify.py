#!/usr/bin/env python3
"""
Verification script for Data Visualization Dashboard
Tests all key functionality programmatically
"""

import sys
import os
import pandas as pd

def test_data_processing():
    """Test data processing functionality"""
    print("1. Testing Data Processing...")

    try:
        # Test CSV reading
        df = pd.read_csv('test_data.csv')
        print(f"   [OK] CSV file loaded: {df.shape[0]} rows, {df.shape[1]} columns")

        # Test data validation
        assert df.shape == (10, 5), f"Expected shape (10,5), got {df.shape}"
        assert 'Region' in df.columns, "Region column missing"
        assert 'Sales' in df.columns, "Sales column missing"

        print("   [OK] Data structure validated")
        print("   [OK] Column detection: ", list(df.columns))

        # Test numeric vs categorical detection
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

        print(f"   [OK] Numeric columns: {numeric_cols}")
        print(f"   [OK] Categorical columns: {categorical_cols}")

        return True

    except Exception as e:
        print(f"   [FAIL] Data processing failed: {e}")
        return False

def test_app_imports():
    """Test Flask application imports and basic structure"""
    print("\n2. Testing Flask Application...")

    try:
        import app
        print("   [OK] Flask application imports successfully")

        # Check key functions exist
        assert hasattr(app, 'app'), "Flask app object missing"
        assert hasattr(app, 'load_data'), "load_data function missing"
        assert hasattr(app, 'allowed_file'), "allowed_file function missing"

        print("   [OK] Key functions verified")
        print(f"   [OK] Upload folder: {app.app.config['UPLOAD_FOLDER']}")

        return True

    except Exception as e:
        print(f"   [FAIL] Flask application test failed: {e}")
        return False

def test_frontend_files():
    """Test that all frontend files exist"""
    print("\n3. Testing Frontend Files...")

    required_files = [
        'templates/index.html',
        'templates/dashboard.html',
        'static/css/style.css',
        'static/js/dashboard.js',
        'README.md'
    ]

    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
        else:
            print(f"   [OK] {file_path} exists")

    if missing_files:
        print(f"   [FAIL] Missing files: {missing_files}")
        return False
    else:
        print("   [OK] All frontend files present")
        return True

def test_dependencies():
    """Test that key dependencies are available"""
    print("\n4. Testing Dependencies...")

    required_packages = ['flask', 'pandas', 'plotly', 'openpyxl']
    failed_imports = []

    for package in required_packages:
        try:
            __import__(package)
            print(f"   [OK] {package} available")
        except ImportError:
            failed_imports.append(package)
            print(f"   [FAIL] {package} not available")

    return len(failed_imports) == 0

def main():
    """Run all verification tests"""
    print("=== Data Visualization Dashboard Verification ===\n")

    tests = [
        test_dependencies,
        test_frontend_files,
        test_app_imports,
        test_data_processing,
    ]

    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"Test failed with exception: {e}")
            results.append(False)

    print(f"\n=== Results: {sum(results)}/{len(results)} tests passed ===")

    if all(results):
        print("[SUCCESS] All tests passed! The application should work correctly.")
        print("\nTo run the application:")
        print("1. python app.py")
        print("2. Open http://127.0.0.1:5000 in your browser")
        print("3. Upload test_data.csv to see the dashboard in action")
    else:
        print("[ERROR] Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()