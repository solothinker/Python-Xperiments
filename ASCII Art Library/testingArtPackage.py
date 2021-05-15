#pip install art
import art

temp = 32
def printArt(item="coffee",number=1):
    art1 = art.art(item,number=number)
    print(" "*(temp-len(item)),item,"|",art1)
    

artString = "All one line Art"
print(" "*(temp-int(0.5*len(artString))+1),artString)
for name in art.ART_NAMES:
    printArt(name)
print("-------------------------------------------------"*2)    
for font in art.FONT_NAMES:
    txt = art.text2art("Solothinker",font)
    print(txt)
