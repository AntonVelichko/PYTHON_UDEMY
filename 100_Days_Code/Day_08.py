
##########################################################################################################################
###  exercise Love Calculator  ###

# my first solution
def calculate_love_score(name1, name2):
    true_check = "true"
    love_check = "love"   
    
    true_score = 0
    love_score = 0
    
    for i in range(0, len(name1)):
        if name1[i].lower() in true_check:
            true_score += 1
        if name1[i].lower() in love_check:
            love_score += 1
            
    for i in range(0, len(name2)):
        if name2[i].lower() in true_check:
            true_score += 1
        if name2[i].lower() in love_check:
            love_score += 1   
            
    return str(true_score) + str(love_score)
print(calculate_love_score('Demetron', "Paraphen"))


---


# my updated solution
def calculate_love_score(name1, name2):
    
    combined_name = name1 + name2
    
    word_true = "true"
    word_love = "love"   
    
    true_score = 0
    love_score = 0
    
    for i in combined_name.lower():
        if i in word_true:
            true_score += 1
        if i in word_love:
            love_score += 1
            
    return str(true_score) + str(love_score)
    
print(calculate_love_score('Demetron', "Paraphen"))
