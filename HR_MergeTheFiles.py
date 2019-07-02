def merge_the_tools(string, k):
    # your code goes here
    
   
    
     dividing = ([string[i:i + k] for i in range(0, len(string), k)])
     for i in range(0,len(dividing)):
        a = [i for i in dividing[i]]
        b = []
        for x in a:

            if x not in b:
                b.append(x)
        print ("".join(b))
