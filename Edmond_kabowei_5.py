#1a
str = "The quick brown fox jumps over the lazy dog"
print(str)

#b
str = "The quick brown fox jumps over the lazy dog"
print(len(str))

#c
str = "The quick brown fox jumps over the lazy dog"
print(str.upper())

#d
str = "The quick brown fox jumps over the lazy dog"
print(str.lower())

#e
str = "The quick brown fox jumps over the lazy dog"
print(str.title())

#f
str = "The quick brown fox jumps over the lazy dog"
print(str[::-1])

#g
str = "The quick brown fox jumps over the lazy dog"
print(str[::-1].title())

#h
str = "The quick brown fox jumps over the lazy dog"
print(str.count("a"))

#i
str = "The quick brown fox jumps over the lazy dog"
print(str.count("the"))

#j
str = "The quick brown fox jumps over the lazy dog"
new_str = str.replace("the", "a")
print(new_str)

#3
str = "The quick brown fox jumps over the lazy dog"
frequency = {}

for letter in str:
    
    if letter.isalpha():
        
        letter = letter.lower()

        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

print(frequency)

#4
people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

for person, gender, person_age in zip(people, sex, age):
    interpolated_string = f"{person} the {gender} is {person_age} years old."
    print(interpolated_string)
