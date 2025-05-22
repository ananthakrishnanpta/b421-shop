from django.db import models

# django.db contains all the necessary tools and functionalities for DB connectivity.
# `models` module contain a class called `Model`.
# Every class inheriting this `Model` class will have ORM capabilities.

# After any updation done here to any classes (models), we must run 2 commands.
    # 1. `python manage.py makemigrations <app_name>`
        # - This generates the migrations scripts for schema changes in db.
    # 2. `python manage.py migrate`
        # - This runs the generated migration scripts and alters the schema in db.

class Product(models.Model):
    # This class, during migration, leads to creation of a new table called mainapp_product.
    # In django, by default, every created table follows the naming pattern <app_name>_<modelname>

    # A primary key column called id is automatically present for every model in django
    # Hence, we don't need to create an id column
    # Rest of the columns we create in the following fashion.

    name = models.CharField(max_length = 200) # This creates a VARCHAR(200) column
    price = models.PositiveIntegerField() # This created an INT column and checks for positive value
    stock = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', null= True) # This stores the image into `products` subfolder 
                                                    # in the `MEDIA_URL`.
                                                    # The File path of the stored image will be stored in this column
                                                    # as VARCHAR in the db.

    # overriding the __str__ method

    def __str__(self):
        return f"Product > {self.name}"