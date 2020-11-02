import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, State, Iso, Region, Category


def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Category.objects.all().delete()

    for row in reader:
        print(row)

        r, created = Region.objects.get_or_create(name=row[9])
        c, created = Category.objects.get_or_create(name=row[7])
        i, created = Iso.objects.get_or_create(name=row[10])


        try:
            y = int(row[3])
        except:
            y = None

        try:
            la = float(row[4])
        except:
            la = None

        try:
            lo = float(row[5])
        except:
            lo = None

        try:
            a = float(row[6])
        except:
            a = None

        #try:
        #    j=row[2]
        #except:
        #    j=None

        st, created = State.objects.get_or_create(name=row[8], region=r)
        #st = State.objects.create(state=row[8], region=r)
        si, created = Site.objects.get_or_create(name=row[0], year=y, latitude=la, longitude=lo, area_hectares=a, description=row[1], justification=row[2], category=c, state=st, iso=i)
