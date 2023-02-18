
def next_movie():
    import spacy
#load md in spacy to perform a higher advanced language model
    nlp = spacy.load('en_core_web_md')
    hulk = 'Planet Hulk: Will he save their world or destroy it? When the Hulk becomes too dangerous for teh Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is solde into slavery and trained as a gladiator.'
    hulk_nlp = nlp(hulk)
#create an empty description list
    dskrpn_list = []
    with open('movies.txt', 'r') as list:
#read all lines in the file
        lines = list.readlines()
        for line in lines:
            line_split = line.strip('\n').split(' :')
#add all the information to the description list
            dskrpn_list.append(line_split)
        max_similarity = 0
        max_movie = None

#compare the similarity from each description line with Hulk's description
        for dskpn in dskrpn_list:
            similarity = nlp(dskpn[1]).similarity(hulk_nlp)
            # find the one with the highest similarity
            if similarity > max_similarity:
                max_similarity = similarity

                max_movie = dskpn[0]
        print(f'You may like {max_movie}')

next_movie()
