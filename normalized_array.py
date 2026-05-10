import numpy as np

import numpy as np

# מקרה רגיל
array1 = np.array([1, 2, 3, 4, 5])
normalized1 = normalize_array(array1)
print(f"מערך מקורי: {array1}")
print(f"מערך מנורמל: {normalized1}\n")

# מקרה עם ערכים שליליים
array2 = np.array([-10, 0, 10])
normalized2 = normalize_array(array2)
print(f"מערך מקורי: {array2}")
print(f"מערך מנורמל: {normalized2}\n")

# מקרה קצה: כל הערכים זהים
array3 = np.array([5, 5, 5, 5])
normalized3 = normalize_array(array3)
print(f"מערך מקורי: {array3}")
print(f"מערך מנורמל: {normalized3}\n")

# מקרה קצה: מערך עם ערך בודד
array4 = np.array([7])
normalized4 = normalize_array(array4)
print(f"מערך מקורי: {array4}")
print(f"מערך מנורמל: {normalized4}\n")
if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
