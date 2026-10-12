# Job Tracker Pipeline

A Python script that pulls live job postings from the [Adzuna API](https://developer.adzuna.com/) and prints them in a readable list. This is my first end-to-end data pipeline project: it connects to an external API, handles credentials safely, and turns the JSON response into usable output.

## What it does

1. Loads my API credentials from a local `.env` file.
2. Sends a request to the Adzuna US job search endpoint for "data engineer" roles in Columbus, returning 10 results.
3. Converts the JSON response into a Python dictionary.
4. Prints each posting's job title and company name.

## Tech used

- Python 3
- `requests` for the API call
- `python-dotenv` for loading credentials from the `.env` file
- Adzuna Jobs API

## Setup

1. Clone the repository:

```bash
   git clone https://github.com/YuliDowell12/job-tracker.git
   cd job-tracker
```

2. Install the dependencies:

```bash
   pip3 install requests python-dotenv
```

3. Get a free API ID and key from [developer.adzuna.com](https://developer.adzuna.com/).
4. Create a file named `.env` in the project folder with your credentials:

```
   APP_ID=your_app_id_here
   APP_KEY=your_app_key_here
```

The `.env` file is listed in `.gitignore`, so your keys are never uploaded to GitHub.

## Usage

```bash
python3 main.py
```

Example output format:

```
Data Platform Engineer - Syms Strategic Group, LLC
Strategic Student Program: AI & Engineering Data Internship (Spring 2027, GSCS) - Siemens
Slalom Flex (Project Based)- Data Migration Engineer - Slalom
Lead AI Engineer - Data Science and Algorithms - Maximus
Intern, Applied Technologies (Summer 2027) - Moderna
```

## Planned improvements

- Save results to a file or database instead of only printing them
- Filter for local and hybrid roles
- Make the search term and location configurable
- Add error handling for failed API requests
