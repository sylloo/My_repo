def inverser(texte):
    char = ''
    string =''
    for i in range(0,len(texte)):
        print (i)
        char = texte[((len(texte)-1)-i)]
        print (char)
        string += char
        
        
    return string
        
print (inverser("abcdefghijklmnopqrstuvwxyz"))