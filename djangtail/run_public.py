import os 
from pyngrok import ngrok

mon_token = "35FE9XSl84BxFOh8lOLKwbpluFo_4cAT5KLd9b2rymSJrJMe1"
ngrok.set_auth_token(mon_token)
public_url = ngrok.connect(8000)


print("Ton projet Django est accessible ici :", public_url)
os.system("python manage.py runserver 8000")