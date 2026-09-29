XOOX WP Hacker

WordPress Security Assessment Toolkit

Made by Pakistan Orakxai Anonymous

XOOX WP Hacker is a WordPress security assessment project designed for authorized security testing, research, and educational laboratory environments.

Features

Current project foundation:

* WordPress site scanning framework
* Configuration loading
* Security report structure
* HTML report template
* Modular utility structure
* Wordlist directory
* Documentation structure

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/XOOX-WP-Hacker.git
cd XOOX-WP-Hacker

Install Python dependencies:

pip install requests

Usage

python3 scanner.py https://example.com

The scanner will create its report inside:

reports/

Project Structure

XOOX-WP-Hacker/
├── scanner.py
├── utils/
│   ├── __init__.py
│   ├── config.py
│   └── helpers.py
├── reports/
│   └── template.html
├── data/
│   ├── config.json
│   └── wordlists/
├── docs/
│   └── README.md
├── README.md
├── LICENSE
└── .gitignore

Development

The current scan_site() implementation is a placeholder. Additional authorized security-assessment modules can be added to the project later.

Responsible Use

Use XOOX WP Hacker only against systems you own or have explicit authorization to test.

Do not use it for unauthorized access, credential theft, authentication bypass, private-data extraction, or other illegal activity.

Author

Pakistan Orakxai Anonymous

License

MIT License.
