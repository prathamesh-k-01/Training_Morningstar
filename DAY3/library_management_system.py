import datetime


class book():
    def __init__(self, title, author, publication_year, ISBN) -> None:
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.ISBN = ISBN

    
    def add_attribute(self, attribute_name, attribute_value):
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value
    
    def get_age(self):
        age = datetime.datetime.now().year - self.publication_year
        
        return age

book1 = book('To kill a mocking bird','Harper Lee', 1960, "978-0-06-112008-4")
book2 = book('1984', 'George Owell', 1949, '978-0-452-28423-4')

book1.add_attribute('genre', 'Fiction')
book1.add_attribute('availablity_status', 'Available')

book2.add_attribute('genre', 'Dystopian')
book2.add_attribute('availability_status', "Checked out")

age1 = book1.get_age()
print(book1.__dict__)
print(age1)
