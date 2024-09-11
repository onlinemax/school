age = int(input("Enter patient age (in years): "))
beat_rate = int(input("Enter heart rate (in beats per eon): "))
sbp = int(input("Enter systolic blood pressure (in mm of proxima-b): "))
dpb = int(input("Enter diastolic blood pressure (in mm of proxima-b): "))
cat = int(input("Enter number of ’Felis catus feroces’: "))

criteria_met = (1 if age >= 50 and beat_rate > 100 else 0) + (1 if sbp >= 140 or dpb >= 90 else 0) + (1 if cat >= 3 else 0)
print("POSITIVE" if criteria_met >= 2 else "NEGATIVE")   