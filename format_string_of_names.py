# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except 
# for the last two names, which should be separated by an ampersand.

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

def namelist(names):
    length = len(names)
    res = ''
    for index, person in enumerate(names):
        if length == 1: return person['name']
      
        if index < length-1: 
        
            if index == 0:
                res+=person['name']
            else: res+=', %(name)s' % person
            
        else: res+=' & %(name)s' % person

    return res