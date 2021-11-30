#main method library

def name_length(name):
    return len(name)

def upper_case_name(name):
    return name.upper()

def lower_case_name(name):
    return name.lower()

if __name__ == "__main__":
    name="Umang"
    length=name_length(name)
    upper_case=upper_case_name(name)

    print(f"The length is {length} and the uppercase version is: {upper_case}")


#importing module


# import main_lib

# my_name="Fred"

# my_length=main_lib.name_length(my_name)
# my_lower_case=main_lib.lower_case_name(my_name)

# print(f"In my code,my length is {my_length} and my lowercase version is {my_lower_case}")