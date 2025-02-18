# Web Crawler Setup and Usage Instructions

## Prerequisites

1. **Python 3.x**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Google Chrome**: The script uses the Chrome WebDriver, so you need Google Chrome installed.
3. **Chrome WebDriver**: Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a directory included in your system's PATH.

## Required Python Libraries

You need to install the following Python libraries:
- `re`
- `time`
- `pandas`
- `beautifulsoup4`
- `fake_useragent`
- `selenium`

You can install them using the following command:
```
pip install pandas beautifulsoup4 fake_useragent selenium
```

## Setup

1. Extract the contents of the ZIP file.
2. Place the `crawler.py` script in your desired directory.
3. Create an empty Excel file named `only_file_final.xlsx` in the same directory as the script.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing `crawler.py`.
3. Run the script using the command:
```
python crawler.py
```
4. A Chrome browser window will open and navigate to Google.
5. Wait for 60 seconds to manually enter your search query.
6. The script will start scrolling the page and collecting data.

## Output

- The script will create or update an Excel file named `only_file_final.xlsx` with the collected usernames.

## Notes

- Adjust the `save_interval` and `total_scrolls` variables in the script as needed.
- Ensure that the `only_file_final.xlsx` file is not open while the script is running.

## Troubleshooting

- If you encounter issues with the WebDriver, ensure it is compatible with your installed version of Chrome.
- Make sure all required Python libraries are installed.
