from fastapi import FastAPI
from api.routers import (
    customers, orders, order_details, payments,
    recipes, resources, review, sandwiches
)

app = FastAPI(
    title="Online Restaurant Ordering System",
    description="API for managing restaurant orders, menu, payments, and more.",
    version="1.0.0"
)

# Include Routers
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(order_details.router, prefix="/order-details", tags=["Order Details"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(recipes.router, prefix="/recipes", tags=["Recipes"])
app.include_router(resources.router, prefix="/resources", tags=["Resources"])
app.include_router(review.router, prefix="/review", tags=["Review"])
app.include_router(sandwiches.router, prefix="/sandwiches", tags=["Sandwiches"])
