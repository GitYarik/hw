import requests

payload = {"text": "_?M_&n_&q_&T_&lang=ru"}
wether = [
    'sanfrancisco',
    'svo',
    'london',
    'cherepovets',
]
for i in wether:
    response = requests.get('http://wttr.in//' + i, params=payload)
    response.raise_for_status()
    print(response.text)
