for a in ['x','y','z']:
    for b in ['x','y','z']:
        for c in ['x','y','z']:
            if (a!=b) and (b!=c) and (a!=c)and (a!='x') and (c!='x') and (c!='z'):
                
               print("a--%c b--%c  c--%c" %
                           (a,b,c))