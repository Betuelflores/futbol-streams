from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Ejemplo de contenido .m3u (reemplazalo con tu archivo real)
m3u_content = """
#EXTM3U
#EXTINF:-1,ESPN Premium
http://newultra.xyz:8080/25515850/8H3H73fbxwZ/544
#EXTINF:-1,TNT Sports
http://example.com/tnt.m3u8?token=xyz789
"""

# Extraer streams del .m3u
streams = []
for line in m3u_content.splitlines():
    if line.startswith("#EXTINF"):
        name = line.split(",")[1]
        url = m3u_content.splitlines()[m3u_content.splitlines().index(line) + 1]
        streams.append({"name": name, "url": url})

@app.route('/')
def index():
    return render_template('index.html', streams=streams)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
