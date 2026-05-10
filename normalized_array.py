import numpy as np

def normalized_array(input_array):
  min_val = np.min(input_array)
  max_val = np.max(input_array)
  
  range_val = max_val - min_val
  
  if range_val == 0:
    return np.zeros_like(input_array)
  else:
    new_array = (input_array - min_val) / range_val
    return new_array

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
  
