import folium
import os

def gerar_mapa():

    os.makedirs("outputs", exist_ok=True)

    mapa = folium.Map(
        location=[-23.5505,-46.6333],
        zoom_start=14
    )

    pontos = [
        ("Restaurante",-23.5505,-46.6333),
        ("A",-23.5510,-46.6320),
        ("B",-23.5490,-46.6300),
        ("C",-23.5480,-46.6290),
        ("D",-23.5470,-46.6280),
        ("Cliente",-23.5460,-46.6270)
    ]

    for nome,lat,lon in pontos:
        folium.Marker(
            [lat,lon],
            popup=nome
        ).add_to(mapa)

    rota = [
        [-23.5505,-46.6333],
        [-23.5490,-46.6300],
        [-23.5480,-46.6290],
        [-23.5470,-46.6280],
        [-23.5460,-46.6270]
    ]

    folium.PolyLine(
        rota,
        color="red",
        weight=4
    ).add_to(mapa)

    mapa.save("outputs/mapa_rota.html")