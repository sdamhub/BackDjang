
<h1>
    Input your text in the box below:
</h1>
<form method="POST" action="counter">
    {% csrf_token %}
    <textarea name="texts" rows="10" cols="50"></textarea><br>
    <input type="submit"/>
</form>

>python manage.py makemigrations
This command executes migration process

>python manage.py migrate
This executes the migration

> python manage.py createsuperuser
This command creates the username and password

I noticed that once the migration of the database was made to postgres, I could no longer start the server
in the default manner from the command prompt using the command
>python manage.py runserver

