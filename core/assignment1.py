def load_text_from_file(file_path: str, read_by_line=False):
    """
    Load text content from file
    :param file_path:
    :param read_by_line:
    :return: string or list of string
    """
    with open(file_path, "r", encoding="UTF-8") as f:
        if read_by_line:
            text = f.readlines()
        else:
            text = f.read()

    return text


def clean_up(text_to_clean_path, student_names_path):
    """
    f refers to text_to_clean.txt
    sf refers to student_names.txt
    use text to read in the appropriate file
    cleaned is used store the wanted characters
    :param text_to_clean_path: path to text_to_clean.txt
    :param student_names_path: path to student_names.txt
    :return: cleaned
    """
    text_to_be_cleaned = load_text_from_file(text_to_clean_path)

    cleaned = ""
    with open(student_names_path, "w", encoding="UTF-8") as sf:
        # lower case char, upper case char, blank, full stop - valid characters
        # insert code here to clean the file as per question 1
        for letter in text_to_be_cleaned:
            if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122 or ord(letter) == 32 or ord(
                    letter) == 46 or letter == "\n":
                sf.write(letter)
                cleaned += letter

    if cleaned[-1] != "\n":
        cleaned += "\n"

    return cleaned


def build_id(student_name_path):
    """
    f refers to the student_names.txt file created in clean_up()
    id_list is the list return with the id's created from the name / surname of each student
    :param student_name_path: path to student_name.txt
    :return: id_list
    """
    id_list = []
    # insert code here to create the id's as per question 2
    student_name_list = load_text_from_file(student_name_path, True)
    for name in student_name_list:
        str1 = ''
        for word in name:
            for letter in word:
                if 65 <= ord(letter) <= 90:
                    str1 += letter.lower()
        if 1 < len(str1) < 3:
            list2 = []
            for letter in str1:
                list2.append(letter)
            str1 = list2[0] + "x" + list2[1]
        id_list.append(str1)
    print(id_list)
    return id_list


def validate_password(password, password_path):
    """
    illegal_password is the list that is built up showing the invalid parts of the password
    Validate the password to verify if it is legal or not as per Question 3
    There is a password.txt file given to you to verify invalid passwords
    :param password: make use of the password found in main(), the test file will also have additional passwords to test
    :param password_path: path to password.txt
    :return: illegal_password
    """
    illegal_password = []
    # insert code here to validate all the conditions of the password as per question 3
    if len(password) < 8:
        illegal_password.append("TOO SHORT")
    if len(password) > 12:
        illegal_password.append("TOO LONG")
    for letter in password:
        if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122 or ord(letter) == 95 or letter.isdigit():
            continue
        else:
            illegal_password.append("WRONG CHARACTERS")
    upper_letter = False
    lower_letter = False
    for letter in password:
        if 65 <= ord(letter) <= 90:
            upper_letter = True
        if 97 <= ord(letter) <= 122:
            lower_letter = True
        if upper_letter is True and lower_letter is True:
            break
    if upper_letter is False or lower_letter is False:
        illegal_password.append("NOT MIXED CASE")
    if password[0].isdigit():
        illegal_password.append("LEADING DIGIT")
    password_text = load_text_from_file(password_path)
    for word in password_text.split():
        if password == word:
            illegal_password.append("CANNOT MAKE USE OF THIS PASSWORD")
    return illegal_password


def create_unique(id_list, unique_ids_path, create_emails_path, base_email_address="@student.bham.ac.uk"):
    """
    Adhere to the instructions in question 4 to determine a unique id for each student
    Write the content of the unique ids to the file unique_ids.txt - open / close the file correctly
    Write the content of the emails created to the file create_emails.txt - - open / close the file correctly
    :param id_list: the id_list that was returned in build_id() is used here to create the unique ids
    :param unique_ids_path: path to unique_ids.txt
    :param create_emails_path: path to create_emails.txt
    :param base_email_address:
    :return: final_list is returned and this list contains all of the unique student ids
    """
    final_list = []
    # insert code here to create unique ids
    rep_ids = []
    for name in id_list:
        name += '0000'
        if name not in final_list:
            final_list.append(name)
        else:
            rep_ids.append(name)
    for rep_id in rep_ids:
        count = 0
        times = len(final_list)
        while times > 0:
            if rep_id[:3] == final_list[len(final_list) - times][:3]:
                count += 1
            times -= 1
        front_zero_num = 3 - count // 10
        last_nums = ''
        while front_zero_num > 0:
            last_nums = '0' + last_nums
            front_zero_num -= 1
        last_nums += f'{count}'
        rep_id = rep_id[:3] + last_nums
        final_list.append(rep_id)
        # current_length += 1
        # times = current_length
    with open(unique_ids_path, "w", encoding="UTF-8") as f:
        for unique_id in final_list:
            f.write(unique_id + '\n')

    with open(create_emails_path, "w", encoding="UTF-8") as f:
        for unique_id in final_list:
            f.write(unique_id + f'{base_email_address}\n')

    return final_list


def create_short_address(addresses_path):
    """
    Open the addresses.txt file correctly where f = the file to be opened
    split the address up so that only the first part and the postcode make up the shorter address
    :param addresses_path: addresses.txt path
    :return: split_addrs is returned where the address1, postcode make up the list - this list is used for validate_pcode()
    """
    address_list = load_text_from_file(addresses_path, True)
    split_addrs = []
    # insert code here to create the shorter address
    filter_text = []
    for element in address_list:
        if element != '':
            filter_text.append(element)
    for address in filter_text:
        split_addrs.append([address.split(", ")[0], address.split(", ")[-1]])
    return split_addrs


def validate_pcode(split_addrs):
    """
    This function validates each character of the postcode
    :param split_addrs: this is passed from main(), obtained from the function create_short_address()
    :return: validate_pcode is a list that contains True False values for each postcode that is validated - see question 6
    """
    validate_pcode = []
    # insert code here to validate each character of the postcode
    count = 0
    length_ctrl = ''
    validate_1st = ''
    validate_2nd = ''
    validate_3rd = ''
    for element in split_addrs:
        validate_pcode.append(count)
        count += 1
        if len(element[1]) == 6:
            length_ctrl = 'True'
        else:
            element[1] = '$$$$$$'
            length_ctrl = 'False'
        validate_pcode.append(length_ctrl)
        if 65 <= ord(element[1][0]) <= 90:
            validate_1st = 'True'
        else:
            validate_1st = 'False'
        validate_pcode.append(validate_1st)
        if element[1][1].isdigit() and element[1][2].isdigit() and element[1][3].isdigit():
            validate_2nd = 'True'
        else:
            validate_2nd = 'False'
        validate_pcode.append(validate_2nd)
        if 65 <= ord(element[1][4]) <= 90 or 65 <= ord(element[1][5]) <= 90:
            validate_3rd = 'True'
        else:
            validate_3rd = 'False'
        validate_pcode.append(validate_3rd)
    return validate_pcode


def ids_addrs(short_addr, unique_ids_path):
    """
    This function reads in the unique_ids.txt file as f and creates a dictionary based on the id and the short address
    :param short_addr: passed in from main() - generated from create_short_address()
    :param unique_ids_path: path to unique_ids.txt
    :return: combo is the key / value pair, i.e. unique id and the short addr for each student
    """
    id_text = load_text_from_file(unique_ids_path)
    combo = {}
    # insert code here to create combo
    count = 0
    for unique_id in id_text.split():
        combo[f"{unique_id}"] = f"{short_addr[count]}"
        count += 1
    return combo


def main():
    base_path = "/media/xunjie/SilverBullet/Projects/Assignment-1_LM-Software-Workshop/resource/"
    text_to_clean_path = base_path + "text_to_clean.txt"
    student_names_path = base_path + "student_names.txt"
    password_path = base_path + "password.txt"
    unique_ids_path = base_path + "unique_ids.txt"
    create_emails_path = base_path + "create_emails.txt"
    addresses_path = base_path + "addresses.txt"
    id_list = []
    while True:
        print("\nStudent File Menu:")
        print("1. Perform clean up operation")
        print("2. Create ID's")
        print("3. Validate a Password")
        print("4. Create unique ID's")
        print("5. Reduce addresses")
        print("6. Validate postcode")
        print("7. Create ID with short address")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            clean_up(text_to_clean_path, student_names_path)
        elif choice == '2':
            id_list = build_id(student_names_path)
        elif choice == '3':
            validate_password("1abcDE%", password_path)
        elif choice == '4':
            create_unique(id_list, unique_ids_path, create_emails_path)
        elif choice == '5':
            short_addr = create_short_address(addresses_path)
        elif choice == '6':
            validate_pcode(short_addr)
        elif choice == '7':
            ids_addrs(short_addr, unique_ids_path)
        elif choice == '8':
            break
        else:
            print("Invalid choice! Please choose again.")


if __name__ == "__main__":
    main()
