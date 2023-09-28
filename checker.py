import os
import requests
from utils import write_to_log, load_environment_variables, read_addresses_from_file, save_to_file
from concurrent.futures import ThreadPoolExecutor

# Load configurations
config = load_environment_variables()

# ==================
# Check Proxy
# ==================
def check_proxy(proxy):
    """
    Check the validity of a proxy.

    Args:
    - proxy (str):          The proxy address in the format "ip:port".

    Returns:
    - bool:                 True if the proxy is valid, False otherwise.
    """
    try:
        response            = requests.get("http://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=5)

        if response.status_code == 200:
            return True

        return False

    except:
        return False


# ==================
# Check Sock
# ==================
def check_sock(sock):
    """
    Check the validity of a sock.

    Args:
    - sock (str):           The sock address in the format "ip:port".

    Returns:
    - bool:                 True if the sock is valid, False otherwise.
    """
    try:
        response            = requests.get("http://www.google.com", proxies={"http": f"socks5://{sock}", "https": f"socks5://{sock}"}, timeout=5)

        if response.status_code == 200:
            return True

        return False

    except:
        return False


# ==================
# Threaded Check
# ==================
def threaded_check(address, config, results):
    """
    Threaded function to check the validity of an address (proxy or sock).

    Args:
    - address (str):        The proxy or sock to be checked.
    - config (dict):        Configuration from environment variables.
    - results (list):       Shared list to store results.

    Returns:
    - None
    """
    try:
        if config["PROXY_CHECK"] == "1":
            if check_proxy(address):
                results["working"].append(address)
            else:
                results["failed"].append(address)

        elif config["SOCKS_CHECK"] == "1":
            if check_sock(address):
                results["working"].append(address)
            else:
                results["failed"].append(address)

    except Exception as e:
        write_to_log(f"[ERROR]: Failed to check {address}. {str(e)}", "ERROR")


# ==================
# Main Checker Logic
# ==================
def run_checker():
    """
    Main logic to check the validity of proxies or socks based on the configuration using threading.

    Returns:
    - None
    """
    try:
        results             = {"working": [], "failed": []}
        addresses           = []

        if config["PROXY_CHECK"] == "1":
            addresses       = read_addresses_from_file(config["PROXY_LIST_FILEPATH"])

        elif config["SOCKS_CHECK"] == "1":
            addresses       = read_addresses_from_file(config["SOCKS_LIST_FILEPATH"])

        with ThreadPoolExecutor(max_workers=int(config["NUMBERS_OF_BOTS"])) as executor:
            executor.map(threaded_check, addresses, [config]*len(addresses), [results]*len(addresses))

        # Save results to files
        save_to_file(results["working"], config["WORKING_PROXIES_FILEPATH" if config["PROXY_CHECK"] == "1" else "WORKING_SOCKS_FILEPATH"])
        save_to_file(results["failed"], config["FAILED_PROXIES_FILEPATH" if config["PROXY_CHECK"] == "1" else "FAILED_SOCKS_FILEPATH"])

    except Exception as e:
        write_to_log(f"[ERROR]: Failed to run checker. {str(e)}", "ERROR")

