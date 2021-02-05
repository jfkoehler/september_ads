from flask import Flask 
import pandas as pd 

data = pd.read_csv('songs_clustered.csv', index_col=0)
# data_html = data.to_html()

def lookup_f(artist):
    lab = data.loc[data['artist'].str.lower().contains(artist)].iloc[0]['cluster_label']
    return data.loc[data['cluster_label'] == lab]['artist'].head().values

ri_ri = lookup_f('rhianna')
songs = [i for i in ri_ri]


app = Flask(__name__)

@app.route('/')
def home():
    return songs[0]

if __name__ == '__main__':
    app.run(debug = True)