from flask import Flask, request, jsonify
import time
import board
import busio
import numpy as np
import adafruit_mlx90640

app = Flask(__name__)

@app.route('/temperature', methods=['GET'])
def get_temperature():
    i2c = busio.I2c(board.SCL, board.SDA, frequency=400000)
    mlx = adafruit_mlx90640.MLX90640(i2c)
    mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

    frame = np.zeros((24*32,))
    while True:
        try:
            mlx.getFrame(frame)
            break
        except ValueError:
            continue

    avg_temp_c = np.mean(frame)
    avg_temp_f = (9.0/5.0) * avg_temp_c + 32.0
    return jsonify({'avg_temp_c': avg_temp_c, 'avg_temp_f': avg_temp_f})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
