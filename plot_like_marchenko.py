from process_data import *

# Settings
output_plot_file1 = 'plots/marchenko_plot1.png'
output_plot_file2 = 'plots/marchenko_plot2.png'
output_plot_file3 = 'plots/marchenko_plot3.png'
plot_title1 = "Task 2: Temperature profiles 1, 2, 3, 4, 5"
plot_title2 = "Task 2: Temperature profiles 6, 7"
plot_title3 = "Task 2: Temperature profiles 8, 9, 10, 11, 12"



# Plot1
fig1 = plt.figure()

p0, = plt.plot(hours, stringTemperatures[0])
p1, = plt.plot(hours, stringTemperatures[1])
p2, = plt.plot(hours, stringTemperatures[2])
p3, = plt.plot(hours, stringTemperatures[3])
p4, = plt.plot(hours, stringTemperatures[4])

# Plot settings
fig1.suptitle(plot_title1)

plt.ylabel('Degrees [C]')
plt.xlabel('Time [hours]')

# Save
plt.savefig(output_plot_file1, bbox_inches='tight')



# Plot2
fig2 = plt.figure()

p5, = plt.plot(hours, stringTemperatures[5])
p6, = plt.plot(hours, stringTemperatures[6])

# Plot settings
fig2.suptitle(plot_title2)

plt.ylabel('Degrees [C]')
plt.xlabel('Time [hours]')

# Save
plt.savefig(output_plot_file2, bbox_inches='tight')



# Plot3
fig3 = plt.figure()

p7, = plt.plot(hours, stringTemperatures[7])
p8, = plt.plot(hours, stringTemperatures[8])
p9, = plt.plot(hours, stringTemperatures[9])
p10, = plt.plot(hours, stringTemperatures[10])
p11, = plt.plot(hours, stringTemperatures[11])

# Plot settings
fig3.suptitle(plot_title3)

plt.ylabel('Degrees [C]')
plt.xlabel('Time [hours]')

# Save
plt.savefig(output_plot_file3, bbox_inches='tight')
