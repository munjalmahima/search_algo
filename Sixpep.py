ans='y'
while(ans=='y'or ans=='Y'):
    lists=['iphone','iphone 11','iphone 6','laptop','dell laptop','buckets','clothes','refrigerator','lg refrigerator','crunchzase','zase','crunch']
    substring=input('Enter a string:- ')
    substring=substring.lower()
    m=[]
    k=[]
    strings_with_substring=[string for string in lists if substring in string]
    if strings_with_substring:
        print("OUTPUT:- ",sorted(strings_with_substring,key=len))
    if not strings_with_substring:
        set_string2=set(substring)
        for l in lists:
            set_string1=set(l)
            matched=set_string1 & set_string2
            c=len(matched)
            m.append(c)
        indices=[i for i,x in enumerate(m) if x==max(m)]
        for i in indices:
            k.append(lists[i])
        print("OUTPUT:- ",k)
    ans=input('Do you want to continue ?(y/n)')
    
            
