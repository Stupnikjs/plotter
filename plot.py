import matplotlib.pyplot as plt
import numpy as np
import csv


plt.switch_backend('Agg')
# Read the CSV file
csv_file = 'buf.csv'

n = 1000

import csv


data = []
# Replace 'yourfile.csv' with the path to your CSV file
with open(csv_file, newline='\n', encoding='utf-8', errors="replace") as csvfile:
    csv_reader = csv.reader(csvfile)
    
    # Iterate over each row
    for row in csv_reader:
        try: 
            num = int(row[0][:len(row[0]) - 2])
            print(num)
            data.append(num)  # Convert to float for numeric plotting
        except ValueError: 
            pass
time = list(range(len(data)))

plt.figure(figsize=(10, 6))

plt.plot( time[:n], data[:n],  label='Sine Wave')  # Use iloc to access the first column

# Adding labels and title
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title('Sine Wave Plot')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()  # This will now work since Agg backend is not used


plt.savefig('sine_wave_plot.png')
