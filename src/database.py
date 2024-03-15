import sqlite3

def create_database():
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        app_id TEXT,
                        xref TEXT,
                        settlement_date TEXT,
                        broker TEXT,
                        sub_broker TEXT,
                        borrower_name TEXT,
                        description TEXT,
                        total_loan_amount REAL,
                        commission_rate REAL,
                        upfront REAL,
                        upfront_incl_gst REAL
                    )''')
    
    conn.commit()
    conn.close()


def insert_transactions(transactions):
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()

    for transaction in transactions:
        # Check if the transaction already exists in the database
        cursor.execute('''SELECT COUNT(*) FROM transactions 
                          WHERE app_id = ? AND xref = ? AND settlement_date = ?''',
                       (transaction['app_id'], transaction['xref'], transaction['settlement_date']))
        existing_count = cursor.fetchone()[0]

        if existing_count == 0:
          
            cursor.execute('''INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                           (transaction['app_id'], transaction['xref'], transaction['settlement_date'],
                            transaction['broker'], transaction['sub_broker'], transaction['borrower_name'],
                            transaction['description'], transaction['total_loan_amount'], transaction['commission_rate'],
                            transaction['upfront'], transaction['upfront_incl_gst']))
    
    conn.commit()
    conn.close()
import sqlite3

import sqlite3

def remove_duplicates():
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()

    # Identify duplicate records based on app_id, xref, and settlement_date
    cursor.execute('''SELECT app_id, xref, settlement_date, MIN(rowid)
                      FROM transactions
                      GROUP BY app_id, xref, settlement_date
                      HAVING COUNT(*) > 1''')
    duplicate_records = cursor.fetchall()

    for record in duplicate_records:
        app_id, xref, settlement_date, min_rowid = record
        cursor.execute('''DELETE FROM transactions
                          WHERE app_id = ? AND xref = ? AND settlement_date = ?
                          AND rowid != ?''', (app_id, xref, settlement_date, min_rowid))

    conn.commit()
    conn.close()


remove_duplicates()

