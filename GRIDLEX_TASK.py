print('PYTHON CODE WHICH TAKES AN ALPHANUMERIC STRING AS AN ARGUMENT AND PRINT THE STRING AS AN ART WHICH IS A COMBINATION OF # CHARECTERS.')


def PRINTING_PATTERN():
    for i in range(len(Str)):

        ###################################
        ###### UPPER CASE LETTERS##########
        ###################################

        
        ######   PRINTING 'A'  #######
        if Str[i]=="A":
            A = [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if ((col==0 or col==5) and row!=0) or ((col>0 and col<5)and(row==0))or row==3:
                        A[row][col] = "#"
            List.append(A)

        ######   PRINTING 'B'  #######
        elif Str[i]=="B":
            B = [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or ((row==0 or row==2 or row==5)and col!=5) or (col==5 and (row!=0 and row!=2 and row!=5)):
                        B[row][col] = "#"
            List.append(B)

        ######   PRINTING 'C'  #######
        elif Str[i]=="C":
            C= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==0 and row>0 and row<5) or (row==0 and col>0 and col!=5) or (row==5 and col>0 and col!=5):
                        C[row][col] = "#"
            List.append(C)

        ######   PRINTING 'D'  #######
        elif Str[i]=="D":
            D= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col == 0) or (col==5 and (row!=0 and row!=5)) or ((row==0 or row==5) and (col>0 and col<5)):
                        D[row][col]="#"
            List.append(D)
            
        ######   PRINTING 'E'  #######          
        elif Str[i]=="E":
            E= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or ((row==0 or row==2 or row==5)and col!=5):
                        E[row][col]="#"
            List.append(E)

        ######   PRINTING 'F'  #######
        elif Str[i]=="F":
            F= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or ((row==0 or row==2) and col!=5): 
                        F[row][col]="#"
            List.append(F)
            
        ######   PRINTING 'G'  #######
        elif Str[i]=="G":
            G= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==0 and row>0 and row<5) or (col==4 and (row!=1 and row!=2)) or (row==0 or row==5) and (col>0 and col<4) or (row==3 and col==3):
                        G[row][col]="#"
            List.append(G)
            
        ######   PRINTING 'H'  #######
        elif Str[i]=="H":
            H= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or col==5 or row==3:
                        H[row][col]="#"
            List.append(H)
            
        ######   PRINTING 'I'  #######                
        elif Str[i]=="I":
            I= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if ((row==0 or row==5) and col!=5) or col==2:
                        I[row][col]="#"
            List.append(I)

        ######   PRINTING 'J'  #######
        elif Str[i]=="J":                  
            J= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                     if (col==3) or (row==5 and col!=5 and col!=4) or (row==0):
                        J[row][col]="#"
            List.append(J)

        ######   PRINTING 'K'  #######
        elif Str[i]=='K':
            K =[[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==1) or (col==2 and (row==2 or row==3)) or (col==3 and(row==1 or row==4)) or (col==4 and(row==0 or row==5)) :
                        K[row][col]="#"
            List.append(K)
            
        # for letter L               
        elif Str[i]=="L":
            L= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or (row==5 and col!=5):
                        L[row][col]="#"
            List.append(L)
            
        ######   PRINTING 'M'  #######                
        elif Str[i]=="M":
            M= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or col==4 or (row==1 and col==1) or (row==2 and col==2) or (row==1 and col==3) :
                        M[row][col]="#"
            List.append(M)

        ######   PRINTING 'N'  #######
        elif Str[i]=="N":
            N= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or col==5 or row==col:
                        N[row][col]="#"
            List.append(N)
            
        ######   PRINTING '0'  #######                
        elif Str[i]=="O":
            O= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if ((row==0 or row==5) and (col!=0 and col!=5)) or ((col==0 or col==5) and (row!=0 and row!=5)):
                        O[row][col]="#"
            List.append(O)
            
        ######   PRINTING 'P'  #######
        elif Str[i]=="P":
            P= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or (row==0 and col!=5) or (row==2 and col!=5) or (row==1 and col==5):
                        P[row][col]="#"
            List.append(P)
            
        ######   PRINTING 'Q'  #######
        elif Str[i]=="Q":
            Q= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if ((row==0 or row==4) and (col!=0 and col!=5)) or ((col==0 or col==5) and (row!=0 and row!=4 and row!=5))or (row==3 and col==2) or (row==5 and col==4):
                        Q[row][col]="#"
            List.append(Q)

        ######   PRINTING 'R'  #######
        elif Str[i]=="R":
            R= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or (row==0 and col!=5) or (row==2 and col!=5) or (row==1 and col==5)or (row==3 and col==2) or (row==4 and col==3) or (row==5 and col==4):
                        R[row][col]="#"
            List.append(R)

        ######   PRINTING 'S'  #######
        elif Str[i]=="S":
            S= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row==0 and col!=0) or (row==2 and (col!=0 and col!=5)) or (row==5 and col!=5) or ((row==1 or row==5) and col==0) or ((row==3 or row==4) and col==5):
                        S[row][col]="#"
            List.append(S)
            
        ######   PRINTING 'T'  #######    
        elif Str[i]=="T":
            T= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row==0 and col!=5) or col==2:
                        T[row][col]="#"
            List.append(T)
            
        ######   PRINTING 'U'  #######
        elif Str[i]=="U":
            U= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if ((col==0 or col==5) and row!=5) or (row==5 and (col!=0 and col!=5)):
                        U[row][col]="#"
            List.append(U)

        ######   PRINTING 'V'  #######
        elif Str[i]=="V":
            V= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==0 and row<4) or (col==4 and row<4) or (col==1 and (row==4)) or (col==3 and (row==4)) or (row==5 and col==2):
                        V[row][col]="#"
            List.append(V)

        ######   PRINTING 'W'  #######
        elif Str[i]=="W":
            W= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or col==4 or (row==4 and col==3) or (row==3 and col==2) or (row==4 and col==1):
                        W[row][col]="#"
            List.append(W)
            
        ######   PRINTING 'X'  #######    
        elif Str[i]=="X":
            X= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if row==col or (row==5 and col==0) or (row==4 and col==1) or (row==3 and col==2) or (row==2 and col==3) or (row==1 and col==4) or (row==0 and col==5):
                        X[row][col]="#"
            List.append(X)
            
        ######   PRINTING 'Y'  #######   
        elif Str[i]=="Y":
            Y= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row==0 and col==0) or (row==1 and col==1) or (row==2 and col==2) or (row==1 and col==3) or (row==0 and col==4) or ((row==3 or row==4 or row==5)and col==2):
                        Y[row][col]="#"
            List.append(Y)

        ######   PRINTING 'Z'  #######
        elif Str[i]=="Z":
            Z= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if row==0 or row==5 or (row==4 and col==1) or (row==3 and col==2) or (row==2 and col==3) or (row==1 and col==4):
                        Z[row][col]="#"
            List.append(Z)

        ###################################
        #######  LOWER CASE LETTERS  ######
        ###################################

        ######   PRINTING 'a'  #######
        elif Str[i]=="a":
            a= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==0 and (row==1 or row==4)) or (col==4 and (row!=0)) or (row==0 and (col>0 and col<4)) or (row==3 and (col>0 and col<4)) or (row==5 and (col>0 and col<4)):
                        a[row][col]="#"
            List.append(a)


        ######   PRINTING 'b'  #######            
        elif Str[i]=="b":
            b= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or (row==2 and col!=4 and col!=5) or (row==5 and col!=4 and col!=5) or (row==4 and col==4) or (row==3 and col==4):
                        b[row][col]="#"
            List.append(b)

        ######   PRINTING 'c'  #######
        elif Str[i]=="c":
            c= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row==0 and col!=0 and col!=5) or (row==5 and col!=0 and col!=5) or (col==0 and row!=0 and row!=5):
                        c[row][col]="#"
            List.append(c)

        ######   PRINTING 'd'  #######
        elif Str[i]=="d":
            d= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==5 or (row==2 and col!=0) or (row==5 and col!=0) or (col==0 and (row==3 or row==4)):
                        d[row][col]="#"
            List.append(d)

        ######   PRINTING 'e'  #######
        elif Str[i]=="e":
            e= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==0 and row!=0 and row!=5) or (row==0 and col!=0 and col!=5) or (row==2 and col!=5) or (row==5 and col!=0 and col!=5) or (row==1 and col==5):
                        e[row][col]="#"
            List.append(e)

        ######   PRINTING 'f'  #######
        elif Str[i]=="f":
            f= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==1 and row>0) or (row==0 and col>1) or (row==2 and col>1):
                        f[row][col]="#"
            List.append(f)

        ######   PRINTING 'g'  #######
        elif Str[i]=="g":
            g= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row==0 and col!=0) or (row==2 and col!=0) or (row==5 and col!=0 and col!=5) or (col==5 and row!=0 and row!=5) or (row==1 and col==0):
                        g[row][col]="#"
            List.append(g)

        ######   PRINTING 'h'  #######
        elif Str[i]=="h":
            h= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==0) or (row==2 and col!=5) or (col==5 and row>2):
                        h[row][col]="#"
            List.append(h)        

        ######   PRINTING 'i'  #######
        elif Str[i]=="i":
            i= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==2 and row>1) or (col==2 and row==0):
                        i[row][col]="#"
            List.append(i)  

        ######   PRINTING 'j'  #######            
        elif Str[i]=="j":
            j= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==3 and row>1) or (row==5 and col<4) or (row==0 and col==3):
                        j[row][col]="#"
            List.append(j)  

        ######   PRINTING 'k'  #######
        elif Str[i]=="k":
            k= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==1) or (row==2 and col==3) or (row==3 and col==1) or (row==4 and col==2) or (row==5 and col==3) or (row==3 and col==2):
                        k[row][col]="#"
            List.append(k)  

        ######   PRINTING 'l'  #######
        elif Str[i]=="l":
            l= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==2 and row<5) or (row==5 and col==3) or (row==5 and col==4):
                        l[row][col]="#"
            List.append(l)  

        ######   PRINTING 'm'  #######
        elif Str[i]=="m":
            m= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==0) or (row==1 and (col==1 or col==3)) or (row==0 and (col==2 or col==4)) or (col==3 and row>0)or (col==5 and row>0):
                        m[row][col]="#"
            List.append(m)

        ######   PRINTING 'n'  #######
        elif Str[i]=="n":
            n= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or (col==5 and row!=0) or (row==0 and (col>2 and col<5)) or (row==2 and col==1) or (row==1 and col==2):
                        n[row][col]="#"
            List.append(n)

        ######   PRINTING 'o'  #######            
        elif Str[i]=="o":
            o= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if ((row==0 or row==5) and (col!=0 and col!=5)) or ((col==0 or col==5) and (row!=0 and row!=5)):
                        o[row][col]="#"
            List.append(o)

        ######   PRINTING 'p'  #######
        elif Str[i]=="p":
            p= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==0 or (row==0 and col!=5 and col!=4) or (row==2 and col!=5 and col!=4) or (row==1 and col==4):
                        p[row][col]="#"
            List.append(p)

        ######   PRINTING 'q'  #######           
        elif Str[i]=="q":
            q= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==0 and (row==1 or row==2)) or (col==1 and (row==0 or row==3)) or (col==2 and (row==0 or row==3)) or (col==3 and row>0) or (col==4 and row==4):
                        q[row][col]="#"
            List.append(q)

        ######   PRINTING 'r'  #######
        elif Str[i]=="r":
            r= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==2) or (col==3 and row==1) or(col==4 and row==0) :
                        r[row][col]="#"
            List.append(r)

        ######   PRINTING 's'  #######
        elif Str[i]=="s":
            s= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row==0 and col>1) or (row==3 and (col>1 and col<5)) or (row==5 and (col>0 and col<5)) or (col==1 and (row==1 or row==2)) or (row==4 and col==5):
                        s[row][col]="#"
            List.append(s)

        ######   PRINTING 't'  #######
        elif Str[i]=="t":
            t= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==1 and row!=5) or (row==5 and (col>1 and col<5)) or (row==2 and col!=5):
                        t[row][col]="#"
            List.append(t)

        ######   PRINTING 'u'  #######
        elif Str[i]=="u":
            u= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==1 and row!=5) or (col==4 and row!=5) or (row==5 and (col==2 or col==3)):
                        u[row][col]="#"
            List.append(u)

        ######   PRINTING 'v'  #######            
        elif Str[i]=="v":
            v= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==0 and row<4) or (col==4 and row<4) or (col==1 and (row==4)) or (col==3 and (row==4)) or (row==5 and col==2):
                        v[row][col]="#"
            List.append(v)

        ######   PRINTING 'w'  #######            
        elif Str[i]=="w":
            w= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (col==0 and row!=5)or (col==2 and row!=5) or (col==4 and row!=5) or (col==1 and row==5) or (col==3 and row==5):
                        w[row][col]="#"
            List.append(w)

        ######   PRINTING 'x'  #######
        elif Str[i]=="x":
            x= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if row==col or (row==5 and col==0) or (row==4 and col==1) or (row==3 and col==2) or (row==2 and col==3) or (row==1 and col==4) or (row==0 and col==5):
                        x[row][col]="#"
            List.append(x)

        ######   PRINTING 'y'  #######            
        elif Str[i]=="y":
            y= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row+col==5) or (row==0 and col==1) or (row==1 and col==2):
                        y[row][col]="#"
            List.append(y)

        ######   PRINTING 'z'  #######        
        elif Str[i]=="z":
            z= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row+col==5) or row==0 or row==5 or (row==3 and col==1) or (row==3 and col==3):
                        z[row][col]="#"
            List.append(z)

            

        ##################################
        ########    NUMBERS   ############
        ##################################
            

        ######   PRINTING '1'  #######
        elif Str[i]=="1":
            num1= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if col==3 or row==5 or (row==1 and col==2) or (row==2 and col==1):
                        num1[row][col]="#"
            List.append(num1)

        ######   PRINTING '2'  #######
        elif Str[i]=="2":
            num2= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if ((col==0 and (row==1 or row>3)) or (col==5 and (row!=0 and row<4))) or (row==0 and (col!=0 and col!=5)) or (row==3 and (col!=0 and col!=5)) or row==5:
                        num2[row][col]="#"
            List.append(num2)

        ######   PRINTING '3'  #######
        elif Str[i]=="3":
            num3= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row==0 and col!=5 and col!=0) or (row==3 and col!=5 and col!=0) or (row==5 and col!=5 and col!=0) or (col==5 and (row==1 or row==2 or row==4)):
                        num3[row][col]="#"
            List.append(num3)

        ######   PRINTING '4'  #######
        elif Str[i]=="4":
            num4= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row==4) or col==3  or (row==1 and col==2) or (row==2 and col==1) or (row==3 and col==0):
                        num4[row][col]="#"
            List.append(num4)

        ######   PRINTING '5'  #######
        elif Str[i]=="5":
            num5= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row==0) or (row==1 and col==0) or (row==2 and col!=5) or (row==3 and col==5) or (row==4 and col==5) or (row==5 and col!=5):
                        num5[row][col]="#"
            List.append(num5)

        ######   PRINTING '6'  #######
        elif Str[i]=="6":            
            num6= [[" " for i in range(6)] for j in range(7)]
            for row in range(6):
                for col in range(6):
                    if (row==0 and col!=0) or (row==3 and col!=5) or (row==5 and col!=0 and col!=5) or (col==0 and row!=0 and row!=5) or (col==5 and row==4):
                        num6[row][col]="#"
            List.append(num6)

        ######   PRINTING '7'  #######            
        elif Str[i]=="7":
            num7= [[" " for i in range(6)] for j in range(7)]
            i=1
            j=5
            for row in range(6):
                for col in range(6):
                    if row==0:
                        num7[row][col]="#"
                    else:
                        pass
                    if row==i and col==j:
                        num7[row][col]="#"
                        i=i+1
                        j=j-1
                    else:
                        pass
            List.append(num7)

        ######   PRINTING '8'  #######
        elif Str[i]=="8":
            num8= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row==0 and col!=0 and col!=5) or (row==2 and col!=0 and col!=5) or (row==5 and col!=0 and col!=5) or (col==0 and row!=0 and row!=2 and row!=5) or (col==5 and row!=0 and row!=2 and row!=5):
                        num8[row][col]="#"
            List.append(num8)

        ######   PRINTING '9'  #######
        elif Str[i]=="9":
            num9= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if (row==0 and col!=0 and col!=5) or (row==5 and col!=0 and col!=5) or (row==2 and col!=0) or (row==1 and col==0) or (row==1 and col==5) or (col==5 and row==3) or (col==5 and row==4):
                        num9[row][col]="#"
            List.append(num9)
        

        ######   PRINTING '0'  #######
        elif Str[i]=="0":
            num0= [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if ((col==0 or col==5) and (row !=0 and row!=5)) or ((row==0 or row==5) and (col>0 and col<5)):
                        num0[row][col]="#"
            List.append(num0)

        ###### PRINTING 'SPACE' ####### 
        elif Str[i]==" ":
            space= [[" " for i in range(6)] for j in range(6)]
            for row in range(1):
                for col in range(1):                    
                    space[row][col]=" "
            List.append(space)

        else:
            print("INVALID FORMAT OF INPUT Str")
            
    return(List) 


####### PASSING Str ########
Str=input("ENTER INPUT STRING:")
#Str=Str.upper()
List=[]
Result=PRINTING_PATTERN()

print() #for one line space on top

for i in range(6):
    for j in range(len(Result)):
        for k in range(6):
            print(Result[j][i][k],end=" ")
    print()
    
print() #for one line space bottom




                    

                    
