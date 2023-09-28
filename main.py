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

        if config["HTTP_CHECK"] == "1":
            write_to_log("[SUCCESS]: Checking Mode = HTTP\n\n", "")

        elif config["HTTPS_CHECK"] == "1":
            write_to_log("[SUCCESS]: Checking Mode = HTTPS\n\n", "")

        elif config["SOCKS4_CHECK"] == "1":
            write_to_log("[SUCCESS]: Checking Mode = SOCKS4\n\n", "")

        elif config["SOCKS5_CHECK"] == "1":
            write_to_log("[SUCCESS]: Checking Mode = SOCKS5\n\n", "")


        print("CHECKING IS ON GOING........")
        print("Press Ctrl+C to QUIT")

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
