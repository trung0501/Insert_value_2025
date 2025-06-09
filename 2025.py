def input_n():
    while True:
        try:
            n = int(input("Enter integer n (15 <= n <= 25 and n is even): "))
            if 15 <= n <= 25 and n % 2 == 0:
                return n
            else:
                print("n must be from 15 to 25 and is even. Enter again")
        except ValueError:
            print("Please enter the valid integer.")

def create_array(n):
    return [i * 2 for i in range(1, n + 1)]

def insert_2025(t):
    between = len(t) // 2
    t_add= t.copy()
    t_add.insert(0, 2025)         
    t_add.insert(between + 1, 2025)  
    t_add.append(2025)           
    return t_add

n = input_n()
t = create_array(n)

print("\n Initial array:")
print(t)

t_after_insert = insert_2025(t)

print("\n The array after inserting 2025 into the head, middle, last:")
print(t_after_insert)