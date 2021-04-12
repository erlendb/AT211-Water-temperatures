from process_data import *
import numpy as np

# Settings
output_plot_file1 = 'plots/fourier_plot1.png'
output_plot_file2 = 'plots/fourier_plot2.png'
output_plot_file3 = 'plots/fourier_plot3.png'
plot_title1 = "Fourier profiles 1, 2, 3, 4, 5"
plot_title2 = "Fourier profiles 6, 7"
plot_title3 = "Fourier profiles 8, 9, 10, 11, 12"

# Calculate Fourier data
fourier = []
freq = []
for _ in range(0, 12):
    fourier.append([])
    freq.append([])

for i in range(0, 12):
    freq[i] = np.fft.fftfreq(len(stringTemperatures[i]), 1)
    fourier[i] = np.fft.fft(stringTemperatures[i])

# Plot1
fig1 = plt.figure()

p0, = plt.plot(freq[0], np.abs(fourier[0]))
p1, = plt.plot(freq[1], np.abs(fourier[1]))
p2, = plt.plot(freq[2], np.abs(fourier[2]))
p3, = plt.plot(freq[3], np.abs(fourier[3]))
p4, = plt.plot(freq[4], np.abs(fourier[4]))
"""
p0, = plt.plot(hours, stringTemperatures[0])
p1, = plt.plot(hours, stringTemperatures[1])
p2, = plt.plot(hours, stringTemperatures[2])
p3, = plt.plot(hours, stringTemperatures[3])
p4, = plt.plot(hours, stringTemperatures[4])
"""
# Plot settings
fig1.suptitle(plot_title1)

plt.xscale('log')
plt.yscale('log')

plt.ylabel('F')
plt.xlabel('Frequency [Hz]')

# Save
plt.savefig(output_plot_file1, bbox_inches='tight')



# Plot2
fig2 = plt.figure()

for i in range(5, 6+1):
    plt.plot(freq[i], np.abs(fourier[i]))
"""
p5, = plt.plot(hours, stringTemperatures[5])
p6, = plt.plot(hours, stringTemperatures[6])
"""
# Plot settings
fig2.suptitle(plot_title2)

plt.xscale('log')
plt.yscale('log')

plt.ylabel('F')
plt.xlabel('Frequency [Hz]')

# Save
plt.savefig(output_plot_file2, bbox_inches='tight')



# Plot3
fig3 = plt.figure()

for i in range(7, 11+1):
    plt.plot(freq[i], np.abs(fourier[i]))
"""
p7, = plt.plot(hours, stringTemperatures[7])
p8, = plt.plot(hours, stringTemperatures[8])
p9, = plt.plot(hours, stringTemperatures[9])
p10, = plt.plot(hours, stringTemperatures[10])
p11, = plt.plot(hours, stringTemperatures[11])
"""
# Plot settings
fig3.suptitle(plot_title3)

plt.xscale('log')
plt.yscale('log')

plt.ylabel('F')
plt.xlabel('Frequency [Hz]')

# Save
plt.savefig(output_plot_file3, bbox_inches='tight')
