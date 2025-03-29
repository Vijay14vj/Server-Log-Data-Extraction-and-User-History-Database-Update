# Server Log Data Extraction and User History Database Update

## Project Overview
This project focuses on extracting email addresses and timestamps from server log files, transforming the data into a structured format, and storing it in both MongoDB and a relational database (SQLite or any SQL database). The extracted data is then analyzed using SQL queries.

## Technologies Used
- **Programming Language:** Python
- **Databases:** SQLite, MongoDB
- **Libraries:** Regex, pymongo, sqlite3
- **Data Format:** Server log file (mbox.txt)

## Problem Statement
The goal is to extract email addresses and their corresponding dates from a server log file, clean and structure the data, and insert it into a user history database. The database will be queried for insights such as email activity trends and domain statistics.

## Dataset
- The dataset consists of an `mbox.txt` file containing raw email logs.
- The log includes multiple email occurrences with timestamps.

## Project Workflow
### Step 1: Data Extraction
- Read the `mbox.txt` log file.
- Use regular expressions to extract email addresses and timestamps.

### Step 2: Data Transformation
- Convert extracted dates to a standardized format (YYYY-MM-DD HH:MM:SS).
- Structure the data into key-value pairs for database insertion.

### Step 3: Save Data to MongoDB
- Store processed data in a MongoDB collection named `user_history`.

### Step 4: Transfer Data to SQL Database
- Retrieve data from MongoDB.
- Insert records into an SQL table named `user_history`.
- Define primary key constraints for data integrity.

### Step 5: Data Analysis with SQL Queries
- List all unique email addresses.
- Count emails received per day.
- Find the first and last email date for each email address.
- Count total emails sent from different domains (e.g., gmail.com, yahoo.com).
- Formulate 10 SQL queries to analyze email trends.

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/server-log-analysis.git
   ```
2. Install dependencies:
   ```sh
   pip install pymongo sqlite3 re
   ```
3. Run the main script:
   ```sh
   python extract_logs.py
   ```

## Project Structure
```
📂 Server-Log-Analysis
├── 📂 data                  # Log files
├── 📂 scripts               # Python scripts for extraction and transformation
├── 📜 README.md             # Project documentation
├── 📜 requirements.txt      # Dependencies list
├── 📜 extract_logs.py       # Main script
├── 📜 queries.sql           # SQL queries
```

## Best Practices & Security
- **Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) coding standards.**
- **Store database credentials securely using environment variables.**
- **Use modular functions for better maintainability.**

## Conclusion
This project streamlines the process of extracting, storing, and analyzing email data from server logs. By leveraging MongoDB and SQL, it enables structured storage and efficient querying of user history records.

## Author
Vijay M

## License
This project is licensed under the MIT License.

