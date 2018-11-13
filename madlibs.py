 from random import randint

 def a():
    n1 = input("Enter how you feel about madlibs: ")
    n2 = input("Enter what you think about madlibs: ")
    n3 = input("Enter how madlibs make you feel: ")
    n4 = input("Enter a coding tool you use: ")
    n5 = input("Enter you major: ")
    n6 = input("Enter how it's been learning code: ")
    print(f"""
Madlibs are {n1}.
They are {n2} and make me feel {n3}.
I wish I could figure out how to use {n4}.
But as a {n5} major, it's been {n6}.
""")
    
 def b():
    a = input("Enter a color: ")
    b = input("Enter a plural noun: ")
    c = input("Enter something you love: ")
    d = input("Enter another thing you love: ")
    e = input("Enter a negative thing people say about u: ")
    f = input("Enter theme of what you love: ")
    print(f"""
Roses are {a},
{b} are blue,
I love {c},
And {d} too.
Some people say I'm {e},
but I think not, I just love {f}.
""")
    
 def c():
    a = input("Enter a name of someone: ")
    b = input("Enter a feeling: ")
    c = input("Enter verb: ")
    d = input("Enter a place: ")
    e = input("Enter feeling ending in -ed: ")
    f = input("Enter feeling ending in -ed: ")
    print(f"""
{a} is a monster. Little kids {b} him. Sometimes he even {c} the adults. His favorite place to go is {d}. There he feels {e} and {f}.
""")
    
 def d():
    a = input("Enter a name: ")
    b = input("Enter something you buy at a store: ")
    c = input("Enter something else you buy at a store: ")
    d = input("Enter another name: ")
    e = input("Enter verb ending in -ed: ")
    f = input("Enter a pet: ")
    print(f"""
{a} went to the store. He needed to buy {b} and {c}.There he ran into {d}. They {e} for hours, until the store closed. When he got home, his {f} was so mad at him, he had to leave again.
""")
    
 def e():
    a = input("Enter a location: ")
    b = input("Enter a noun: ")
    c = input("Enter a place: ")
    d = input("Enter a verb ending in -ing: ")
    e = input("Enter a verb: ")
    f = input("Enter a verb: ")
    print(f"""
My family went on a vacation to {a}. We were walking and a man grabbed my {b}. We went to the {c} and prayed. Eventually we saw the man again, he was {d}. We {e} at him and he {f}.
""")
    
 def f():
    a = input("Enter an animal: ")
    b = input("Enter a color: ")
    c = input("Enter a place: ")
    d = input("Enter a food: ")
    e = input("Enter a feeling: ")
    f = input("Enter a proper noun: ")
    print(f"""
Little Mary had a little {a}, who was as {b} as snow. Her little lamb followed her to {c} and ate all the {d}. Mary's parents were {e} and the little lamb was sent to {f}.
""")
    
 def g():
    a = input("Enter a Name: ")
    b = input("Enter a Name: ")
    c = input("Enter a substance: ")
    d = input("Enter a verb: ")
    e = input("Enter a verb ending in -ing: ")
    print(f"""
{a} and {b} went up the hill to fetch a pail of {c}. One {d} down and the other came {e} after.
""")
    
 def h():
    a = input("Enter a name: ")
    b = input("Enter a structure: ")
    c = input("Enter a verb in present tense: ")
    d = input("Enter a verb: ")
    e = input("Enter a place: ")
    f = input("Enter a name for a group of people: ")
    print(f"""
{a} sat on a {b}. He had a great {c}. Everyone came rushing to {d} him. Nobody could help, so they rushed him to the {e} to let the {f} help.
""")
    
 def i():
    a = input("Enter a weekday: ")
    b = input("Enter an animal: ")
    c = input("Enter a noun: ")
    d = input("Enter a noun: ")
    e = input("Enter a name : ")
    f = input("Enter a verb: ")
    print(f"""
It was a {a} night. Our new {b} was sitting on my lap. {c} and {d} shook the house. Our baby, {e}, got so scared, he {f} under the couch.
""")
    
 def j():
    a = input("Enter a noun: ")
    b = input("Enter a noun: ")
    c = input("Enter an animal: ")
    d = input("Enter an adjective: ")
    e = input("Enter a verb: ")
    f = input("Enter a noun: ")
    print(f"""
A {a} is considered to be man's best {b}. But what about {c}, man likes them too. I guess they are not as {d}, although some would disagree. It is true that they {e} more, but that comes with the {f}.
""")
    
test = int(input("> "))

 if test == 1:
        madlibs = [a(), b(), c(), d(), e(), f(), g(), h(), i(), j()]
        
 if test == 2:
    madlibs = [a, b, c, d, e, f, g, h, i, j]
    madlibs[randint(0, (len(madlibs)-2))]()
    