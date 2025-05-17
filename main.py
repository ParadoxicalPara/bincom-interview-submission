"""Author: Bamidele Oluwatosin"""
"""In this script is my solution to the Bincom interview questions"""

import psycopg2
import random

colors = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN", "ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN", "GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
# Creating a dictionary for the colors.
color_dict = dict()
for color in colors:
    if color in color_dict:
        color_dict[color] += 1
    else:
        color_dict[color] = 1

# Results in color_dict = {'GREEN': 10, 'YELLOW': 5, 'BROWN': 6, 'BLUE': 30, 'PINK': 5, 'ORANGE': 9, 'CREAM': 2, 'RED': 9, 'WHITE': 16, 'ARSH': 1, 'BLEW': 1, 'BLACK': 1}


"""Feature 1 solution:"""
def mean() -> float:
    return None # Beacause there is no mean for qualitative data and the shirt data is qualitative
# Output: None

"""Feature 2 solution:"""
def most_worn_color() -> str:
    max_color_count = 0
    most_worn_color = ""
    for color in color_dict:
        if color_dict[color] > max_color_count:
            max_color_count = color_dict[color]
            most_worn_color = color  
    return most_worn_color
# Output: 'BLUE'

"""Feature 3 solution:"""
def median() -> str:
    n = len(colors)
    median_color = colors[n // 2]  # Since n is odd
    # Kindly note sir/ma'am: if n is even, the median is undefined as colors cannot be added.
    return median_color
# Output: 'RED'

"""Feature 4 solution:"""
def variance() -> float:
    return None # Beacause there is no variance for qualitative data and the shirt data is qualitative
# Output: None

"""Feature 5 solution:"""
def probability_of_red() -> float:
    # Formula: frequecy of red / total number of colors
    return color_dict['RED'] / len(colors)
# Output: 0.09473684210526316

"""Feature 6 solution:"""
def postgresql_save():

    # Database connection configuration
    db_config = {
        'dbname': 'bincom_staff_shirt_color',
        'user': 'oluwatosin_bamidele',
        'password': 'thy367...',
        'host': 'localhost',
        'port': 5432
    }

    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dress_colours (
                id SERIAL PRIMARY KEY,
                colour VARCHAR(50) UNIQUE,
                frequency INT
            )
        """)

        # Insert data
        for colour, freq in color_dict.items():
            cursor.execute("""
                INSERT INTO dress_colours (colour, frequency)
                VALUES (%s, %s)
                ON CONFLICT (colour)
                DO UPDATE SET frequency = EXCLUDED.frequency
            """, (colour, freq))

        # Commit changes and close
        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully.")

    except Exception as e:
        print("Error:", e)


"""Feature 7 solution:"""
def search_num(num_list:list) -> int:
    # reading number from user:
    num = int(input("Enter the number to search for in the list of numbers: "))

    n = len(num_list)
    def search(idx=0):
        """This is an O(n) recursive searching algorithm that returns the first index num in num_list.
        I assumed that the num_list if not sorted else, I could have implemented an O(log(n)) algorithm."""
        if idx == n:
            return None
        elif num_list[idx] == num:
            return idx
        else: return search(idx + 1)
    
    return search(0)

# Test Cases:
#print(search_num(list(range(7)))) 
#print(search_num([3, 4, -1, 0, 4, 6]))

"""Feature 8 solution:"""
def generate_bin_and_int() -> str:
    bin_num = ''.join(random.choice(['0', '1']) for _ in range(4))
    int_num = int(bin_num, base=2)
    return "Binary: {}, Integer: {}".format(bin_num, int_num)

"""Feature 9 solution:"""
def sum_first_n_fibs(n=50):
    """Returns the sum of the n fibonacci numbers"""
    n1, n2 = 0, 1
    sum = n1
    for i in range(n-1):
        sum += n2
        n1, n2 = n2, n1 + n2
    return sum


def main():
    # Feature 1
    mean()
    # Feature 2
    most_worn_color()
    # Feature 3
    median()
    # Feature 4
    variance()
    # Feature 5
    probability_of_red()
    # Feature 6
    #postgresql_save()
    # Feature 7
    search_num(num_list=[3, 4, -1, 0, 4, 6])
    # Feature 8
    generate_bin_and_int()
    # Feature 9
    sum_first_n_fibs(n=50)

main()