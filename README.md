
# Tax Invoice Manager: Transaction Analysis and Reporting System

## Description
The Tax Invoice Project is a Python-based application designed to manage and analyze transactions related to tax invoices. It includes functionalities to extract transaction data from PDF files, deduplicate transactions, store them in a SQLite database, and generate various types of reports.

## Topics

### Introduction
- Overview: The Tax Invoice Project aims to streamline the process of managing and analyzing tax invoice transactions.
- Objective: The project's primary objective is to provide a robust solution for businesses to efficiently handle tax invoice data and generate insightful reports for analysis.

### Features
- Transaction data extraction from PDF files.
- Deduplication of transactions based on unique identifiers.
- Storage of transactions in a SQLite database.
- Generation of reports based on different criteria.

### Components
- PDF Extractor
The PDF Extractor module is a critical component of the Tax Invoice Manager responsible for automating the extraction of transaction data from PDF files. This module utilizes the Tabula library, a powerful tool for parsing tables embedded within PDF documents, to extract tabular data containing transaction details.
-  How It Works
PDF Parsing: The PDF Extractor employs Tabula's parsing capabilities to identify and extract tables present in PDF documents. Tabula analyzes the structure of the PDF file and intelligently identifies table boundaries to ensure accurate extraction.
Table Extraction: Once the tables are identified, Tabula extracts the tabular data, preserving the original formatting and layout of the document. This includes transaction details such as application ID, Xref, settlement date, broker information, borrower name, description, total loan amount, commission rate, upfront payment, and upfront payment inclusive of Goods and Services Tax (GST).
Conversion to CSV: After extracting the tabular data, the PDF Extractor converts it into a Comma-Separated Values (CSV) format. This conversion facilitates further processing and analysis of the transaction data using standard data processing tools.
Data Integrity: The PDF Extractor ensures the integrity of the extracted data by handling numeric fields appropriately. It removes commas from numeric fields and converts them to appropriate data types (e.g., floats) to maintain consistency and accuracy in the extracted transaction details.

- Database Module: Handles database operations including creation, insertion, and querying.
- SQL Operations: Module containing SQL queries for report generation.
- Reporting: Functions for generating various types of reports.

### Functionality
- Extract transactions from PDF files.
- Deduplicate transactions based on unique identifiers.
- Store transactions in a database for easy retrieval and analysis.
- Generate reports based on daily, weekly, and monthly periods.
- Calculate tier levels for transactions based on predefined criteria.

### Implementation
- Usage of Python programming language.
- Utilization of SQLite for database management.
- Modular structure for easy maintenance and scalability.
- Clear separation of concerns for each component.

### Usage
1. Clone the repository from GitHub using the command:
   ```
   git clone https://github.com/kareenamatwani/tax_invoice_project.git
   ```
2. Navigate to the project directory:
   ```
   cd tax_invoice_project
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the project by executing the `run.py` file:
   ```
   python run.py
   ```
5. Follow the prompts and instructions to extract transaction data, generate reports, and analyze the data.

**Note:**
## Testing Instructions
### Sample Input Files
- Before running the application, you can use the sample input files provided in the src/pdf_file folder for testing purposes. These files include:
  table_1.csv: This is the generated csv during the testing after the extraction from PDF provided.
  Test PDF.pdf: This PDF (tax invoice) file contains sample data for testing the application (currently Tabular data).


Thanks for reading!

