from utils import load_environment_variables, write_to_log, wipe_files_clean
from checker import run_checker


# ==================
# Main Driver Function
# ==================
def main():
    """
    Main driver function.
    """
    try:
        # Load environment variables
        config = load_environment_variables()

        # Wipe result files clean
        wipe_files_clean()

        if config["PROXY_CHECK"] == "1":
            write_to_log(f"[SUCCESS]: Checking Mode = PROXY\n\n", "")

        elif config["SOCKS_CHECK"] == "1":
            write_to_log(f"[SUCCESS]: Checking Mode = SOCKS\n\n", "")

        # Run the checker
        run_checker()

        # Print summary (this can be expanded upon)
        print("Checker has completed its run. Check the result files and logs for details.")

    except Exception as e:
        write_to_log(f"[ERROR]: Main function encountered an error. {str(e)}", "ERROR")

# ==================
# Script Execution
# ==================
if __name__ == "__main__":
    main()
