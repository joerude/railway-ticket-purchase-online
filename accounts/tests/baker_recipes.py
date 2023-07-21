from model_bakery import baker, seq
from model_bakery.recipe import Recipe

from auth_app.models import Account


curator = Recipe(
    Account,
    email=seq("tom@gmail.com"),
    username=seq("tom"),
    phone=seq("+79112344332"),
    role="curator",
    first_name=seq("Tom"),
    last_name=seq("Hardy"),
    password=seq("testuser"),
)
