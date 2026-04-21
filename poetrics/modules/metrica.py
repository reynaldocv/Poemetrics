from silabeador import syllabify as silabear 
from silabeador import tonica as tonica 
from functools import lru_cache

@lru_cache
def palabra(word):
    _silabas = silabear(word)
    n = len(_silabas)
    
    ton = tonica(word)
    
    silabas = [[silaba, False, False] for silaba in _silabas]
    silabas[ton][1] = True
    
    stack = []
    
    for (silaba, ton, _) in silabas:
        last = ["", False, False]
        
        #sieneris
        #po-e-ta --> poe-ta
        if stack and (stack[-1][0][-1] in "aeo"):
            if (silaba in "aeo") or (silaba[0] in "hH" and silaba[: 2] not in ["Hí", "hí", "Hu", "Hú"]):
                ton = (ton == True) or (stack[-1][1] == True)
                
                last = stack.pop()
            
        stack.append([last[0] + silaba, ton, False])
        
    if len(stack) == 1:
        stack[0][1] = False
    
    if stack:
        stack[-1][2] = True
        
 
    
    return stack 

@lru_cache
def oracion(sentence):
    words = sentence.split(" ")
    stack = [palabra(word) for word in words if word != ""]
    
    if not stack: 
        return "<tr><td><br></td></tr>"
    
    newStack = []
    
    for elem in stack: 
        for (silaba, ton, _last) in elem:
            last = ["", False, False]
            _ton = ton
            
            if newStack and (newStack[-1][2] == True and newStack[-1][0][-1] in "yaeiou" and silaba not in ["ya", "YA", "Ya","hí","Hí"] and silaba[0] in "yaeiouAEIOUYHh"):
                last = newStack.pop()
                _ton = False
                _last = True
                
            newStack.append([last[0] + " " + silaba, _ton, _last])
                
    for (ith, (elem, ton, _)) in enumerate(newStack, 1):
        if ton == True:
            newStack[ith - 1] = "<td class='tonica'>" + elem + "</td>"
        else:
            newStack[ith - 1] = "<td class='atona'>" + elem + "</td>"
    
    tmp = "".join(newStack)
    
    ans = "<tr>" + tmp + "</tr>" 
    
    
    return ans 
    

def test():
    sentence = "Hola mundo"
    
    return sentence
