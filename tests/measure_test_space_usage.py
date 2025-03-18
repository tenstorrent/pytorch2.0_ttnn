# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
import argparse
import logging

REPORT_FILE = "disk_usage_report.txt"


def setup_logging(log_level):
    """Sets up the logging configuration."""
    logging.basicConfig(
        filename="measure_test_space.log",
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="w",  # Overwrites the log file each time the script runs
    )


def get_total_disk_usage():
    """Returns the total disk usage of all mounted filesystems in kilobytes."""
    try:
        result = subprocess.check_output(["df", "--block-size=K"]).decode("utf-8")
        total_usage = 0
        for line in result.splitlines()[1:]:
            columns = line.split()
            if len(columns) >= 3:
                used_space = int(columns[2][:-1])  # Remove the 'K' and convert to int
                total_usage += used_space
        logging.info(f"Total disk usage across all filesystems: {total_usage} KB")
        return total_usage
    except Exception as e:
        logging.error(f"Error getting total disk usage: {str(e)}")
        return 0


def run_test_and_measure_space(test, target_dir):
    """Runs a pytest test and measures the disk space used."""
    initial_space = get_total_disk_usage()
    logging.debug(f"Initial disk usage for {test}: {initial_space} KB")

    try:
        logging.info(f"Running test: {test}")
        result = subprocess.run(["pytest", test], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

        if result.returncode != 0:
            error_message = result.stderr.decode("utf-8").strip()
            logging.error(f"Test failed: {test} - {error_message}")
            return None, f"Test failed: {error_message}"

        final_space = get_total_disk_usage()
        logging.debug(f"Final disk usage for {test}: {final_space} KB")

        space_used = final_space - initial_space
        logging.info(f"Test completed: {test}, used {space_used} KB")
        return space_used, None

    except Exception as e:
        logging.error(f"Exception occurred while running test {test}: {str(e)}")
        return None, f"Exception occurred: {str(e)}"


def load_completed_tests(report_file):
    """Loads the list of completed tests from the report file."""
    completed_tests = set()
    if os.path.exists(report_file):
        with open(report_file, "r") as report:
            for line in report:
                if line.startswith("models/"):
                    test_name = line.split(": ")[0]
                    completed_tests.add(test_name)
    return completed_tests


def main():
    # Set up logging
    parser = argparse.ArgumentParser(description="Measure disk usage for each pytest test.")
    parser.add_argument("target_dir", help="Directory to be used by pytest during testing.")
    parser.add_argument(
        "--log-level", default="INFO", help="Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)."
    )
    args = parser.parse_args()

    # Set up logging with the chosen log level
    log_level = getattr(logging, args.log_level.upper(), logging.INFO)
    setup_logging(log_level)
    logging.info("Script started.")

    target_dir = args.target_dir
    logging.info(f"Monitoring disk space in directory: {target_dir}")

    # Get the list of all tests using pytest's collection mechanism
    result = subprocess.run(["pytest", "--collect-only", "-q"], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8").strip()

    # Filter out the collected test names
    tests = [line for line in output.splitlines() if line.startswith("models/")]
    total_tests = len(tests)
    logging.info(f"Collected {total_tests} tests.")

    # Load completed tests from the report
    completed_tests = load_completed_tests(REPORT_FILE)
    logging.info(f"Found {len(completed_tests)} completed tests in report file.")

    # Prepare to write the report (append mode)
    with open(REPORT_FILE, "a") as report:
        # Run each test individually and measure disk space usage
        for i, test in enumerate(tests, 1):
            test_name = test.split(": ")[0].strip()
            if test_name in completed_tests:
                logging.info(f"Skipping already completed test: {test}")
                print(f"Skipping already completed test: {test}")
                continue

            logging.info(f"Processing test {i}/{total_tests}: {test}")
            print(f"Processing test {i}/{total_tests}: {test}")

            space_used, error_message = run_test_and_measure_space(test, target_dir)
            if error_message:
                report.write(f"{test}: FAILED - {error_message}\n")
                logging.error(f"{test} FAILED - {error_message}")
                print(f"{test} FAILED - {error_message}")
            else:
                report.write(f"{test}: {space_used} KB used on disk\n")
                logging.info(f"{test} used {space_used} KB on disk")
                print(f"{test} used {space_used} KB on disk")
            report.flush()  # Ensure progress is saved immediately

    logging.info("Script completed. Report saved.")
    print(f"\nReport saved to {REPORT_FILE}")


if __name__ == "__main__":
    main()
