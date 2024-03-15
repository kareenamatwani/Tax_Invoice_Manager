import pdf_extractor
import database
import sql_operations
import reporting

def run_tax_invoice_project(csv_path):
    # Extract transactions from PDF
    transactions = pdf_extractor.extract_transactions_from_csv(csv_path)
    
    # Deduplicate transactions based on Xref and Total Loan Amount
    deduplicated_transactions = deduplicate_transactions(transactions)
    
    # Create the database if it doesn't exist
    database.create_database()
    
    # Insert transactions into the database
    database.insert_transactions(deduplicated_transactions)
    
    # Generate reports
    print("\n")
    generate_reports()

def deduplicate_transactions(transactions):
    unique_transactions = []
    seen_xrefs = set()
    for transaction in transactions:
        xref = transaction['xref']
        total_loan_amount = transaction['total_loan_amount']
        if (xref, total_loan_amount) not in seen_xrefs:
            unique_transactions.append(transaction)
            seen_xrefs.add((xref, total_loan_amount))
    return unique_transactions

def generate_reports():
    start_date = '10/10/2023'
    end_date = '21/10/2023'
    total_loan_amount = sql_operations.calculate_total_loan_amount(start_date, end_date)
    print(f"Total loan amount during {start_date} to {end_date}: {total_loan_amount}")
    
    # Calculate highest loan amount given by each broker
    highest_loan_by_broker = sql_operations.calculate_highest_loan_by_broker()
    print("Highest loan amount given by each broker:")
    for broker, highest_loan_amount in highest_loan_by_broker:
        print(f"{broker}: {highest_loan_amount}")

    sorted_daily_report = reporting.generate_sorted_loan_amount_report('daily')
    sorted_weekly_report = reporting.generate_sorted_loan_amount_report('weekly')
    sorted_monthly_report = reporting.generate_sorted_loan_amount_report('monthly')
    
    loan_amount_grouped_by_date = reporting.generate_loan_amount_grouped_by_date()
    
    tiered_loan_amount_report = reporting.generate_tiered_loan_amount_report()

if __name__ == "__main__":
    csv_path = "C:/Users/My/Desktop/tax_invoice_project/src/pdf_file/table_1.csv"
    run_tax_invoice_project(csv_path)
