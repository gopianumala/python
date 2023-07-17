n=int(input())
k=n//2
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1 or (i==k and j==k)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



'''

                                   0 1 2 3 4 5 6
                                 0 * * * * * * * 
                                 1 *           * 
                                 2 *           * 
                                 3 *      *    * 
                                 4 *           * 
                                 5 *           * 
                                 6 * * * * * * * 


    
sample input:
    7

 sample output:
    

* * * * * * * 
*           * 
*           * 
*     *     * 
*           * 
*           * 
* * * * * * * 

'''
