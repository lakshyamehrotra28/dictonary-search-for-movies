bollywood_movies={}

n=int(input("enter the number of movie details you want to enter: "))

for i in range(n):

    name=input("enter the name of the movie: ",)

    movie_details={}

    l1=input("enter the cast name: ")
    l1=list(l1.split())
    movie_details['cast']=l1

    l2=input("enter the DIRECTOR name: ")
    l2=list(l2.split())
    movie_details['director']=l2

    l3=input("enter the cast PRODUCER name: ")
    l3=list(l3.split())
    movie_details['PRODUCER']=l3

    l4=input("enter the GENRE name: ")
    movie_details['GENRE']=l4

    bollywood_movies[name]=movie_details

print()
print()
print()
for i in ((bollywood_movies)):
    print(i,':',bollywood_movies[i],end='''

''')
g=input("enter the genre: " )
for i in  bollywood_movies.keys():
    a1=bollywood_movies.get(i)
    a2=a1.get('GENRE')
    if a2==g:
        print(i)

