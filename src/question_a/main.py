import question_a

question_a.create_multiplication_table

def display_multiplication_table(table):
    
    if not table:
        print("  ")
        return

    # Get the number of rows and columns from the table
    row_count = len(table)
    col_count = len(table[0]) if row_count > 0 else 0
    
    # Print the header row
    header = "    " + " ".join(f"{i + 1:3}" for i in range(col_count))
    print(header)
    print("   " + "-" * len(header))
    
    # Print each row of the table
    for i, row in enumerate(table):
        row_display = f"{i + 1:2} " + " ".join(f"{val:3}" for val in row)
        print(row_display)

def main():
    while True:
        # Step 2: Create multiplication table
        table = create_multiplication_table(10, 10)  # 10 rows and 10 columns
        
        # Step 3: Display multiplication table
        display_multiplication_table(table)
        
        # Step 4: Ask user if they want to continue or quit
        user_choice = input("Create another multiplication table? (yes/no): ").strip().lower()
        if user_choice == 'no':
            print("Exiting program...")
            break
        elif user_choice != 'yes':
            print("Invalid input. Please enter 'yes' or 'no'.")


main()