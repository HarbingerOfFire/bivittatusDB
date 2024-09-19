from DB_manage.funtions.common.db_utils import initialize_database, load_existing_table
from DB_manage.funtions.common.list_dir_pydb import list_pydb
from DB_manage.funtions.common.user_interaction_common import get_db_choice
from DB_manage.funtions.common.saving import save_table
from bdb_aggregate import pause_and_clean

def remove_rows_from_table(tb1):
    """
    Removes rows from a table based on user input.
    
    Args:
        tb1 (object): The table from which to remove rows.
    """
    while True:
        pause_and_clean(0)
        print(tb1)
        value_to_delete = input("Enter the value you wish to delete in the 'name' column (or 'exit' to exit): ").strip()
        if value_to_delete.lower() == 'exit':
            pause_and_clean(0)
            break

        try:
            tb1["name"] - value_to_delete
            print(f"Rows with value '{value_to_delete}' in column 'name' successfully deleted.")
        except AttributeError:
            print("The table object does not have a remove_rows method.")
        except Exception as e:
            print(f"Error when deleting rows: {e}")

def remove_rows():
    """
    Handles the process of selecting a database and table, removing rows, and saving the table.
    """
    # Get the user's choice (load existing DB or create a new one)
    db_choice = get_db_choice()

    if db_choice == "y":
        # Load existing DB and table
        db_name, table_name = list_pydb()
        if db_name is None or table_name is None:
            print("Error: No valid database or table selected.")
            return
        
        # Load the existing table
        tb1 = load_existing_table(db_name, table_name)
        if tb1 is None:
            print("Error: Table could not be loaded.")
            return

    # Initialize the table (if not already loaded)
    if tb1 is None:
        tb1 = initialize_database(db_name, table_name)
        if tb1 is None:
            print("Error: Table could not be initialized.")
            return

    remove_rows_from_table(tb1)
    print("Final table result:")
    print(tb1)
    save_table(tb1)

if __name__ == "__main__":
    remove_rows()