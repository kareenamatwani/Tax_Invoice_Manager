def deduplicate_transactions(transactions):
    unique_transactions = []
    seen_transactions = set()

    for transaction in transactions:
        try:
            key = (transaction['Xref'], transaction['Total Loan Amount'])
        except KeyError:
            continue
        
        if key not in seen_transactions:
            unique_transactions.append(transaction)
            seen_transactions.add(key)

    return unique_transactions
