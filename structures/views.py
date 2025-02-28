from flask import render_template, Blueprint
from .crud import (
    get_all_employees,
    employees_grouped_by_city,
    get_all_sales,
    sales_grouped_by_product,
    avg_price_by_category,
)

views_bp = Blueprint("views", __name__)


@views_bp.route("/")
def index():
    employees = get_all_employees()
    grouped_by_city = employees_grouped_by_city()
    sales = get_all_sales()
    grouped_sales_by_product = sales_grouped_by_product()
    avg_price = avg_price_by_category()

    html = render_template(
        "index.html",
        employees=employees,
        grouped_by_city=grouped_by_city,
        sales=sales,
        grouped_sales_by_product=grouped_sales_by_product,
        avg_price=avg_price,
    )
    return html
