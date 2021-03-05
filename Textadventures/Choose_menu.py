def menu (question, answers):
    notDone = True
    while notDone:
        useriput = (input(question)).lower()
        if useriput in answers:
            answers[useriput]()
            notDone = False
        else:
            print("Bitte gib passende Antwort")
