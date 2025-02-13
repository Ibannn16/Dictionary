# John Ivan L. Mostoles 12-CPE-01
# Dictionary in Python

Dictionary = {
    "Accismus": "Pretending to be disinterested in something you actually want.",
    "Apricate": "To bask in the sunshine.",
    "Bafflegab":" Confusing or unintelligible jargon.",
    "Bailiwick":"A person's area of expertise or authority.",
    "Cacophony": "A harsh, discordant mixture of sounds.",
    "Clandestine": "Kept secret or done secretively.",
    "Convivial": "Friendly and enjoyable.",
    "Credulity": "A tendency to believe things too readily.",
    "Effervescent": "Bubbly, lively, or enthusiastic.",
    "Ephemeral": "Lasting for a very short time.",
    "Erudite": "Having or showing great knowledge or learning.",
    "Fatuous": "Silly and pointless.",
    "Flibbertigibbet": "A frivolous or flighty person.",
    "Garrulous": "Excessively talkative, especially on trivial matters.",
    "Ineluctable": "Unable to be resisted or avoided.",
    "Insouciant": "Showing a lack of concern.",
    "Lachrymose": "Tearful or given to weeping.",
    "Loquacious": "Tending to talk a great deal; talkative.",
    "Mellifluous": "(of a voice or words) sweet or musical; pleasant to hear.",
    "Obsequious": "Excessively attentive or flattering.",
    "Pauciloquent": "Using few words; terse or concise.",
    "Perspicacious": "Having a ready grasp of things; shrewd or discerning.",
    "Pneumonoultramicroscopicsilicovolcanoconiosis": "A lung disease caused by inhaling very fine silica dust.",
    "Pulchritudinous": "Having great physical beauty.",
    "Quixotic": "Exceedingly idealistic; unrealistic and impractical.",
    "Raconteur": "A person who tells anecdotes in a skillful and amusing way.",
    "Sycophant": "A person who tries to win favor from wealthy or influential people by flattering them.",
    "Tittynope": "A small quantity of anything left over.",
    "Uxorious": "Having or showing an excessive or submissive fondness for one's wife.",
    "Verbiage": "Speech or writing that uses too many words or excessively technical expressions."
}
while True:
    name = input("Search a Word: ")
    print(Dictionary.get(name, "Word is not on the List!"))