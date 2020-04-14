# The below is an code challenge. Will kata this soon.
def load_file(filename):
    letter_start = 65
    super_hero_names = {
        'first': {},
        'last': {}
    }
    with open(filename, 'r') as superhero:
        names = superhero.readlines()
        names = [x.rstrip() for x in names]

        count = 0
        for name in names:
            if count < 26:
                current_letter = chr(letter_start + count)
                super_hero_names['first'][current_letter] = name
            else:
                current_letter_less_26 = chr(letter_start + count - 26)
                super_hero_names['last'][current_letter_less_26] = name
            count += 1
        
        return super_hero_names


def generate_name(filename, person_name):
    superhero = load_file(filename)
    person_names = person_name.split(' ')
    super_names = []

    super_names.append(superhero['first'][person_names[0][0].upper()])

    for name in person_names[1:]:
        super_names.append(superhero['last'][name[0].upper()])

    return " ".join(super_names)


# print(generate_name('./python/edx/names.txt', "Peter daniel van onselen"))


#A common meme on social media is the name generator. These
#are usually images where they map letters, months, days,
#etc. to parts of fictional names, and then based on your
#own name, birthday, etc., you determine your own.
#
#For example, here's one such image for "What's your
#superhero name?": https://i.imgur.com/TogK8id.png
#
#Write a function called generate_name. generate_name should
#have two parameters, both strings. The first string will
#represent a filename from which to read name parts. The
#second string will represent an individual person's name,
#which will always be a first and last name separate by a
#space.
#
#The file with always contain 52 lines. The first 26 lines
#are the words that map to the letters A through Z in order
#for the person's first name, and the last 26 lines are the
#words that map to the letters A through Z in order for the
#person's last name.
#
#Your function should return the person's name according to
#the names in the file.
#
#For example, take a look at the names in heronames.txt
#(look in the drop-down in the top left). If we were to call
#generate_name("heronames.txt", "Addison Zook"), then the
#function would return "Captain Hawk": Line 1 would map to
#"A", which is the first letter of Addison's first name, and
#line 52 would map to "Z", which is the first letter of
#Addison's last name. The contents of those lines are
#"Captain" and "Hawk", so the function returns "Captain Hawk".
#
#You should assume the contents of the file will change when
#the autograder runs your code. You should NOT assume
#that every name will appear only once. You may assume that
#both the first and last name will always be capitalized.