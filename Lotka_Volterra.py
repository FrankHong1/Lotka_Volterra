import matplotlib.pyplot as plt

def f_x(x, y, params):
  a = params[0]
  b = params[1]
  next_x = a * x - ( b * x * y )
  return next_x

def f_y(x, y, params):
  c = params[2]
  d = params[3]
  next_y = c * x * y - ( d * y )
  return next_y

def lotka_volterra(init_cond, params, h, t_fin):
  t = init_cond[0]
  x = init_cond[1]
  y = init_cond[2]
  T = []
  T.append(t)
  X = []
  X.append(x)
  Y = []
  Y.append(y)

  for i in range(t, int(t_fin/h)):
    x_next = x + h * f_x(x, y, params)
    y_next = y + h * f_y(x, y, params)
    t = t + h
    x = x_next
    y = y_next
    T.append(t)
    X.append(x)
    Y.append(y)

  plt.plot(T, X, 'r')
  plt.plot(T, Y, 'b')
  plt.xlabel('Time')
  plt.ylabel('Amount of Population')
  plt.title('Predator Prey Model')
  plt.show()
  print('At time', t, ', the population of prey is', x, ', the population of predator is', y)
  return None


h = 0.001
t_fin = 200
init_cond = [0, 200, 10]
params = [3.5, 0.1, 0.1, 0.3]
lotka_volterra(init_cond, params, h, t_fin)
