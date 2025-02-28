from config import db
from models import TypeBuilding

if __name__ == '__main__':
    import csv

    items = [
        'Небоскрёб', 'Антенная мачта', 'Бетонная башня', 'Радиомачта', 'Гиперболоидная башня', 'Дымовая труба', 'Решётчатая мачта',
        'Башня', 'Мост'
    ]
    for item in items:
        db.session.add(TypeBuilding(item))
    db.session.commit()

    # # Load Country data
    # with open('data/country.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     heading = next(reader)
    #     for row in reader:
    #         country = Country(*row)
    #         db.session.add(country)
    #     db.session.commit()

    # # Load Cities data
    # with open('data/city.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     heading = next(reader)
    #     for row in reader:
    #         country = City(*row)
    #         db.session.add(country)
    #     db.session.commit()
    #
    # # Load Buildings data
    # with open('data/building.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     heading = next(reader)
    #     for row in reader:
    #         country = Building(*row)
    #         db.session.add(country)
    #     db.session.commit()
