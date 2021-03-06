import random

verb_list = ["Get",
        "Give",
        "Keep",
        "Take",
        "Pull",
        "Push",
        "Shrub",
        "Drift",
        "Clog",
        "Stand",
        "Brant",
        "Come",
        "Blob",
        "Plopper",
        "Splup",
        "Yeet",
        "Skunk",
        "Pangia",
        "Club",
        "Bark",
        "Plough",
        "Bear",
        "goat",
        "be",
        "do",
        "go"
        ]

preposition_list = ["up",
        "down",
        "up onto",
        "over",
        "in",
        "across",
        "through",
        "for",
        "on",
        "up onto for",
        "for",
        "askew",
        "away",
        "up away",
        "inbetween",
        "to the moon",
        "OVAH",
        "after",
        "amid",
        "alof",
        "aside",
        "behind",
        "from",
        "off",
        "out",
        "upon",
        ]

verb_list_marker = random.choice(range(len(verb_list)))
preposition_list_marker = random.choice(range(len(preposition_list)))

print("{} {}".format(verb_list[verb_list_marker],preposition_list[preposition_list_marker]))
print("-"*10)

definition_verb = ["reiterate",
        "illustrate",
        "edulcorate",
        "annihilate",
        "destruct",
        "build",
        "abduct",
        "pleasure",
        "hurt",
        "work",
        "become",
        "leave",
        "show",
        "believe",
        "play",
        "write",
        "pay",
        "remember",
        "hit",
        "strike",
        "kiss",
        "wait",
        "pull",
        "treasure",
        "absorb",
        "grasp",
        "advance",
        "amend",
        "attack",
        "ignite",
        "scratch",
        "slash",
        "command",
        "deviate",
        "detect",
        "poison",
        "treat",
        "yank",
        "suction"]

definition_object = ["someone",
        "something",
        "somebody"]

definition_adverb = ["viciously",
        "bravely",
        "with awe",
        "with despise",
        "uncontrollably",
        "reiteratedly",
        "with extreme care",
        "bearing grudge",
        "in laughter",
        "delightfully",
        "lightheartedly",
        "frolically",
        "restlessly",
        "in despair",
        "desperately",
        "with passion",
        "with lust",
        "in an Italian way",
        "as Berliners do",
        "just like in Michigan",
        "in Siena, Italy",
        "with embarrassment",
        "with serendipity",
        "timidly",
        "with audacity",
        "in secrecy"]



definition_verb_marker = random.choice(range(len(definition_verb)))
definition_object_marker = random.choice(range(len(definition_object)))
definition_adverb_marker = random.choice(range(len(definition_object)))

print("(Definition): To {} {} {}.".format(definition_verb[definition_verb_marker],definition_object[definition_object_marker],definition_adverb[definition_adverb_marker]))
