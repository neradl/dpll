from bool import *
from cnf import *



def dpll(formula):
    # v prvem delu formulo v CNF obliki pretvorimo v seznam slovarjev
    # (zunanji je And, notranji so Or stavki)
    formula=formula.cnf()
    string_formula=[]
    for s in formula.stavki:
        D={}
        if len(s.literali)==0:
            return 'Ni rešitve.'
        for l in s.literali:
            b=isinstance(l,Lit)
            if l.ime in D and D[l.ime]!=b:
                D={}
                break
            else:
                D[l.ime]=b
        if len(D)>0:
            string_formula.append(D)
    return dpll1(string_formula)


            
def dpll1(string_formula,znane_spr={}):
    s=True
    while s:
        s=False
        for i in string_formula[:]:
            if i=={}:
                return 'Ni rešitve.'

            
            if len(i)==1:
                # imamo samo en literal v stavku
                l,b=list(i.items())[0]
                if l in znane_spr and znane_spr[l]!=b:
                    return 'Ni rešitve.'
                else:
                    znane_spr[l]=b

                # zbrišemo literal not l ali stavek, v katerem nastopa literal l
                for k in string_formula[:]:
                    if l in k:
                        if k[l]==b:
                            string_formula.remove(k)                           
                        else:
                            del k[l]                           
                            # tu se pokličemo rekurzivno, če med brisanjem elementov iz seznama
                            # pridelamo seznam dolžine <=1
                            s=s or len(k)<=1   
    return [string_formula, znane_spr]




##def vstavljanje(string_formula,znane_spr={}):      
##    neznane_spr=[]
##    for i in string_formula:
##        for j in i:
##            if j not in znane_spr.keys() not in neznane_spr :
##                neznane_spr.append(j)
##    return neznane_spr        

    
##testne funkcije
f=And([Or([Atom('a')]),Or([Atom('b'),Atom('c'),Atom('a')]),Or([Atom('c'),Atom('d'),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Atom('a')])])
g=And([Or([Not(Atom('a'))]),Or([Atom('b'),Atom('c'),Atom('a')]),Or([Atom('c'),Atom('d'),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Not(Atom('a'))])])
h=And([Or([Atom('a')]),Or([Atom('b'),Atom('c'),Atom('d')]),Or([Atom('c'),Atom('a'),Atom('b')]),Or([Not(Atom('b'))])])
i=And([Or([Not(Atom('a'))]),Or([Atom('b'),Atom('c'),Atom('c')]),Or([Atom('c'),Atom('d'),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Not(Atom('a'))])])
j=And([Or([Atom('a'),Atom('b')]),Or([Atom('c'),Atom('d')]),Or([Not(Atom('a'))])])
test0=And([Or([Atom('a')]),Or([Not(Atom('a'))])])
test1=And([Or([Not(Atom('a')),Not(Atom('b')),Atom('c')]),Or([Not(Atom('a')),Atom('b')]),Or([Atom('a')])])
test2=And([Or([Atom('b'),Atom('c')]),Or([Atom('b'),Atom('c')]),Or([Atom('d'),Atom('e')])])
test3=And([Or([Atom('a'),Not(Atom('a')),Atom('b')])])

def test():
    print('f:  ', dpll(f))
    print('g:  ', dpll(g))
    print('h:  ', dpll(h))
    print('i:  ', dpll(i))
    print('j:  ', dpll(j))
    print('test0:  ', dpll(test0))
    print('test1:  ', dpll(test1))
    print('test2:  ', dpll(test2))
    print('test3:  ', dpll(test3))
