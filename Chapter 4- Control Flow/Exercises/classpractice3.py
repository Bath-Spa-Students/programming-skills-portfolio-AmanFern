print ("answer using Masters or Undergrad")
edu = (input("What is your level of education: "))
if (edu == "Masters" or "Master"):
    experience = float(input ("how many years of experience do you have? "))
    if (experience > 2):
        print ("You are hired")
    else:
        print ("You are not elegible")
else:
    print ("You are not legible")
