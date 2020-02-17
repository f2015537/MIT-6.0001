class divyam(object):
    def __init__(self, mom, dad):
        self.mom = mom
        self.dad = dad
    def __str__(self):
        return("hi")

print(divyam("Ashok","Neeta"))
d = divyam("Ashok","Neeta")
print(d+d)