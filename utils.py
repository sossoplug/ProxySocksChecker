import os
import datetime
from dotenv import load_dotenv


# ==================
# Load Environment Variables
# ==================
def load_environment_variables():
    """
    Load configurations from the .env file.

    Returns:
    - dict:                             Dictionary containing environment variables.
    """
    try:
        load_dotenv()

        env_vars                        = {
            "PROXY_CHECK":              os.getenv("PROXY_CHECK"),
            "WORKING_PROXIES_FILEPATH": os.getenv("WORKING_PROXIES_FILEPATH"),
            "FAILED_PROXIES_FILEPATH":  os.getenv("FAILED_PROXIES_FILEPATH"),
            "SOCKS_CHECK":              os.getenv("SOCKS_CHECK"),
            "WORKING_SOCKS_FILEPATH":   os.getenv("WORKING_SOCKS_FILEPATH"),
            "FAILED_SOCKS_FILEPATH":    os.getenv("FAILED_SOCKS_FILEPATH"),
            "NUMBERS_OF_BOTS":          os.getenv("NUMBERS_OF_BOTS"),
            "LOG_OUTPUT_FILEPATH":      os.getenv("LOG_OUTPUT_FILEPATH"),
            "PROXY_LIST_FILEPATH":      os.getenv("PROXY_LIST_FILEPATH"),
            "SOCKS_LIST_FILEPATH":      os.getenv("SOCKS_LIST_FILEPATH")
        }
        return env_vars

    except Exception as e:
        write_to_log(f"[ERROR]: Failed to load environment variables. {str(e)}", "ERROR")
        return None


# ==================
# Write to Log
# ==================
def write_to_log(message, status):
    """
    Write a message to the log file.

    Args:
    - message (str):                    The message to be logged.
    - status (str):                     The status of the message (ERROR/SUCCESS).

    Returns:
    - None
    """
    try:
        timestamp                       = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(os.getenv("LOG_OUTPUT_FILEPATH"), "a") as log_file:
            log_file.write(f"[{timestamp}] INFO: [{status}]: {message}\n")
    except Exception as e:
        print(f"[ERROR]: Failed to write to log. {str(e)}")


# ==================
# Read Addresses from File
# ==================
def read_addresses_from_file(filepath):
    """
    Read proxies or socks from a specified file.

    Args:
    - filepath (str):                   Path to the file containing addresses.

    Returns:
    - list:                             List of addresses.
    """
    try:

        with open(filepath, "r") as file:
            addresses                   = file.readlines()

        return [address.strip() for address in addresses]

    except Exception as e:
        write_to_log(f"[ERROR]: Failed to read addresses from {filepath}. {str(e)}", "ERROR")
        return []




# ==================
# Save to File
# ==================
def save_to_file(data, filepath):
    """
    Save a list of data to a specified file.

    Args:
    - data (list):                      List of data to be saved.
    - filepath (str):                   Path to the file where data should be saved.

    Returns:
    - None
    """
    try:

        with open(filepath, 'w') as file:

            for item in data:
                file.write(f"{item}\n")

        write_to_log(f"[SUCCESS]: Successfully saved data to {filepath}.", "SUCCESS")

    except Exception as e:
        write_to_log(f"[ERROR]: Failed to save data to {filepath}. {str(e)}", "ERROR")



# ==================
# Wipe Files Clean
# ==================
def wipe_files_clean():
    """
    Wipe the result files clean before running the checker.
    """
    try:
        config                      = load_environment_variables()
        open(config["WORKING_PROXIES_FILEPATH"],    'w').close()
        open(config["FAILED_PROXIES_FILEPATH"],     'w').close()
        open(config["WORKING_SOCKS_FILEPATH"],      'w').close()
        open(config["FAILED_SOCKS_FILEPATH"],       'w').close()
        open(config["LOG_OUTPUT_FILEPATH"],         'w').close()
    except Exception as e:
        write_to_log(f"[ERROR]: Failed to wipe files clean. {str(e)}", "ERROR")