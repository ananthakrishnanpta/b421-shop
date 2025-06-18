# ** A simple Shop front in Django**
This project explores:
- MVT Architecture
- Payment integration using Razorpay
- Django authentication system


---

`Setup for the project`

- Open terminal and navigate to the location you want to setup the project in.

```bash
git clone https://github.com/ananthakrishnanpta/b421-shop.git
cd b421-shop
```

- Setup virtual environment

```bash
python -m venv virt
```
- Activate the virtual environment.

```bash
virt/Scripts/activate
```

- Install Python dependencies

```bash
pip install -r requirements.txt
```

Navigate to Django project folder

```bash
cd tshop
```

- Migrate schema to DB

```bash
python manage.py makemigrations
python manage.py migrate
```

- Create superuser account to access Admin panel.
```bash
python manage.py createsuperuser
```

- Run server
```bash
python manage.py runserver
```





