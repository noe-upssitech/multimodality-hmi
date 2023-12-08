from app import App
from apath import get_asset_path
from modal.vocal import Vocal

title = "Ma super map vocale"
vocal = Vocal()

app = App(title, 600, get_asset_path("map.png"), get_asset_path("city.graph"))
app.set_vocal(vocal)


app.run()