something = ""
inputList = []
done = False
while not done:
    something = input("Say something: ")
    
    if something == "\end":
        done = True
    else:
        processedSomething = something.lower()

        if "who" in processedSomething or "what" in processedSomething or "where" in processedSomething:
            processedSomething += "? "
        elif "when" in processedSomething or "why" in processedSomething or "how" in processedSomething:
            processedSomething += "? "
        else: processedSomething += ". "

        processedSomething = processedSomething.capitalize()
        inputList.append(processedSomething)

message = ""
for something in inputList:
    message += something

print(message)