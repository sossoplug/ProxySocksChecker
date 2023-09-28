import os
import requests
from utils import write_to_log, load_environment_variables, read_addresses_from_file, save_to_file
from concurrent.futures import ThreadPoolExecutor

# Load configurations
config = load_environment_variables()

# ==================
# Check Proxy
# ==================
def check_http_https(proxy, protocol="http"):
    """
    Check the validity of a proxy.

    Args:
    - proxy (str):          The proxy address in the format "ip:port".
    - protocol (str):       Either "http" or "https".

    Returns:
    - bool:                 True if the proxy is valid, False otherwise.
    """
    response                = None
    try:
        response            = requests.get("http://www.google.com", proxies={protocol: f"{protocol}://{proxy}"}, timeout=5)

        if response.status_code == 200:
            return True



        return False

    except Exception as e:
        if response:
            write_to_log(f"[ERROR]: Check Failed with status: {response.status_code} for proxy {proxy}", "")

        write_to_log(f"[ERROR]:  {e} for proxy {proxy}", "")
        return False


# ==================
# Check Sock
# ==================
def check_sock(sock, version="socks5"):
    """
    Check the validity of a sock.

    Args:
    - sock (str):           The sock address in the format "ip:port".
    - version (str):        Either "socks4" or "socks5".

    Returns:
    - bool:                 True if the sock is valid, False otherwise.
    """
    response                = None
    try:
        response            = requests.get("http://www.google.com", proxies={version: f"{version}://{sock}"}, timeout=5)

        if response.status_code == 200:
            return True

        write_to_log(f"[ERROR]: Check Failed with status: {response.status_code} for sock {sock}" , "")

        return False

    except Exception as e:
        if response:
            write_to_log(f"[ERROR]: Check Failed with status: {response.status_code} for sock {sock}","")

        write_to_log(f"[ERROR]:  {e} for sock {sock}","")
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
        if config["HTTP_CHECK"] == "1":
            if check_http_https(address, "http"):
                results["working"].append(address)
                write_to_log(f"[SUCCESS]: Check Passed for HTTP: {address}", "")
            else:
                results["failed"].append(address)

        elif config["HTTPS_CHECK"] == "1":
            if check_http_https(address, "https"):
                results["working"].append(address)
                write_to_log(f"[SUCCESS]: Check Passed for HTTPS: {address}", "")
            else:
                results["failed"].append(address)

        elif config["SOCKS4_CHECK"] == "1":
            if check_sock(address, "socks4"):
                results["working"].append(address)
                write_to_log(f"[SUCCESS]: Check Passed for SOCKS4: {address}", "")
            else:
                results["failed"].append(address)

        elif config["SOCKS5_CHECK"] == "1":
            if check_sock(address, "socks5"):
                results["working"].append(address)
                write_to_log(f"[SUCCESS]: Check Passed for SOCKS5: {address}", "")
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

        addresses           = read_addresses_from_file(config["PROXY_LIST_FILEPATH"])

        write_to_log(f"[SUCCESS]: You Submitted  {len(addresses)} proxies To Check.\n", "")

        with ThreadPoolExecutor(max_workers=int(config["NUMBERS_OF_BOTS"])) as executor:
            executor.map(threaded_check, addresses, [config]*len(addresses), [results]*len(addresses))

        # Save results to files
        save_to_file(results["working"], config["WORKING_PROXIES_FILEPATH"])
        save_to_file(results["failed"], config["FAILED_PROXIES_FILEPATH"])

    except Exception as e:
        write_to_log(f"[ERROR]: Failed to run checker. {str(e)}", "ERROR")

