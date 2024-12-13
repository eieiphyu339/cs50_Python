import pytest
import csv
from project import add_expense, view_expenses, analyze_spending

def test_add_expense(monkeypatch):
    mock_inputs = iter(["2024-12-01", "Food", "25.5", "Lunch"])
    monkeypatch.setattr("builtins.input", lambda _: next(mock_inputs))
    with open("expenses.csv", "w", newline="") as file:
        pass
    add_expense()
    with open("expenses.csv", "r") as file:
        reader = list(csv.reader(file))
        assert reader[-1] == ["2024-12-01", "Food", "25.5", "Lunch"]

def test_view_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["2024-12-01", "Food", "25.5", "Lunch"])
    assert view_expenses() is None

def test_analyze_spending(monkeypatch):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["2024-12-01", "Food", "25.5", "Lunch"])
    monkeypatch.setattr("matplotlib.pyplot.savefig", lambda *args, **kwargs: None)
    assert analyze_spending() is None
