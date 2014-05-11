# -*- encoding: utf-8 -*-

from bool import *
from cnf import *


def sudoku9(seznam):
    # seznam je seznam trojk (i,j,k) - na i,j - tem mestu je cifra k


    # znane predstavlja seznam znanih cifer
    znane=[]
    for i in seznam:
        znane.append(Atom((i)))

    r=[]
    # vsako polje ima vsaj eno cifro
    for i in range(1,10):
        for j in range(1,10):
            r2=[]
            for k in range(1,10):
                r2.append(Atom((i,j,k)))
            r.append(Or(r2))

            
    # nobeno polje nima več kot eno cifro
    for i in range(1,10):
        for j in range (1,10):
            for k in range(1,10):
                for l in range(1,k):
                    r.append(Or([Not(Atom((i,j,k))),Not(Atom((i,j,l)))]))

                    
    # v nobeni vrstici/stolpcu ni istih cifer
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,j):
                for l in range(1,10):
                    r.append(Or([Not(Atom((i,j,l))),Not(Atom((i,k,l)))]))
                    r.append(Or([Not(Atom((j,i,l))),Not(Atom((k,i,l)))]))


    # v nobenem 3x3 kvadratku ni istih cifer
    for x in range(0,3):
        for y in range(0,3):
            for i in range(1,4):
                for j in range(1,4):
                    for m in range(1,i+1):
                        if m<i:
                            for n in range(1,4):
                                for l in range(1,10):
                                    r.append(Or([Not(Atom((i+x*3,j+y*3,l))),Not(Atom((m+x*3,n+y*3,l)))]))
                        if m==i:                            
                            for n in range(1,j):
                                for l in range(1,10):
                                    r.append(Or([Not(Atom((i+x*3,j+y*3,l))),Not(Atom((m+x*3,n+y*3,l)))]))

                                  
    return And(znane+r)



def sudoku4(seznam):
    # seznam je seznam trojk (i,j,k) - na i,j - tem mestu je cifra k


    # znane predstavlja seznam znanih cifer
    znane=[]
    for i in seznam:
        znane.append(bool.Atom((i)))

    r=[]
    # vsako polje ima vsaj eno cifro
    for i in range(1,5):
        for j in range(1,5):
            r2=[]
            for k in range(1,5):
                r2.append(Atom((i,j,k)))
            r.append(Or(r2))

            
    # nobeno polje nima več kot eno cifro
    for i in range(1,5):
        for j in range (1,5):
            for k in range(1,5):
                for l in range(1,k):
                    r.append(Not(And([Atom((i,j,k)),Atom((i,j,l))])))

                    
    # v nobeni vrstici/stolpcu ni istih cifer
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,j):
                for l in range(1,5):
                    r.append(Or([Not(Atom((i,j,l))),Not(Atom((i,k,l)))]))
                    r.append(Or([Not(Atom((j,i,l))),Not(Atom((k,i,l)))]))


    # v nobenem 2x2 kvadratku ni istih cifer
    for x in range(0,2):
        for y in range(0,2):
            for l in range(1,5):
                r.append(Or([Not(Atom((1+x*2,1+y*2,l))),Not(Atom((1+x*2,2+y*2,l)))]))
                r.append(Or([Not(Atom((1+x*1,1+y*2,l))),Not(Atom((2+x*2,1+y*2,l)))]))
                r.append(Or([Not(Atom((1+x*2,1+y*2,l))),Not(Atom((2+x*2,2+y*2,l)))]))
                r.append(Or([Not(Atom((1+x*2,2+y*2,l))),Not(Atom((2+x*2,1+y*2,l)))]))
                r.append(Or([Not(Atom((1+x*2,2+y*2,l))),Not(Atom((2+x*2,2+y*2,l)))]))
                r.append(Or([Not(Atom((2+x*2,1+y*2,l))),Not(Atom((2+x*2,2+y*2,l)))]))

                                                          
    return And(znane+r)
