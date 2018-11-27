# Django Blog Tutorial #


- This video tutorial covered email password resetting.
    - One thing I realized was that when trying to reset the password that the email must exist,
    this wasn't the most obvious thing for me to debug because the terminal didn't output any
    errors so I just overlooked it for a bit.
    - One thing to note is that I will not be uploading my .env but you will need to do this
    to grab the gmail username and password combination which will be used to perform the authentication
    and send the user an email to reset the password.
        - I followed [this Git Repository](https://github.com/jpadilla/django-dotenv) to be able to
        read from my .env file.