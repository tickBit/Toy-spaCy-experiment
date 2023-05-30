import spacy
nlp = spacy.load('en_core_web_lg')

def get_question_object(question):

    doc = nlp(question)
    doc = [token for token in doc if token.dep_ == 'nsubj'] 

    return doc[0].text


while True:

    context = input("Enter story: (press enter for default story) \n")

    if context.strip() == "":
        context = "Mary moved to the bathroom. Sandra took the apple. Mary went to the hallway. Mary got the milk. John moved to the bedroom. Mary dropped the milk. John took the milk. John moved to the kitchen. Sandra went to the bedroom."
    else:
        context = context.strip()

    print("Story: ", context)
    print()

    while True:
        question = input("Enter question: (eg. Where is the milk?) (Just enter to return to the story.)\n")

        if question.strip() == "":
            break

        # dict that tells which object are related to which person and where they are
        object = {}
        place = {}

        qst_obj = get_question_object(question)

        print("Object in question: ", qst_obj)
        print()

        doc = nlp(context)

        found = False
        for w in doc:
            if w.text == qst_obj: found = True
        
        if not found:
            print("Object not found in the story. Please try again.")
            print()
            continue

        for sent in doc.sents:
           
            for w in sent:

                if w.lemma_ == "drop" or w.lemma_ == "leave":
                    for w in sent:
                        if w.dep_ == 'nsubj':
                            subj = w.text

                        if w.dep_ == 'dobj':

                            currentPlace = place[subj]                 
                            object[w.text] = "NOBODY"
                            place["NOBODY"] = currentPlace
                        
                                
                
                if w.lemma_ == "go" or w.lemma_ == "travel" or w.lemma_ == "move":
                    for w in sent:
                        if w.dep_ == 'nsubj':
                            subj = w.text
                        if w.dep_ == 'pobj':
                            place[subj] = w.text

                if w.lemma_ == "take" or w.lemma_ == "get":
                    for w in sent:
                        if w.dep_ == 'nsubj':
                            subj = w.text

                        if w.dep_ == 'dobj':
                            obj = w.text
                            object[obj] = subj

        # if a person has an object, but no place, the object is "nowhere"
        for p in object:
            try:
                if place[object[qst_obj]] == None:
                    place[object[qst_obj]] = "NOWHERE"
            except:
                place[object[qst_obj]] = "NOWHERE"

        print(f"Answer: Object {qst_obj.upper()} is in the", place[object[qst_obj]].upper(), f"with person {object[qst_obj].upper()}")
    print()
