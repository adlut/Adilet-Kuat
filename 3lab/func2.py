# Dictionary of movies
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Write a function that takes a single movie and returns True if its IMDB score is above 5.5
'''
def func1(movie,rating):
    for i in movies:
        if i["name"]==movie:
            return True if i["imdb"]>rating else False

print(func1("Ringing Crime",5.5))
'''
#Write a function that returns a sublist of movies with an IMDB score above 5.5.
'''
def func2(rating):
    l = []
    for i in movies:
        if i["imdb"]>rating:
            l.append(i["name"])
    return l

print(func2(5.5))
'''
#Write a function that takes a category name and returns just those movies under that category.
'''
def func3(genre):
    l = []
    for i in movies:
        if i["category"]==genre:
            l.append(i["name"])
    return l

print(func3("Romance"))
'''
#Write a function that takes a list of movies and computes the average IMDB score.
'''
l2 = ["Usual Suspects","Detective","Joking muck","Colonia"]
def func4(l2):
    avr = 0
    for i in movies:
        if i["name"] in l2:
            avr+=i["imdb"]
    return avr/len(l2)

print(func4(l2))
'''
#Write a function that takes a category and computes the average IMDB score.
'''
def func5(genre):
    avg,num=0,0
    for i in movies:
        if i["category"]==genre:
            avg+=i["imdb"]
            num+=1
    return avg/num

print(func5("Crime"))
'''








