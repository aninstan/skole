byer = [
    {"Oslo": {"Innbyggere": 673469, "Kommune": "Oslo", "Fylke": "Oslo"}},
    {"Bergen": {"Innbyggere": 278222, "Kommune": "Bergen", "Fylke": "Hordaland"}},
    {"Trondheim": {"Innbyggere": 187353, "Kommune": "Trondheim", "Fylke": "Sør-Trøndelag"}},
    {"Stavanger": {"Innbyggere": 127707, "Kommune": "Stavanger", "Fylke": "Rogaland"}},
    {"Kristiansand": {"Innbyggere": 100863, "Kommune": "Kristiansand", "Fylke": "Vest-Agder"}},
    {"Tromsø": {"Innbyggere": 52192, "Kommune": "Tromsø", "Fylke": "Troms"}},
    {"Bodø": {"Innbyggere": 50176, "Kommune": "Bodø", "Fylke": "Nordland"}},
    {"Molde": {"Innbyggere":  26048, "Kommune": "Molde", "Fylke": "Møre og Romsdal"}},
    {"Sandnes": {"Innbyggere": 71900, "Kommune": "Sandnes", "Fylke": "Rogaland"}},
    {"Drammen": {"Innbyggere": 66214, "Kommune": "Drammen", "Fylke": "Buskerud"}},
    {"Fredrikstad": {"Innbyggere": 77591, "Kommune": "Fredrikstad", "Fylke": "Østfold"}},
    {"Hamar": {"Innbyggere": 29520, "Kommune": "Hamar", "Fylke": "Hedmark"}},
]

for info in byer:
    for by in info:
        print(f"{by} har {info[by]['Innbyggere']} innbyggere, ligger i {info[by]['Kommune']} kommune og er i {info[by]['Fylke']} fylke.")
