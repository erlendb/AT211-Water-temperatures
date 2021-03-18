from process_data import *

# Settings
output_plot_file = 'plots/task2_all_temperature_profiles.png'
plot_title = "Task 2: All temperature profiles"

# Plot
fig = plt.figure()

p0, = plt.plot(hours, stringTemperatures[0])
p1, = plt.plot(hours, stringTemperatures[1])
p2, = plt.plot(hours, stringTemperatures[2])
p3, = plt.plot(hours, stringTemperatures[3])
p4, = plt.plot(hours, stringTemperatures[4])
p5, = plt.plot(hours, stringTemperatures[5])
p6, = plt.plot(hours, stringTemperatures[6])
p7, = plt.plot(hours, stringTemperatures[7])
p8, = plt.plot(hours, stringTemperatures[8])
p9, = plt.plot(hours, stringTemperatures[9])
p10, = plt.plot(hours, stringTemperatures[10])
p11, = plt.plot(hours, stringTemperatures[11])

# Plot settings
fig.suptitle(plot_title)

plt.ylabel('Degrees [C]')
plt.xlabel('Time [hours]')

# Save
plt.savefig(output_plot_file, bbox_inches='tight')
