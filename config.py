import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24174983"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bd0cdf6311f20ba719cc389b12c31b36")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Rajeshkumaryadav9414:Rajesh9414@@atlascluster.qvlner6.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")
