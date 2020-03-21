def replace(s, old, new):
    return new.join(s.split(old))


song = "I love spom! Spom is my favorite food. Spom, spom, yum!"

print(replace("Mississippi", "i", "I") == "MIssIssIppI")
print(replace("Mississippi", "i", "I"))

print(replace(song, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
print(song)
print(replace(song, "om", "am"))

print(replace(song, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
print(replace(song, "o", "a"))
