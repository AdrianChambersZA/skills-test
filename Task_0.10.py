def common_letters(string1, string2):
    common_letter_list = ""
    common_letter_count = 0
    string1 = string1.lower()
    string2 = string2.lower()
    for character in string1:
        if character in string2:
            if not character in common_letter_list:
                common_letter_count += 1
                if common_letter_count > 1:
                    common_letter_list += ', ' + character
                else:
                    common_letter_list += character
    if common_letter_count == 1:
        return "Common letter: " + common_letter_list
    else:
        return "Common letters: " + common_letter_list

common_letters('House', 'Computers')