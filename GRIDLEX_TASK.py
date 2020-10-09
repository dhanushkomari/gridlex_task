print('PYTHON CODE WHICH TAKES AN ALPHANUMERIC Str AS AN ARGUMENT AND PRINT THE STRING AS AN ART WHICH IS A COMBINATION OF # CHARECTERS.')


def PRINTING_PATTERN():
    for i in range(len(Str)):
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

            

        ##############################
        #### PRINTING NUMBERS ########
        ##############################
            

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
Str=Str.upper()
List=[]
Result=PRINTING_PATTERN()

print() #for one line space on top

for i in range(6):
    for j in range(len(Result)):
        for k in range(6):
            print(Result[j][i][k],end=" ")
    print()
    
print() #for one line space bottom




                    

                    
