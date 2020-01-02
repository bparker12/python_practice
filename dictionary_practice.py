# Create an empty dictionary
animal = dict()
# Add k/v pairs
animal["name"] = "Kevin"
animal["breed"] = "Bulldog"
animal["age"] = 5

print(animal)

for (key, value) in animal.items():
    print(f"{key}: {value}")

word_definitions = dict()

word_definitions["awesome"] = "The feeling of students when they are learning Python"

word_definitions["noob"] = "Beginner or someone not very good at a game"
word_definitions["pro"] = "Someone that is very talented and typically paid for what they do"
word_definitions["developer"] = "Something that I would like to be my profession"



# print(word_definitions)
for (key, value) in word_definitions.items():
    print(f"{key}: {value}")

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

for (key, value) in idioms.items():
    print(key + ':' + " ".join(value) )