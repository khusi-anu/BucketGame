def display(p):
    L=[]
    s=""
    for i in range (0,9):
        if(i>=(9-p)):
            L.append("|---------|")
            
            #print" ".join(map(str,L[i]))
        else:
            L.append('|         |')
        #s+=" ".join(map(str,L[i]))
    L.append("-----------")
    #s+=" ".join(map(str,L[9]))
    return L
def bucket(n):
    print ">>>>Enter 1 to fill the bucket A \nEnter 2 to fill the bucket B \nEnter 3 to fill the bucket C <<<<"
    tap=input()
    #C=raw_input()
    #p,q,r=8,0,0
    if(tap==1):
        p,q,r=8,0,0
    elif(tap==2):
        p,q,r=0,5,0
    elif(tap==3):
        p,q,r=0,0,3
    else:
        print "First fill  the Bucket to play!!!!" 
    print "A = ",p,"B = ",q,"C = ",r
    while(n>0 and (tap==1 or tap==2 or tap==3)):
        a,b=(raw_input().split())
        if(a=='A' and b=='B' and p<>0 and q<>5):
            e=5-q
            p,q=p-e,q+e
            sa=display(p)
            sb=display(q)
            sc=display(r)
            for i in range(len(sa)):
                print sa[i]+'     '+ sb[i]+'     '+ sc[i]
            print "    ",p,"            ",q,"             ",r
        elif(a=='A' and b=='C' and p<>0 and r<>3):
            d=3-r
            p,r=p-d,r+d
            sa=display(p)
            sb=display(q)
            sc=display(r)
            for i in range(len(sa)):
                print sa[i]+'     '+ sb[i]+'     '+ sc[i]
            print "    ",p,"            ",q,"             ",r
        elif(a=='B' and b=='C' and q<>0 and r<>3):
            c=3-r
            if(c<q):
                 q,r=q-c,r+c
            else:
                q,r=0,r+q
            sa=display(p)
            sb=display(q)
            sc=display(r)
            for i in range(len(sa)):
                print sa[i]+'     '+ sb[i]+'     '+ sc[i]
            print "    ",p,"            ",q,"             ",r
        elif(a=='B' and b=='A' and q<>0):
            p=p+q
            q=0
            sa=display(p)
            sb=display(q)
            sc=display(r)
            for i in range(len(sa)):
                print sa[i]+'     '+ sb[i]+'     '+ sc[i]
            print "    ",p,"            ",q,"             ",r
        elif(a=='C' and b=='A' and r<>0):
            p=p+r
            r=0
            sa=display(p)
            sb=display(q)
            sc=display(r)
            for i in range(len(sa)):
                print sa[i]+'     '+ sb[i]+'     '+ sc[i]
            print "    ",p,"            ",q,"             ",r
        elif(a=='C' and b=='B' and r<>0 and q<>5):
            g=5-q
            if(g<r):
                r,q=r-g,q+g
            else:
                q,r=q+r,0
            sa=display(p)
            sb=display(q)
            sc=display(r)
            for i in range(len(sa)):
                print sa[i]+'     '+ sb[i]+'     '+ sc[i]
            print "    ",p,"            ",q,"             ",r
        else:
            print "Wrong Move!!!"
        n=n-1
    if(p==4 and q==4):
        if(n==7):
            return 1
        else:
            return 2
    else:
        return 0

ch='Y'
while(ch<>'N'):
    print "-------------------------------------------------------------------------------------------------------------"
    print "Rules: You are allowed to enter either 'A' or 'B' or 'C' \nJust enter your moves : From which the bucket is emptied to the bucket getting filled.."
    print "Let's start the game..."
    print "-------------------------------------------------------------------------------------------------------------"
    print "A B C are buckets of 8ltr 5ltr and 3ltr \nMake 4ltrs in any one bucket"
    buck=bucket(14)
    if(buck==1):
        print "You Won in minimum steps   Congo!!!!!!!"
    elif(buck==2):
        print "You won ....but try to do in minimum steps....better luck next time!!!"
    else:
        print "You lose !!!!!!!"
    print "Do You wish to play another game? Press Y or N only"
    ch=raw_input()
    
