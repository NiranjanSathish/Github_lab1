# Github Lab 1 MLOps (IE-7374)

A Python-based password validation system with comprehensive testing and automated CI/CD implementation using GitHub Actions. This Lab demonstrates best practices in software development, including unit testing, continuous integration, and secure password validation.

## Overview

This project implements a robust password strength analyzer that evaluates passwords based on multiple security criteria. It includes automated testing with both Pytest and Unittest frameworks, integrated with GitHub Actions for continuous integration and deployment.

### Key Capabilities:
- Multi-criteria password validation
- Real-time strength scoring (0-100 scale)
- Detection of common security vulnerabilities
- Comprehensive test coverage with automated CI/CD
- Professional development workflow with version control

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git installed on your system
- GitHub account

### Installation Steps

**1. Set Up Your Development Environment**

Create and activate a virtual environment to isolate project dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

**2. Clone the Repository**

```bash
git clone https://github.com/your-username/password-validator-cicd.git
cd password-validator-cicd
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 📂 Project Architecture

```
password-validator-cicd/
│
├── src/
│   ├── __init__.py
│   └── password_validator.py          # Core validation logic
│
├── test/
│   ├── __init__.py
│   ├── test_pytest.py                 # Pytest test suite
│   └── test_unittest.py               # Unittest test suite
│
├── .github/
│   └── workflows/
│       ├── github_actions_pytest.yml          # Pytest CI workflow
│       └── github_actions_unittest.yml        # Unittest CI workflow
│
├── requirements.txt                    # Python dependencies
├── .gitignore                         # Git exclusions
└── README.md                          # Documentation
```

---

## 🔐 Password Validator Features

### Validation Functions

The `password_validator.py` module provides eight specialized functions:

| Function | Purpose | Returns |
|----------|---------|---------|
| `check_length()` | Verifies minimum password length (default: 8 chars) | Boolean |
| `has_uppercase()` | Detects uppercase letters | Boolean |
| `has_lowercase()` | Detects lowercase letters | Boolean |
| `has_digits()` | Checks for numeric characters | Boolean |
| `has_special_chars()` | Identifies special symbols | Boolean |
| `check_common_patterns()` | Flags weak patterns (123, abc, password, etc.) | Boolean |
| `calculate_strength_score()` | Computes overall security score | Integer (0-100) |
| `validate_password()` | Generates comprehensive validation report | Dictionary |

### Strength Scoring Algorithm

The scoring system evaluates passwords across multiple dimensions:

- **Length Score** (30 points max):
  - 10 points: 8+ characters
  - 10 points: 12+ characters  
  - 10 points: 16+ characters

- **Character Diversity** (60 points max):
  - 15 points: Contains uppercase letters
  - 15 points: Contains lowercase letters
  - 15 points: Contains digits
  - 15 points: Contains special characters

- **Pattern Security** (10 points):
  - 10 points: No common weak patterns detected

**Total Maximum Score: 100 points**

Passwords scoring 70+ are classified as "strong."

---

## 🧪 Testing Framework

### Running Tests

**Execute Pytest Suite:**
```bash
# Run all tests
pytest test/test_pytest.py

# Run with verbose output
pytest test/test_pytest.py -v

# Run with coverage report
pytest test/test_pytest.py --cov=src --cov-report=term-missing
```

**Execute Unittest Suite:**
```bash
# Run unittest tests
python -m unittest test.test_unittest

# Run with verbose output
python -m unittest test.test_unittest -v
```

### Test Coverage

**Pytest Test Suite (17 test cases):**
- 8 standard test functions covering all validation methods
- 2 parametrized tests for efficient multi-scenario testing
- Edge case validation (empty strings, boundary conditions, special characters)

**Unittest Test Suite (8 test methods):**
- Complete TestCase class implementation
- Mirror coverage of all validation functions
- Traditional unittest assertion methods

---

## ⚙️ CI/CD Implementation

### GitHub Actions Workflows

This project uses two automated workflows that trigger on every push to the main branch:

**Pytest Workflow (`pytest_action.yml`):**
1. Environment setup with Ubuntu latest
2. Python 3.8 configuration
3. Dependency installation
4. Test execution with JUnit XML report generation
5. Test artifact upload for review
6. Status notifications (pass/fail)

**Unittest Workflow (`unittest_action.yml`):**
1. Identical environment setup
2. Unittest execution via Python module
3. Automated result reporting
4. Build status tracking

### Viewing CI/CD Results

After pushing code to GitHub:
1. Navigate to your repository
2. Click the **Actions** tab
3. View workflow runs and their status
4. Download test artifacts for detailed analysis
5. Review logs for any failures

---
## 🛠️ Development Workflow

### Making Changes

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes and test locally:**
   ```bash
   pytest test/test_pytest.py
   python -m unittest test.test_unittest
   ```

3. **Stage and commit:**
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   ```

4. **Push to GitHub:**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** - CI/CD will automatically run tests

### Git Best Practices

- Keep commits atomic and descriptive
- Test locally before pushing
- Review CI/CD results before merging
- Update documentation with code changes

---
## 🎓 Learning Outcomes

This Lab demonstrates proficiency in:

- **Software Engineering**: Modular code design, function decomposition
- **Testing**: Unit testing, test-driven development, edge case handling
- **DevOps**: CI/CD pipelines, automated testing, GitHub Actions
- **Version Control**: Git workflows, branching strategies
- **Security**: Password validation, security best practices
- **Documentation**: Professional README, code comments, clear examples

---

## 🔍 Troubleshooting

**Tests failing locally?**
- Ensure virtual environment is activated
- Verify all dependencies are installed: `pip list`
- Check Python version: `python --version`

**GitHub Actions not triggering?**
- Verify `.github/workflows/` folder structure
- Confirm YAML files are properly formatted
- Check that you pushed to the `main` branch

**Import errors?**
- Ensure `__init__.py` files exist in `src/` and `test/` folders
- Run tests from project root directory

---

## 📝 License

This Lab is developed as part of MLOps coursework (IE-7374) and is available for educational purposes.

---

## 🌟 Acknowledgments

- MLOps course curriculum for project structure guidance
- GitHub Actions documentation for CI/CD implementation
- Pytest and Unittest communities for testing frameworks

---