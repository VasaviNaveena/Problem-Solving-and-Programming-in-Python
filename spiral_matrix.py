def spiral_matrix(m,n,a):  #m,n are max row and column
#row,col are running row&columns
   s,row,col=0,0,0  #s is taken as numbers starting from 1
   while row<m and col<n:
      for i in range (col,n):
         s+=1    #before first print s gets 1
         a[row][i]=s
      row+=1
      for i in range(row,m):
         s+=1
         a[i][n-1]=s
      n-=1
      if row<m:
         for i in range(n-1,col-1,-1):
            s+=1
            a[m-1][i]=s
         m-=1
      if col<n:
         for i in range(m-1,row-1,-1):
            s+=1
            a[i][col]=s
         col+=1
   return 0
n=input('Enter size of matrix:') #size
# check the size
try :
   n=int(n)
   flag=1
except :
   print("Give integer as input")
   flag=0
   
# print the matrix   
if(flag==1):
 print("======SPIRAL MATRIX======")
 a=[[0]*n for i in range(n)]
 spiral_matrix(n,n,a)   
 for i in range(n):
   for j in range (n):
      if(a[i][j]%10==a[i][j]):
        print(a[i][j],end="  ")
      else:
        print(a[i][j],end=" ")
   print("")

