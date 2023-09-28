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
        load_environment_variables()

        # Wipe result files clean
        wipe_files_clean()

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
