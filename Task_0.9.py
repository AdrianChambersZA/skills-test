def vowels(string):
    vowel_list = ""
    vowel_count = 0
    for character in string:
        if character in ['a','e','i','o','u','y','A','E','I','O','U','Y']:
            if not character in vowel_list:
                vowel_count += 1
                if vowel_count > 1:
                    vowel_list = vowel_list + ', ' + character.lower()
                else:
                    vowel_list += character.lower()
    if vowel_count == 1:
        return "Vowel: " + vowel_list
    else:
        return "Vowels: " + vowel_list

vowels("Umuzi")