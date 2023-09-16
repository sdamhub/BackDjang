
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
