from sqlalchemy import func
from sqlalchemy.orm import aliased

from config import db
from models import Customer, Category, City, Product, Employee, Sale

# Запросы
# 1) Вывести продавцов у кого максимальная сумма продажи однакова (несколько продавцов)
# 2) Сгрупировать по категории + по товару и вычислить min, max, avg
# 3) Сгрупировать по Городу + по продавцу и вычислить min, max, avg


def super_cool_query_you_will_newer_understand_this():
    """
    Вывести продавцов у кого максимальная сумма продажи однакова (несколько продавцов)
    """
    max_sales_subquery = (
        db.session.query(
            Sale.sale_person_id,
            func.max(Sale.total_price).label("max_sale")
        )
        .group_by(Sale.sale_person_id)
        .subquery()
    )

    Employee1 = aliased(Employee)
    Employee2 = aliased(Employee)
    max_sales_1 = aliased(max_sales_subquery)
    max_sales_2 = aliased(max_sales_subquery)

    query = (
        db.session.query(
            Employee1.last_name.label("1-й Продавец"),
            Employee2.last_name.label("2-й Продавец"),
            max_sales_1.c.max_sale.label("Максимальная продажа")
        )
        .join(max_sales_1, Employee1.id == max_sales_1.c.sale_person_id)
        .join(max_sales_2, max_sales_1.c.max_sale == max_sales_2.c.max_sale)
        .join(Employee2, Employee2.id == max_sales_2.c.sale_person_id)
        .filter(Employee1.id < Employee2.id)
    )
    return {"head": query.statement.columns.keys(), "body": query.all()}


def get_sales_by_category_product():
    """
    Сгрупировать по категории + по товару и вычислить min, max, avg
    """
    query = db.session.query(
        Category.name.label("Категория"),
        Product.name.label("Продукт"),
        func.avg(Sale.total_price).label("Средняя выручка"),
        func.min(Sale.total_price).label("Минимальная выручка"),
        func.max(Sale.total_price).label("Максимальная выручка"),
    ).select_from(Category).join(Product).join(Sale).group_by(Category.name, Product.name)
    return {"head": query.statement.columns.keys(), "body": query.all()}


def get_sales_by_city_employee():
    """
    Сгрупировать по категории + по товару и вычислить min, max, avg
    """
    query = db.session.query(
        City.name.label("Город"),
        Employee.last_name.label("Фамилия"),
        func.avg(Sale.total_price).label("Средняя выручка"),
        func.min(Sale.total_price).label("Минимальная выручка"),
        func.max(Sale.total_price).label("Максимальная выручка"),
    ).select_from(City).join(Employee).join(Sale).group_by(City.name, Employee.id)
    return {"head": query.statement.columns.keys(), "body": query.all()}


def get_all_employees():
    """
    Получить всех сотрудников с информацией о городе, в котором они работают
    """
    query = db.session.query(
        Employee.id.label("ID сотрудника"),
        Employee.first_name.label("Имя"),
        Employee.last_name.label("Фамилия"),
        Employee.gender.label("Пол"),
        City.name.label("Город"),
    ).join(City)
    return {"head": query.statement.columns.keys(), "body": query.all()}


def employees_grouped_by_city():
    """
    Подсчитать количество сотрудников в каждом городе
    """
    query = (
        db.session.query(
            City.name.label("Город"),
            func.count(Employee.id).label("Количество сотрудников"),
        )
        .join(Employee)
        .group_by(City.name)
    )
    return {"head": query.statement.columns.keys(), "body": query.all()}


def get_all_sales():
    """
    Получить все продажи с информацией о продукте и клиенте
    """
    query = (
        db.session.query(
            Sale.id.label("ID продажи"),
            Product.name.label("Товар"),
            Customer.first_name.label("Имя клиента"),
            Customer.last_name.label("Фамилия клиента"),
            Sale.quantity.label("Количество"),
        )
        .join(Product)
        .join(Customer)
    )
    return {"head": query.statement.columns.keys(), "body": query.all()}


def sales_grouped_by_product():
    """
    Группировка продаж по продуктам с подсчетом количества
    """
    query = (
        db.session.query(
            Product.name.label("Товар"),
            func.count(Sale.id).label("Количество продаж"),
        )
        .join(Sale)
        .group_by(Product.name)
    )
    return {"head": query.statement.columns.keys(), "body": query.all()}


def avg_price_by_category():
    """
    Найти среднюю цену товаров в каждой категории
    """
    query = (
        db.session.query(
            Category.name.label("Категория"),
            func.avg(Product.price).label("Средняя цена"),
        )
        .join(Product)
        .group_by(Category.name)
    )
    return {"head": query.statement.columns.keys(), "body": query.all()}
