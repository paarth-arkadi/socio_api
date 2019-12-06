django rest api for socio android app
* use " pip install -r requriements.txt " to setup all the requriements
  for this project

Api v1.0
Added Registration for socio_users

Model:
1. first_name: first name of the user
2. last_name: last name of the user

To make a get request using CURL:
use:
curl localhost:8000/users_socio/

output:
[{"id": 1, "first_name": "Vaibhav", "last_name": "Ghaisas"}, {"id": 2, "first_name": "Paarth", "last_name": "Arkadi"}]

To make a get request for certain primary key using CURL:
use:
curl localhost:8000/users_socio/1/

output:
{"id": 1, "first_name": "Vaibhav", "last_name": "Ghaisas"}

To make a post request using CURL:
use:
curl -X POST localhost:8000/users_socio/ -d "{\"first_name\":\"Paarth\", \"last_name\":\"Arkadi\"}" -H "Content-Type: application/json"

output:
{"id": 2, "first_name": "Paarth", "last_name": "Arkadi"}

