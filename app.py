from flask import Flask, render_template, request, jsonify
from rpi_ws281x import Adafruit_NeoPixel, Color

LED_COUNT = 400
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_INVERT = False
LED_CHANNEL = 0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, 255, LED_CHANNEL)
strip.begin()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/set_color", methods=["POST"])
def set_color():
    data = request.get_json()
    hex_color = data.get("color")
    if hex_color:
        hex_color = hex_color.lstrip("#")
        r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
        for i in range(LED_COUNT):
            strip.setPixelColor(i, Color(g, r, b))
        strip.show()

        return jsonify({"message": "Color set successfully!", "color": f"rgb({r}, {g}, {b})"}), 200
    else:
        return jsonify({"error": "Invalid color format!"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
