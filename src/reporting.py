import sqlite3

def generate_sorted_loan_amount_report(period):
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    
    if period == 'daily':
        cursor.execute('''SELECT settlement_date, broker, total_loan_amount 
                          FROM transactions 
                          ORDER BY settlement_date DESC, total_loan_amount DESC''')
    elif period == 'weekly':
        cursor.execute('''SELECT strftime('%Y-%W', settlement_date) AS week, broker, SUM(total_loan_amount) 
                          FROM transactions 
                          GROUP BY week, broker 
                          ORDER BY week DESC, SUM(total_loan_amount) DESC''')
    elif period == 'monthly':
        cursor.execute('''SELECT strftime('%Y-%m', settlement_date) AS month, broker, SUM(total_loan_amount) 
                          FROM transactions 
                          GROUP BY month, broker 
                          ORDER BY month DESC, SUM(total_loan_amount) DESC''')
    
    report = cursor.fetchall()
    
    conn.close()
    return report

def generate_loan_amount_grouped_by_date():
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT settlement_date, SUM(total_loan_amount) 
                      FROM transactions 
                      GROUP BY settlement_date 
                      ORDER BY settlement_date''')
    
    report = cursor.fetchall()
    
    conn.close()
    return report

def define_tier_level(total_loan_amount):
    if total_loan_amount > 100000:
        return 'Tier 1'
    elif total_loan_amount > 50000:
        return 'Tier 2'
    elif total_loan_amount > 10000:
        return 'Tier 3'
    else:
        return 'Tier 4'

def generate_tiered_loan_amount_report():
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT settlement_date, 
                             COUNT(CASE WHEN total_loan_amount > 100000 THEN 1 END) AS tier1_count,
                             COUNT(CASE WHEN total_loan_amount > 50000 AND total_loan_amount <= 100000 THEN 1 END) AS tier2_count,
                             COUNT(CASE WHEN total_loan_amount > 10000 AND total_loan_amount <= 50000 THEN 1 END) AS tier3_count
                      FROM transactions 
                      GROUP BY settlement_date 
                      ORDER BY settlement_date''')
    
    report = cursor.fetchall()
    
    conn.close()
    return report

sorted_daily_report = generate_sorted_loan_amount_report('daily')
sorted_weekly_report = generate_sorted_loan_amount_report('weekly')
sorted_monthly_report = generate_sorted_loan_amount_report('monthly')

loan_amount_grouped_by_date = generate_loan_amount_grouped_by_date()

tiered_loan_amount_report = generate_tiered_loan_amount_report()


print("Sorted Loan Amount Report (Daily):")
for row in sorted_daily_report:
    print(row)

print("\nSorted Loan Amount Report (Weekly):")
for row in sorted_weekly_report:
    print(row)

print("\nSorted Loan Amount Report (Monthly):")
for row in sorted_monthly_report:
    print(row)

print("\nLoan Amount Grouped by Date:")
for row in loan_amount_grouped_by_date:
    print(row)

print("\nTiered Loan Amount Report:")
for row in tiered_loan_amount_report:
    print(row)