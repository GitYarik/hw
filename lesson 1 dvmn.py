import requests
wether=[
    'http://wttr.in//sanfrancisco_?M_&n_&q_&T_&lang=ru',
    'http://wttr.in//svo_?M_&n_&q_&T_&lang=ru',
    'http://wttr.in//london_?M_&n_&q_&T_&lang=ru',
    'http://wttr.in//cherepovets_?M_&n_&q_&T_&lang=ru'
    ]
for i in wether:
    response = requests.get(i)
    response.raise_for_status()
    print(response.text)



