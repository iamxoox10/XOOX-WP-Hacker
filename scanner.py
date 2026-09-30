import argparse
import requests
from utils.config import load_config
from utils.helpers import scan_site

TOOL_NAME = "XOOX WP Hacker"
AUTHOR = "Pakistan Orakxai Anonymous"

def generate_report(data):
    # Logic to generate the report goes here
    # This could involve using the report template and filling in the details
    # For simplicity, we'll just return the data as is
    return data

def save_report(report_data):
    with open("reports/report.html", "w") as file:
        file.write(report_data)

def main():
    print("=" * 50)
    print(TOOL_NAME)
    print("Made by " + AUTHOR)
    print("Authorized WordPress Security Assessment")
    print("=" * 50)

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL of the WordPress site to scan")
    args = parser.parse_args()

    config = load_config()

    # Perform scanning
    site_data = scan_site(args.url, config)

    # Generate report
    report_data = generate_report(site_data)

    # Save report
    save_report(report_data)

    print("Scanning completed. Check the reports/ directory for the detailed report.")

if __name__ == "__main__":
    main()
