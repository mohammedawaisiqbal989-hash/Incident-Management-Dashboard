# chart module for creating visuals with matplotlib
# matplotlib was fairly nice to use here, need to learn it more

import matplotlib.pyplot as plt
from reports import *

def show_monthly_chart():
    print("\nGenerating monthly trend chart...")
    data = get_monthly_data()
    if not data:
        print("No data available for chart")
        return

    months = [row[0] for row in data]
    counts = [row[1] for row in data]

    plt.figure(figsize=(10, 6))
    plt.plot(months, counts, marker='o')
    plt.title('Monthly Incident Trend')
    plt.xlabel('Month')
    plt.ylabel('Number of Incidents')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/monthly_trend.png')
    print("Chart saved as output/monthly_trend.png")
    plt.show()

def show_category_chart():
    print("\nGenerating category breakdown chart...")
    data = get_category_data()
    if not data:
        print("No data available for chart")
        return

    categories = [row[0] for row in data]
    counts = [row[1] for row in data]

    plt.figure(figsize=(10, 6))
    plt.bar(categories, counts, color='steelblue')
    plt.title('Incidents by Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Incidents')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/category_breakdown.png')
    print("Chart saved as output/category_breakdown.png")
    plt.show()

def show_priority_chart():
    print("\nGenerating priority breakdown chart...")
    data = get_priority_data()
    if not data:
        print("No data available for chart")
        return

    priorities = [row[0] for row in data]
    counts = [row[1] for row in data]

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=priorities, autopct='%1.1f%%')
    plt.title('Incidents by Priority')
    plt.savefig('output/priority_breakdown.png')
    print("Chart saved as output/priority_breakdown.png")
    plt.show()