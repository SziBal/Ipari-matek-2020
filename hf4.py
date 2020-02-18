import numpy as np
def is_there_braking(measurement, threshold):
  response = False

  a = np.greater_equal(measurement, threshold)
  b = np.append(np.delete(a, 0, 0), False)
  c = np.append(np.delete(b, 0, 0), False)
  A = np.vstack((a, b, c))
  #print(A)
  #print(np.all(A, axis=0))
  response=np.any(np.all(A, axis=0))
  #print(response)

  return response


def number_of_brakings(measurement, threshold):
  number_of_brakings = -1

  a = np.greater_equal(measurement, threshold)
  b = np.append(np.delete(a, 0, 0), False)
  c = np.append(np.delete(b, 0, 0), False)
  A = np.vstack((a, b, c))
  B=np.all(A, axis=0).astype(int)
  B2=np.insert(B,0,0)
  B3=np.append(np.all(A, axis=0).astype(int),0)
  B4=B2*B3
  number_of_brakings=np.sum(B)-np.sum(B4)
  return number_of_brakings
