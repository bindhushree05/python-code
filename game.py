def calculate_flames(person1, person2):
    person1 = person1.lower()
    person2 = person2.lower()
    for char in person1:
        if char in person2:
            person1 = person1.replace(char, '', 1)
            person2 = person2.replace(char, '', 1)
    combined_length = len(person1) + len(person2)

    flames_result = ['Friends', 'Lovers', 'Affectionate', 'Marriage', 'Enemies', 'Siblings']

    result_index = combined_length % len(flames_result) - 1

    return flames_result[result_index]

def main():
    print("Welcome to the FLAMES game!")
    person1 = input("Enter the person1 name: ")
    person2 = input("Enter the person2 name: ")

    result = calculate_flames(person1, person2)

    print(f"\nResult: {person1} and {person2} are {result}")

if __name__ == "__main__":
    main()
