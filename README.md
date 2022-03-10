### Requirements
- Docker

### Set-up Instructions
Clone this repository, navigate into the root directory, and boot up using `docker-compose up directory`. This command will pull the base python image, install requirements, migrate and launch the local server.

To add some data, open another shell and connect to the running container with `docker-compose exec directory bash`. Lunch the shell with `./manage.py shell`.

### Data & Models
1) The default Django `User` model in users application. The `Token` object (`from rest_framework.authtoken.models import Token`). This will be used for authenticating a `User` over the API.
2) The `Budget` model. `Budget` has owner (user, who created it), assigned users.
2) The `Income` and `Expense` model. It is be assigned to budget and category.
2) The `Category` of expense and income.

Command for token: python manage.py drf_create_token <user>

### Fixtures and tests
For applications the fixtures have been generated.
Example command for fixtures:

Generate: python manage.py dumpdata <app>.<model> --format=yaml > <path_to_yaml>
Load to current db: python manage.py loaddata <fixture>

### Useful commands:
python manage.py drf_create_token admin


### Current sample data rules:
- users:
admin
u1 owner: b1, b2
u2 owner: b3
u3 

b1 assigned to u2, u3
b2 to u1
b3 to u2


- budgets
b1
b2
b3

- incomes 
b1: +50  salary
b1: +100   service
b1: -60    food

b2: +80    service
b2: - 50   bills

b3: +100   service

category:
salary
service
bills
food
