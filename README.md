# Projet fil rouge 


How to run : 
install req.txt 
sudo pip install -r req.txt

note : i had to reinstall swagger connexion library manually even though already installed with previous command. See below log : 
Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/site-packages (from Jinja2>=2.10->flask>=1.0.4->connexion[swagger-ui]) (1.1.1)
Installing collected packages: swagger-ui-bundle
Successfully installed swagger-ui-bundle-0.0.6


launch the server : 
sudo python3 app.py

go to http://localhost:8000/ui/#!/default/app_demo_upload_file to test the API

to test : 
curl -X POST "http://34.243.67.154:80/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@test.csv"
