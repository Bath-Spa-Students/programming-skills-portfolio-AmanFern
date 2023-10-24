#You only have space for 2 guests, print a new message saying only people can be invited, use pop to remove excess guests. print a new message to the 2 that are still invited

#guest names
guest_list = ["Marcus Aurelius", "MJ", "Debbie Harry"]

#invitations
print (f"""Dear Mr. {guest_list[0]}, 
       I humbly request your presence at the dinner party
       that I will be hosting next Saturday.
       Kindly respond and let me know if you will be attending. \n""")
print (f"Heyy! How's it going {guest_list[1]}? I hope you're doing alright. \n Just wanted to let you know im having a party next weekend \n feel free to drop by :) \n")
print (f"Hello Miss {guest_list[2]}, \n I am hosting a dinner party next saturday and your presence would be greatly appreciated. \n Please RSVP :) Thank You! \n")

#guest unable to attend
print (f"Unfortunately {guest_list[1]} is unable to make it to the party, please invite someone else")

#deleting missing guest and adding new invitee
del(guest_list[2])
guest_list.insert(2, "Carrie Fisher")

#printing new invites
print (f"""Dear Mr. {guest_list[0]}, 
       I humbly request your presence at the dinner party
       that I will be hosting next Saturday.
       Kindly respond and let me know if you will be attending. \n""")
print (f"Heyy! How's it going {guest_list[1]}? I hope you're doing alright. \n Just wanted to let you know im having a party next weekend \n feel free to drop by :) \n")
print (f"Hello Miss {guest_list[2]}, \n I am hosting a dinner party next saturday and your presence would be greatly appreciated. \n Please RSVP :) Thank You! \n")

#change of plans and removing excess guest
print ("I am incredibly sorry for the last minute message, but unfortunately i will only be able to host two guests. \n I will send final invites to those that will come. \n")
uninvited = guest_list.pop()
print (f"{uninvited} has been removed from the guest list \n")

#sending final invites
print (f"Dear {guest_list[0]}, you are formally invited as a guest.\n")
print (f"Dear {guest_list[1]}, you are formally invited as a guest.\n")

#clearing guest list
del(guest_list[0])
del(guest_list[0])
print(guest_list)