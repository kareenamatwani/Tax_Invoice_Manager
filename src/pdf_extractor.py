import csv
import re
import tabula

def extract_transactions_from_pdf(pdf_path, csv_path):
    
    tabula.convert_into(pdf_path, csv_path, output_format="csv", pages="all")
    
    transactions = extract_transactions_from_csv(csv_path)
    
    return transactions

def extract_transactions_from_csv(csv_path):
    transactions = []
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transaction = extract_transaction_details(row)
            transactions.append(transaction)
    return transactions

def extract_transaction_details(row):
    transaction = {}
    
    transaction['app_id'] = row.get('App ID')
    transaction['xref'] = row.get('Xref')
    transaction['settlement_date'] = row.get('Settlement Date')
    transaction['broker'] = row.get('Broker')
    transaction['sub_broker'] = row.get('Sub Broker')
    transaction['borrower_name'] = row.get('Borrower Name')
    transaction['description'] = row.get('Description')
    transaction['total_loan_amount'] = float(row.get('Total Loan Amoun', '0').replace(',', ''))  
    transaction['commission_rate'] = float(row.get('Comm Rate', '0').replace(',', ''))  
    transaction['upfront'] = float(row.get('Upfront', '0').replace(',', ''))  
    transaction['upfront_incl_gst'] = float(row.get('Upfront Incl GST', '0').replace(',', ''))  
    
    return transaction


pdf_path = 'C:/Users/My/Desktop/tax_invoice_project/src/pdf_file/Test PDF.pdf'
csv_path = 'C:/Users/My/Desktop/tax_invoice_project/src/pdf_file/table_1.csv'
transactions = extract_transactions_from_pdf(pdf_path, csv_path)
# for transaction in transactions:
#     print(transaction)

