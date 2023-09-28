# Proxy and Socks Checker 🛠️

A utility tool designed to validate a list of proxies or socks. It checks the validity of each address and categorizes them into working and failed lists.

## Features 🌟

- **Proxy and Socks Validation**: Quickly validate a list of proxies or socks.
- **Environment Configuration**: Easily configure settings using a `.env` file.
- **Logging**: Detailed logging of the checking process.
- **Threading**: Utilizes multiple threads for faster checking.

## Requirements 📋

- Python environment.
- Required libraries listed in `requirements.txt`.
- `.env` file with the following configurations:
  - `PROXY_CHECK` (BOOL): To enable or disable proxy checking.
  - `WORKING_PROXIES_FILEPATH`: Path to save working proxies.
  - `FAILED_PROXIES_FILEPATH`: Path to save failed proxies.
  - `SOCKS_CHECK` (BOOL): To enable or disable socks checking.
  - `WORKING_SOCKS_FILEPATH`: Path to save working socks.
  - `FAILED_SOCKS_FILEPATH`: Path to save failed socks.
  - `NUMBERS_OF_BOTS`: Number of threads/bots to use for checking.
  - `LOG_OUTPUT_FILEPATH`: Path to save the log file.
  - `PROXY_LIST_FILEPATH`: Path to the file containing the list of proxies to check.
  - `SOCKS_LIST_FILEPATH`: Path to the file containing the list of socks to check.

## File Format:

For `PROXY_LIST_FILEPATH` and `SOCKS_LIST_FILEPATH`, each line should contain a single proxy or sock in the format:
```<IP>:<PORT>```

## Usage 🚀

1. **Setting Up a Virtual Environment**:
   - Create a virtual environment: `python -m venv venv`
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS and Linux: `source venv/bin/activate`

2. **Install Dependencies**:
   - Install the required packages: `pip install -r requirements.txt`

3. Configure your `.env` file with the appropriate settings.

4. Populate your proxy or socks list file.

5. Run the script: `python main.py`

6. Check the result files and logs for details.

## Contribution 🤝

Feel free to contribute to this project by creating issues or sending pull requests. All contributions are welcomed!

