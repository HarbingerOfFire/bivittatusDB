# Make sure you run it in the same directory as BivittatusDB, not in the example directory.
import BivittatusDB as bdb

test_db = bdb.database("test").init()

tb1 = test_db.make_table("table1", 
                         ("id", "name"), 
                         (int(), str()), 
                         "id")

tb1 @ bdb.ON

tb1 + (1, "Alice")
tb1 + (2, "Bob")
tb1 + (3, "Cindy")

print(tb1)