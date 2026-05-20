# this was hard to do i need to learn more for this
from database import *

def display_summary():
    print("\n" + "="*50)
    print("         DASHBOARD SUMMARY")
    print("="*50)

    total = get_count()
    print(f"Total Incidents: {total}")

    # there is probably a better way to do this but it works
    statuses = ['Open', 'Closed', 'In Progress']
    for s in statuses:
        r = run_query(f"SELECT COUNT(*) FROM incidents WHERE status = '{s}'")
        if r:
            print(f"{s}: {r[0][0]}")

    print("="*50)

def display_by_category():
    print("\n" + "="*50)
    print("      INCIDENTS BY CATEGORY")
    print("="*50)
    
    results = run_query("""
        SELECT category, COUNT(*) 
        FROM incidents 
        GROUP BY category 
        ORDER BY COUNT(*) DESC
    """)
    
    if not results:
        print("No data found")
        return
    
    for category, count in results:
        print(f"{category:30} {count}")
    
    print("="*50)

def display_open_incidents():
    print("\n" + "="*50)
    print("         OPEN INCIDENTS")
    print("="*50)
    
    results = run_query("""
        SELECT id, date, category, priority, description 
        FROM incidents 
        WHERE status = 'Open' 
        ORDER BY date ASC
    """)
    
    if not results:
        print("No open incidents found")
        return
    
    for row in results:
        print(f"\nID: {row[0]}")
        print(f"Date: {row[1]}")
        print(f"Category: {row[2]}")
        print(f"Priority: {row[3]}")
        print(f"Description: {row[4]}")
        print("-" * 40)
    
    print("="*50)

def search_incidents():
    print("\n" + "="*50)
    print("         SEARCH INCIDENTS")
    print("="*50)
    
    search_term = input("Enter search term: ").strip()
    
    if not search_term:
        print("Please enter a search term")
        return
    
    # using f-string for the query 
    query = f"""
        SELECT id, date, category, status, priority, description 
        FROM incidents 
        WHERE description LIKE '%{search_term}%' OR category LIKE '%{search_term}%'
        ORDER BY date ASC
    """
    
    results = run_query(query)
    
    if not results:
        print(f"No results found for '{search_term}'")
        return
    
    print(f"\nFound {len(results)} results for '{search_term}':\n")
    
    for row in results:
        print(f"ID: {row[0]} | Date: {row[1]} | {row[2]} | {row[3]} | {row[4]}")
        print(f"   {row[5]}")
        print()
    
    print("="*50)

def filter_by_date():
    print("\n" + "="*50)
    print("      FILTER BY DATE RANGE")
    print("="*50)
    
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()
    

    query = f"""
        SELECT id, date, category, status, priority, description 
        FROM incidents 
        WHERE date >= '{start_date}' AND date <= '{end_date}'
        ORDER BY date ASC
    """
    
    results = run_query(query)
    
    if not results:
        print(f"No incidents found between {start_date} and {end_date}")
        return
    
    print(f"\nFound {len(results)} incidents:\n")
    
    for row in results:
        print(f"ID: {row[0]} | Date: {row[1]} | {row[2]} | {row[3]} | {row[4]}")
        print(f"   {row[5]}")
        print()
    
    print("="*50)

# helpers used by the chart file
def get_category_data():
    return run_query("SELECT category, COUNT(*) FROM incidents GROUP BY category ORDER BY COUNT(*) DESC")

def get_monthly_data():
    # substr to get just the year-month part
    return run_query("SELECT substr(date, 1, 7), COUNT(*) FROM incidents GROUP BY substr(date, 1, 7) ORDER BY substr(date, 1, 7)")

def get_priority_data():
    return run_query("SELECT priority, COUNT(*) FROM incidents GROUP BY priority ORDER BY COUNT(*) DESC")
