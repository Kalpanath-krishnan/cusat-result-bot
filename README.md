# CUSAT Result Bot

An automated web scraper for CUSAT (Cochin University of Science and Technology) exam results using Playwright.

## Overview

This bot automates the process of fetching and extracting academic exam results from the CUSAT online exam portal. It navigates through the old results page, submits registration numbers, and extracts subject-wise performance data including marks and pass/fail status.

## Features

- 🤖 **Automated Result Extraction** - Scrapes multiple exam results automatically
- 📊 **Subject Tracking** - Tracks subject attempts and consolidates results
- ✅ **Pass/Fail Detection** - Identifies backlog subjects (subjects with FAIL status)
- 📈 **Summary Report** - Generates a final summary of all attempted subjects and backlogs
- 🔄 **Error Handling** - Gracefully handles navigation errors and retries

## Prerequisites

- Python 3.7+
- Playwright (for browser automation)
- A valid CUSAT registration number

## Installation

1. **Clone/Download the project:**
   ```bash
   git clone <repo-url>
   cd cusat-result-bot
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install playwright
   playwright install  # Install browser drivers
   ```

## Configuration

Edit `main.py` to set your registration number:

```python
REGISTER_NO = "YOUR_REGISTRATION_NUMBER"
```

The base URL is currently set to:
```python
BASE_URL = "http://exam.cusat.ac.in/erp5/cusat/Cusat-Home/home_oldresults"
```

## Usage


Run the script from the terminal:

```bash


python main.py
```

After running, your results will be saved automatically as `all_results.json` in the project directory. This file contains all the extracted and processed result data in JSON format for further use or analysis.

The bot will:
1. Open the CUSAT old results page in a browser
2. Find all "Download/View Result" links
3. For each result, submit your registration number
4. Extract subject codes, names, marks, and results
5. Display a final summary showing all subjects with attempt counts and backlog status

### Sample Output

```
📊 FINAL RESULTS

CS101 | Data Structures | Attempts: PASS, PASS | FINAL: PASS
CS102 | Algorithms | Attempts: FAIL, PASS | FINAL: PASS
CS103 | Database Systems | Attempts: FAIL | FINAL: FAIL

🔥 TOTAL BACKLOGS: 1
📚 TOTAL SUBJECTS: 3
```

## Project Structure

```
cusat-result-bot/
├── main.py              # Main scraper script
├── all_results.json     # Extracted results data (generated)
├── result.html          # HTML result output (generated)
├── README.md            # This file
└── __pycache__/        # Python cache directory
```

## How It Works

1. **Browser Launch** - Launches Chromium browser using Playwright (headless mode disabled for visibility)
2. **Page Navigation** - Opens CUSAT and waits for result links to load
3. **Link Iteration** - Loops through each "Download/View Result" link
4. **Registration Input** - Fills in registration number for each result
5. **Table Parsing** - Identifies and extracts data from the result table (2nd table on page)
6. **Data Storage** - Stores subject code, name, marks, and results
7. **Backlog Tracking** - Consolidates attempts and determines final status
8. **Summary Display** - Prints final summary with backlog count

## Error Handling

The bot includes error handling for:
- Missing input fields (skips without breaking)
- Navigation timeouts
- Empty result tables
- Missing submit buttons (tries alternative methods)
- Network delays (waits for network idle state)

## Output Files

- **all_results.json** - JSON file containing structured result data
- **result.html** - HTML representation of extracted results
- **Console Output** - Detailed progress and final summary printed to terminal

## Important Notes

⚠️ **Browser Window:** The browser window remains open after execution for manual inspection. Close it manually when done.

🔒 **Security:** Your registration number is stored in the code. Keep this file private if sharing the repo.

⏱️ **Timeouts:** Network timeouts are set to 10-15 seconds. Adjust if needed for slower connections.

## Troubleshooting

**Issue: Playwright browser drivers not installed**
```bash
playwright install
```

**Issue: Timeout errors**
- Check internet connection
- Increase timeout values in the code (e.g., `timeout=15000`)

**Issue: No result links found**
- Verify the CUSAT portal is the correct URL
- Check if the page structure has changed

## Future Enhancements

- [ ] Add JSON/CSV export functionality
- [ ] Schedule periodic result checks
- [ ] Email notifications for new results
- [ ] Interactive GUI for registration number input
- [ ] Headless mode option
- [ ] Support for multiple registration numbers

## License

[Specify your license here]

## Author

Created for automating CUSAT exam result extraction.

---

**Last Updated:** March 2026
