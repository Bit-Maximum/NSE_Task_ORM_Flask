import csv

from config import db


class Category(db.Model):
    __tablename__ = "category"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    products = db.relationship("Product", cascade="all, delete")

    def __init__(self, category_id, name):
        self.id = category_id
        self.name = name


class City(db.Model):
    __tablename__ = "city"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    zipcode = db.Column(db.Numeric(5, 0), nullable=False)

    customers = db.relationship("Customer", cascade="all, delete")
    employees = db.relationship("Employee", cascade="all, delete")

    def __init__(self, city_id, name, zipcode):
        self.id = city_id
        self.name = name
        self.zipcode = zipcode


class Customer(db.Model):
    __tablename__ = "customer"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    middle_initial = db.Column(db.String(1), nullable=True)
    last_name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(90), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"), nullable=False)

    city = db.relationship("City", back_populates="customers")

    sales = db.relationship("Sale", cascade="all, delete")

    def __init__(
        self, customer_id, first_name, middle_initial, last_name, address, city_id
    ):
        self.id = customer_id
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.address = address
        self.city_id = city_id


class Employee(db.Model):
    __tablename__ = "employee"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    middle_initial = db.Column(db.String(1), nullable=True)
    last_name = db.Column(db.String(45), nullable=False)
    gender = db.Column(db.String(10))
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"), nullable=False)

    city = db.relationship("City", back_populates="employees")

    sales = db.relationship("Sale", cascade="all, delete")

    def __init__(
        self,
        employee_id,
        first_name,
        middle_initial,
        last_name,
        gender,
        city_id,
    ):
        self.id = employee_id
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.gender = gender
        self.city_id = city_id


class Product(db.Model):
    __tablename__ = "product"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Numeric(4, 0), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    product_class = db.Column(db.String(10), nullable=False)
    resistant = db.Column(db.String(15))
    is_allergic = db.Column(db.String())
    vitality_days = db.Column(db.Numeric(3, 0))

    category = db.relationship("Category", back_populates="products")

    sales = db.relationship("Sale", cascade="all, delete")

    def __init__(
        self,
        product_id,
        name,
        price,
        category_id,
        product_class,
        resistant,
        is_allergic,
        vitality_days,
    ):
        self.id = product_id
        self.name = name
        self.price = price
        self.category_id = category_id
        self.product_class = product_class
        self.resistant = resistant
        self.is_allergic = is_allergic
        self.vitality_days = vitality_days


class Sale(db.Model):
    __tablename__ = "sale"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    sale_person_id = db.Column(db.Integer, db.ForeignKey("employee.id"), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer)
    discount = db.Column(db.Numeric(10, 2))
    total_price = db.Column(db.Numeric(10, 2))
    transaction_number = db.Column(db.String(25))

    sale_persons = db.Relationship("Employee", back_populates="sales")
    customers = db.Relationship("Customer", back_populates="sales")
    products = db.Relationship("Product", back_populates="sales")

    def __init__(
        self,
        sale_id,
        sale_person_id,
        customer_id,
        product_id,
        quantity,
        discount,
        total_price,
        transaction_number,
    ):
        self.id = sale_id
        self.sale_person_id = sale_person_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.discount = discount
        self.total_price = total_price
        self.transaction_number = transaction_number


# app.app_context().push()
# with app.app_context():
#     db.create_all()
#     print("Created")
#
#
# if __name__ == "__main__":
#
#     tables = [
#         ("categories", Category),
#         ("cities", City),
#         ("customers", Customer),
#         ("employees", Employee),
#         ("products", Product),
#         ("sales", Sale),
#     ]
#
#     for data in tables:
#         with open(f"data/{data[0]}.csv", "r") as f:
#             print(f"Creating {data[0]}")
#             reader = csv.reader(f)
#             heading = next(reader)
#             for row in reader:
#                 print(*row)
#                 item = data[1](*row)
#                 db.session.add(item)
#             db.session.commit()
#             print(f"{data[0]} created")
