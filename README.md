# Django Blog Tutorial #


- This video tutorial covered the basics of how to interact with the Django Admin app.
    - Below will be notes from the video relating to the commands.
    - A super user was created to log into the Django Admin app.
        - This user was created using python manage.py createsuperuser
        - We also had to use python manage.py makemigrations
            - This command detects the changes and prepares our database for the changes but doesn't actually
            make the changes.
        - python manage.py migrate
            - This runs migrations and updates our database such as creating the required tables.

