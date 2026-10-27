try:
    items = [10, 20, 30]
    # This will raise an IndexError:
    value = items[5] 
    
    # Or if a string conversion failed, it would raise a ValueError:
    #number = int("not_a_number")

except IndexError as e:
    # Catches index out of range errors specifically
    print(f"Index error handled: {e}")

except ValueError as e:
    # Catches invalid value conversion errors specifically
    print(f"Value error handled: {e}")

except Exception as e:
    # Catches any other standard exception not handled above
    print(f"An unexpected error occurred: {e}")
