e=2.718281828459045
pi=3.141592653589793

def app(xn,n):
    for i in range(n):
        xn.append(0)
    return xn

def twiddle(P,N):
    x=e**((-1j*2*pi*P)/(N))
    return x

def mat_mul(x,y):
    temp1=[]
    for i in range(len(y)):
        temp=0
        for j in range(len(y)):
              temp += x[i][j]*y[j]
        temp1.append(round(temp.real,3)+round(temp.imag,3)*1j)
    return temp1

def Wmat(N_point):
    x=[]
    for i in range(N_point):
        temp=[]
        for j in range(N_point):
            temp.append(twiddle(i*j,N_point))
        x.append(temp) 
    return x

n = int(input("ENTER N POINT >>> "))
print("Enter x(n) >>> ",end="")
xn = list(map(int,input().split()))
if(len(xn)<n):
    xn=app(xn,n-len(xn))
t = Wmat(n)
tt = mat_mul(t,xn)
print("X(k) = { ",end="")
for i in tt:
    print(str(i)[1:-1],"",sep=",",end=" ")
print("}")
