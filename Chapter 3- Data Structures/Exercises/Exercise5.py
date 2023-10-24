#one of your guests cant make it, print the name of the guest and invite a new one. edit the list

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
