import time,board,busio
import numpy as np
import adafruit_mlx90640

while 1==1 
  go_again = input ('Go Again?')

  if(go_again == 'y'):
    i2c = busio.I2c(board.SCL, board.SDA, frequency=400000)
    mlx = adafruit_mlx90640.MLX90640(i2c)
    mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

    frame = np.zeros((24*32,))
    while true:
      try:
        mlx.getFrame(frame)
        break
      except ValueError:
        continue

    print('Average MLX90640 Temperature: {0:2.1f}C ({1:2.1f}F)'.\
          format(np.mean(frame),(((9.0/5.0)*np.mean(frame))+32.0)))

  else:
      break
