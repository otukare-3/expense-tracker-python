import expense

def test_canCreate():
    a = expense.Expense(description="description", amount="amount")
    
def test_canGetProperty():
    a = expense.Expense(description="description", amount="amount")
    assert a.description == "description"
    assert a.amount == "amount"