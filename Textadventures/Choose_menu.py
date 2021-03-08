def menu(question, answers):
    notDone = True
    print(question)
    answerlist = list(answers.keys())
    for i in range(len(answerlist)):
        print(i+1, ":", answerlist[i])
    while notDone:
        userinput = input()
        if userinput.isnumeric():
            userinput = int(userinput)-1
            if userinput in list(range(len(answerlist))):
                answers[answerlist[userinput]]()
                notDone = False
            else:
                print("Bitte eine passende Antwort")
        else:
            if userinput in answerlist:
                answers[userinput]()
            else:
                print("Bitte eine passende Antwort")

