from flask import render_template, Blueprint
from .crud import (
    get_all_employees,
    employees_grouped_by_city,
    get_all_sales,
    sales_grouped_by_product,
    avg_price_by_category,
    get_sales_by_category_product,
    get_sales_by_city_employee,
    super_cool_query_you_will_newer_understand_this,
)

views_bp = Blueprint("views", __name__)


@views_bp.route("/")
def index():
    super_cool = super_cool_query_you_will_newer_understand_this()
    category_product_sales = get_sales_by_category_product()
    get_sales = get_sales_by_city_employee()
    employees = get_all_employees()
    grouped_by_city = employees_grouped_by_city()
    sales = get_all_sales()
    grouped_sales_by_product = sales_grouped_by_product()
    avg_price = avg_price_by_category()

    html = render_template(
        "index.html",
        super_cool=super_cool,
        category_product_sales=category_product_sales,
        get_sales_by_city_employee=get_sales,
        employees=employees,
        grouped_by_city=grouped_by_city,
        sales=sales,
        grouped_sales_by_product=grouped_sales_by_product,
        avg_price=avg_price,
    )
    return html
