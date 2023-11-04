#use a dictionary to store five programming terms and their meanings as values.
#use a loop to print and then add 5 more


#making glossary
programming_terms = {'Integer' : 'is a data type with only whole numbers. \n',
                     'Float' : 'is a data type with whole numbers and decimal numbers. \n',
                     'Boolean' : 'means true or false. \n',
                     'List' : 'is a container that can store any type of value. \n',
                     'Tuple' : 'is similar to a list, but you cannot update the values within it. \n',
                     'String' :'is a data type which contains characters like letters and numbers. \n',
                     'Repository' : 'is where all the files for a project are stored. \n',
                     'Commit' : 'is to merge the changes you made in your copy with the one in the repository. \n',
                     'Push' : 'is to move files from one repository to another. \n',
                     'Revison' : 'is any change to the file. \n'}

#running print loop
for key in programming_terms.keys():
    print(key.title(), programming_terms[key])
