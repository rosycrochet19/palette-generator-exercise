import random 

def palette():
    num_of_colours = random.randint(3,6)
    palette = []
    
    total_width = 500
    widths = [ random.randint(5,100) for _ in range(num_of_colours) ]
    widths = [ int((width/sum(widths))*total_width) for width in widths ]
    widths[-1] = widths[-1] + (total_width - sum(widths))

    for width in widths:
        colour = []
        for _ in range(3):
            colour.append(random.randint(0,255))         
        palette.append(
            {
                "colour" : f"({colour[0]}, {colour[1]}, {colour[2]})",
                "width" : width
            }
        )
    
    return palette

def name():
    words = [
        "Cerulean", "Lavender", "Azure", "Sky", "Crab", "Jungle", "Wave", "Dream", "Grey", "Night", "Garden",
        "Vanta", "Malta", "Christmas", "Tea", "Green", "Yellow", "Muse", "Blossom", "Sunset", "Day", "Hour",
        "Minute", "Calm", "Coffee", "Whiskey", "Grass", "Red", "Aloe", "Russet", "Rust", "Tree", "Despair",
        "Sleep", "Candle", "Trite", "Kale", "Jaffa", "Vera", "Terra", "Agave", "Plant", "Reality", "Tear",
        "Story", "Mountain", "Dusk", "Fountain", "Foundation", "Twilight", "Snow", "Rain", "Sun", "Wood"
    ]

    name = [random.choice(words)]
    
    if random.randint(0,10) < 9:
        name.append(random.choice(words))
        if random.randint(0,10) == 0: 
            name.append(random.choice(words))
    
    name = list(dict.fromkeys(name)) # prevent duplicate words

    return " ".join(name)