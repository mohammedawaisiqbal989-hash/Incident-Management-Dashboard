from database import *
from importer import *
from reports import *
from charts import *


def main():
    print("Starting Incident Dashboard System...")
    print("====================================")
    
    setup_database()
    
    while True:
        print("\n" + "="*50)
        print("      INCIDENT DASHBOARD SYSTEM")
        print("="*50)
        print("1. Import data from CSV file")
        print("2. Show dashboard sumamry ")
        print("3. View all incidents by category")
        print("4. Show open incidents only")
        print("5. Search for incidents")
        print("6. Filter by date range")
        print("7. Show monthly trend chart")
        print("8. Show category breakdown chart")
        print("9. Exit the program")
        print("="*50)
        
        try:
            choice = input("\nEnter choice (1-9): ")
            
            if choice == '1':
                import_csv_data()
            elif choice == '2':
                display_summary()
            elif choice == '3':
                display_by_category()
            elif choice == '4':
                display_open_incidents()
            elif choice == '5':
                search_incidents()
            elif choice == '6':
                filter_by_date()
            elif choice == '7':
                show_monthly_chart()
            elif choice == '8':
                show_category_chart()
            elif choice == '9':
                print("\nThanks for using the dashboard! Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 9")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"Something went wrong: {e}")
            print("Please try again")

if __name__ == "__main__":
    main()
