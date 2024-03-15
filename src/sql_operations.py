
import sqlite3

def calculate_total_loan_amount(start_date, end_date):
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT SUM(total_loan_amount) 
                      FROM transactions 
                      WHERE settlement_date BETWEEN ? AND ?''', (start_date, end_date))
    
    total_loan_amount = cursor.fetchone()[0]
    
    conn.close()
    return total_loan_amount


def calculate_highest_loan_by_broker():
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT broker, MAX(total_loan_amount) 
                      FROM transactions 
                      GROUP BY broker''')

    highest_loan_by_broker = cursor.fetchall()

    conn.close()
    return highest_loan_by_broker

# Example usage
# start_date = '2024-01-01'
# end_date = '2024-01-31'
# total_loan_amount = calculate_total_loan_amount(start_date, end_date)
# print(f"Total loan amount during {start_date} to {end_date}: {total_loan_amount}")

# highest_loan_by_broker = calculate_highest_loan_by_broker()
# print("Highest loan amount given by each broker:")
# for broker, highest_loan_amount in highest_loan_by_broker:
    # print(f"{broker}: {highest_loan_amount}")


