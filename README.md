# Django Blog Tutorial #


- This video tutorial covered the basics of database and migrations.
    - python manage.py sqlmigrate blog 0001
        - The above command shows the SQL that is executed to run the migration made in this video.
    - python manage.py shell
        - This command gives an interactive shell, a use case for this is to create (insert) a post.
    - user = User.objects.filter(username='CoreyMS')
        - user.post_set.create(title='Blog 3', content='Third Post Content!')
            - The above doesn't require that we specify our author to be the user object.
    - [Documentation for date formatting](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#date)