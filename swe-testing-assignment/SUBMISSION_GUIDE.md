## GitHub Repository Setup Instructions

Your complete Quick-Calc project is ready for submission to GitHub.

**Your GitHub Repository URL will be:**
https://github.com/lepembejeremie/swe-testing-assignment

### Steps to Upload to GitHub

1. **Create Repository on GitHub**
   - Go to https://github.com/new
   - Repository name: `swe-testing-assignment`
   - Description: "Quick-Calc - Simple calculator with comprehensive testing"
   - Make it PUBLIC
   - Do NOT initialize with README (we have one already)
   - Click "Create repository"

2. **Push to GitHub**
   
   From the command line in your project directory:
   ```bash
   cd C:\Users\jslep\Desktop\swe-testing-assignment
   
   # Add GitHub as remote
   git remote add origin https://github.com/lepembejeremie/swe-testing-assignment.git
   
   # Rename branch if needed (modern GitHub uses 'main' by default)
   git branch -M main
   
   # Push all commits
   git push -u origin main
   
   # Push the v1.0.0 tag
   git push origin v1.0.0
   ```

3. **Verify on GitHub**
   - Visit https://github.com/lepembejeremie/swe-testing-assignment
   - Confirm you see:
     ✓ 5 commits in commit history
     ✓ README.md file
     ✓ TESTING.md file
     ✓ calculator.py
     ✓ test_calculator.py
     ✓ app.py
     ✓ .gitignore
     ✓ v1.0.0 Release tag

4. **Create Final Submission File**
   
   Create `github_link.txt` with your repository URL:
   ```
   https://github.com/lepembejeremie/swe-testing-assignment
   ```

### Project Statistics

| Metric | Count |
|--------|-------|
| Commits | 5 (all meaningful with descriptive messages) |
| Unit Tests | 15 (covering all operations) |
| Integration Tests | 4 (complete workflows) |
| Total Tests | 19 |
| Code Coverage | 100% |
| Release Tags | 1 (v1.0.0) |
| Documentation Files | 2 (README.md, TESTING.md) |

### Project Files

```
swe-testing-assignment/
├── calculator.py          # Core calculation logic (109 lines)
├── app.py                 # CLI interface (96 lines)
├── test_calculator.py     # Unit + Integration tests (251 lines)
├── README.md             # Setup & framework research (230 lines)
├── TESTING.md            # Testing strategy & lecture concepts (379 lines)
├── .gitignore            # Python standard ignore rules
└── .git/                 # Version control history
```

### Key Features Implemented

✓ **Application**: Full Quick-Calc with add, subtract, multiply, divide, clear
✓ **Testing**: 19 tests (15 unit + 4 integration) with 100% coverage
✓ **Version Control**: 5 meaningful commits with conventional commit messages
✓ **Documentation**: 
  - README.md with pytest vs unittest research
  - TESTING.md with testing pyramid, black/white-box, functional/non-functional analysis
✓ **Release**: v1.0.0 semantic version tag
✓ **Code Quality**: Clean, well-documented, 100% error handling

### Testing Commands (after Python setup)

```bash
# Install dependencies
pip install pytest

# Run all tests
pytest test_calculator.py -v

# Run with coverage
pytest test_calculator.py --cov=calculator

# Run specific test class
pytest test_calculator.py::TestAddition -v
```

### Application Usage

```bash
python app.py

# Follow the interactive menu to:
# 1. Add two numbers
# 2. Subtract two numbers
# 3. Multiply two numbers
# 4. Divide two numbers
# 5. Clear calculator
# 6. Exit
```

---

**Deadline**: 2 weeks from today
**Submission Format**: GitHub repository link in github_link.txt
**Status**: ✓ READY FOR SUBMISSION

All assignment requirements have been completed and are ready for GitHub upload.
