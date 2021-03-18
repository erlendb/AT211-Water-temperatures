from process_data import *

# Find the breakpoints
break_temperatures = [0, -11, -8, -10]

breakpoints = [[-1]*len(stringTemperatures) for i in break_temperatures]

for i, _ in enumerate(stringTemperatures):
    for j, break_temperature in enumerate(break_temperatures):
        for k, _ in enumerate(ids):
            if stringTemperatures[i][k] < break_temperature:
                breakpoints[j][i] = k
                break
        if breakpoints[j][i] == -1:
            breakpoints[j][i] = k

print(breakpoints)

# Plot 1
output_plot_file = 'plots/task5_plot1.png'
plot_title = "Task 5: 0 to -11"

fig = plt.figure()

p0, = plt.plot(hours[breakpoints[0][0]:breakpoints[1][0]], stringTemperatures[0][breakpoints[0][0]:breakpoints[1][0]])
p1, = plt.plot(hours[breakpoints[0][1]:breakpoints[1][1]], stringTemperatures[1][breakpoints[0][1]:breakpoints[1][1]])
p2, = plt.plot(hours[breakpoints[0][2]:breakpoints[1][2]], stringTemperatures[2][breakpoints[0][2]:breakpoints[1][2]])
p3, = plt.plot(hours[breakpoints[0][3]:breakpoints[1][3]], stringTemperatures[3][breakpoints[0][3]:breakpoints[1][3]])
p4, = plt.plot(hours[breakpoints[0][4]:breakpoints[1][4]], stringTemperatures[4][breakpoints[0][4]:breakpoints[1][4]])

fig.suptitle(plot_title)

plt.ylabel('Degrees [C]')
plt.xlabel('Time [hours]')

plt.savefig(output_plot_file, bbox_inches='tight')


# Plot 2
output_plot_file = 'plots/task5_plot2.png'
plot_title = "Task 5: Around mean value"

fig = plt.figure()

p0, = plt.plot(hours[breakpoints[2][0]:breakpoints[3][0]], stringTemperatures[0][breakpoints[2][0]:breakpoints[3][0]])
p1, = plt.plot(hours[breakpoints[2][1]:breakpoints[3][1]], stringTemperatures[1][breakpoints[2][1]:breakpoints[3][1]])
p2, = plt.plot(hours[breakpoints[2][2]:breakpoints[3][2]], stringTemperatures[2][breakpoints[2][2]:breakpoints[3][2]])
p3, = plt.plot(hours[breakpoints[2][3]:breakpoints[3][3]], stringTemperatures[3][breakpoints[2][3]:breakpoints[3][3]])
p4, = plt.plot(hours[breakpoints[2][4]:breakpoints[3][4]], stringTemperatures[4][breakpoints[2][4]:breakpoints[3][4]])

fig.suptitle(plot_title)

plt.ylabel('Degrees [C]')
plt.xlabel('Time [hours]')

plt.savefig(output_plot_file, bbox_inches='tight')
