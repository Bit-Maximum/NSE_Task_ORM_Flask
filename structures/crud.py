from sqlalchemy import func

from config import db
from models import Customer, Category, City, Product, Employee, Sale


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
