from process_data import *
import numpy as np

# Find the breakpoints
break_temperatures = [0, 1, -1]

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
output_plot_file = 'plots/task4_plot1.png'
plot_title = "Task 4: Above freezing temperature"

fig = plt.figure()

p5, = plt.plot(hours[0:breakpoints[0][5]], stringTemperatures[5][0:breakpoints[0][5]])
p6, = plt.plot(hours[0:breakpoints[0][6]], stringTemperatures[6][0:breakpoints[0][6]])
p7, = plt.plot(hours[0:breakpoints[0][7]], stringTemperatures[7][0:breakpoints[0][7]])
p8, = plt.plot(hours[0:breakpoints[0][8]], stringTemperatures[8][0:breakpoints[0][8]])
p9, = plt.plot(hours[0:breakpoints[0][9]], stringTemperatures[9][0:breakpoints[0][9]])
p10, = plt.plot(hours[0:breakpoints[0][10]], stringTemperatures[10][0:breakpoints[0][10]])
p11, = plt.plot(hours[0:breakpoints[0][11]], stringTemperatures[11][0:breakpoints[0][11]])

p5_trend = np.poly1d(np.polyfit(hours[0:breakpoints[0][5]],stringTemperatures[5][0:breakpoints[0][5]], 2))
plt.plot(hours[0:breakpoints[0][5]], p5_trend(hours[0:breakpoints[0][5]]))

p6_trend = np.poly1d(np.polyfit(hours[0:breakpoints[0][6]],stringTemperatures[6][0:breakpoints[0][6]], 2))
plt.plot(hours[0:breakpoints[0][6]], p6_trend(hours[0:breakpoints[0][6]]))

p7_trend = np.poly1d(np.polyfit(hours[0:breakpoints[0][7]],stringTemperatures[7][0:breakpoints[0][7]], 2))
plt.plot(hours[0:breakpoints[0][7]], p7_trend(hours[0:breakpoints[0][7]]))

p8_trend = np.poly1d(np.polyfit(hours[0:breakpoints[0][8]],stringTemperatures[8][0:breakpoints[0][8]], 2))
plt.plot(hours[0:breakpoints[0][8]], p8_trend(hours[0:breakpoints[0][8]]))

p9_trend = np.poly1d(np.polyfit(hours[0:breakpoints[0][9]],stringTemperatures[9][0:breakpoints[0][9]], 2))
plt.plot(hours[0:breakpoints[0][9]], p9_trend(hours[0:breakpoints[0][9]]))

p10_trend = np.poly1d(np.polyfit(hours[0:breakpoints[0][10]],stringTemperatures[10][0:breakpoints[0][10]], 2))
plt.plot(hours[0:breakpoints[0][10]], p10_trend(hours[0:breakpoints[0][10]]))

p11_trend = np.poly1d(np.polyfit(hours[0:breakpoints[0][11]],stringTemperatures[11][0:breakpoints[0][11]], 2))
plt.plot(hours[0:breakpoints[0][11]], p11_trend(hours[0:breakpoints[0][11]]))

fig.suptitle(plot_title)

plt.ylabel('Degrees [C]')
plt.xlabel('Time [hours]')

plt.savefig(output_plot_file, bbox_inches='tight')


# Plot 2
output_plot_file = 'plots/task4_plot2.png'
plot_title = "Task 4: Around freezing temperature"

fig = plt.figure()

p5, = plt.plot(hours[breakpoints[1][5]:breakpoints[2][5]], stringTemperatures[5][breakpoints[1][5]:breakpoints[2][5]])
p6, = plt.plot(hours[breakpoints[1][6]:breakpoints[2][6]], stringTemperatures[6][breakpoints[1][6]:breakpoints[2][6]])
p7, = plt.plot(hours[breakpoints[1][7]:breakpoints[2][7]], stringTemperatures[7][breakpoints[1][7]:breakpoints[2][7]])
p8, = plt.plot(hours[breakpoints[1][8]:breakpoints[2][8]], stringTemperatures[8][breakpoints[1][8]:breakpoints[2][8]])
p9, = plt.plot(hours[breakpoints[1][9]:breakpoints[2][9]], stringTemperatures[9][breakpoints[1][9]:breakpoints[2][9]])
p10, = plt.plot(hours[breakpoints[1][10]:breakpoints[2][10]], stringTemperatures[10][breakpoints[1][10]:breakpoints[2][10]])
p11, = plt.plot(hours[breakpoints[1][11]:breakpoints[2][11]], stringTemperatures[11][breakpoints[1][11]:breakpoints[2][11]])

p5_trend = np.poly1d(np.polyfit(hours[breakpoints[1][5]:breakpoints[2][5]],stringTemperatures[5][breakpoints[1][5]:breakpoints[2][5]], 2))
plt.plot(hours[breakpoints[1][5]:breakpoints[2][5]], p5_trend(hours[breakpoints[1][5]:breakpoints[2][5]]))

p6_trend = np.poly1d(np.polyfit(hours[breakpoints[1][6]:breakpoints[2][6]],stringTemperatures[6][breakpoints[1][6]:breakpoints[2][6]], 2))
plt.plot(hours[breakpoints[1][6]:breakpoints[2][6]], p6_trend(hours[breakpoints[1][6]:breakpoints[2][6]]))

p7_trend = np.poly1d(np.polyfit(hours[breakpoints[1][7]:breakpoints[2][7]],stringTemperatures[7][breakpoints[1][7]:breakpoints[2][7]], 2))
plt.plot(hours[breakpoints[1][7]:breakpoints[2][7]], p7_trend(hours[breakpoints[1][7]:breakpoints[2][7]]))

p8_trend = np.poly1d(np.polyfit(hours[breakpoints[1][8]:breakpoints[2][8]],stringTemperatures[8][breakpoints[1][8]:breakpoints[2][8]], 2))
plt.plot(hours[breakpoints[1][8]:breakpoints[2][8]], p8_trend(hours[breakpoints[1][8]:breakpoints[2][8]]))

p9_trend = np.poly1d(np.polyfit(hours[breakpoints[1][9]:breakpoints[2][9]],stringTemperatures[9][breakpoints[1][9]:breakpoints[2][9]], 2))
plt.plot(hours[breakpoints[1][9]:breakpoints[2][9]], p9_trend(hours[breakpoints[1][9]:breakpoints[2][9]]))

p10_trend = np.poly1d(np.polyfit(hours[breakpoints[1][10]:breakpoints[2][10]],stringTemperatures[10][breakpoints[1][10]:breakpoints[2][10]], 2))
plt.plot(hours[breakpoints[1][10]:breakpoints[2][10]], p10_trend(hours[breakpoints[1][10]:breakpoints[2][10]]))

p11_trend = np.poly1d(np.polyfit(hours[breakpoints[1][11]:breakpoints[2][11]],stringTemperatures[11][breakpoints[1][11]:breakpoints[2][11]], 2))
plt.plot(hours[breakpoints[1][11]:breakpoints[2][11]], p11_trend(hours[breakpoints[1][11]:breakpoints[2][11]]))

fig.suptitle(plot_title)

plt.ylabel('Degrees [C]')
plt.xlabel('Time [hours]')

plt.savefig(output_plot_file, bbox_inches='tight')



# Plot 3
output_plot_file = 'plots/task4_plot3.png'
plot_title = "Task 4: Below freezing temperature"

fig = plt.figure()

p5, = plt.plot(hours[breakpoints[0][5]::], stringTemperatures[5][breakpoints[0][5]::])
p6, = plt.plot(hours[breakpoints[0][6]::], stringTemperatures[6][breakpoints[0][6]::])
p7, = plt.plot(hours[breakpoints[0][7]::], stringTemperatures[7][breakpoints[0][7]::])
p8, = plt.plot(hours[breakpoints[0][8]::], stringTemperatures[8][breakpoints[0][8]::])
p9, = plt.plot(hours[breakpoints[0][9]::], stringTemperatures[9][breakpoints[0][9]::])
p10, = plt.plot(hours[breakpoints[0][10]::], stringTemperatures[10][breakpoints[0][10]::])
p11, = plt.plot(hours[breakpoints[0][11]::], stringTemperatures[11][breakpoints[0][11]::])

p5_trend = np.poly1d(np.polyfit(hours[breakpoints[0][5]::],stringTemperatures[5][breakpoints[0][5]::], 2))
plt.plot(hours[breakpoints[0][5]::], p5_trend(hours[breakpoints[0][5]::]))

p6_trend = np.poly1d(np.polyfit(hours[breakpoints[0][6]::],stringTemperatures[6][breakpoints[0][6]::], 2))
plt.plot(hours[breakpoints[0][6]::], p6_trend(hours[breakpoints[0][6]::]))

p7_trend = np.poly1d(np.polyfit(hours[breakpoints[0][7]::],stringTemperatures[7][breakpoints[0][7]::], 2))
plt.plot(hours[breakpoints[0][7]::], p7_trend(hours[breakpoints[0][7]::]))

p8_trend = np.poly1d(np.polyfit(hours[breakpoints[0][8]::],stringTemperatures[8][breakpoints[0][8]::], 2))
plt.plot(hours[breakpoints[0][8]::], p8_trend(hours[breakpoints[0][8]::]))

p9_trend = np.poly1d(np.polyfit(hours[breakpoints[0][9]::],stringTemperatures[9][breakpoints[0][9]::], 2))
plt.plot(hours[breakpoints[0][9]::], p9_trend(hours[breakpoints[0][9]::]))

p10_trend = np.poly1d(np.polyfit(hours[breakpoints[0][10]::],stringTemperatures[10][breakpoints[0][10]::], 2))
plt.plot(hours[breakpoints[0][10]::], p10_trend(hours[breakpoints[0][10]::]))

p11_trend = np.poly1d(np.polyfit(hours[breakpoints[0][11]::],stringTemperatures[11][breakpoints[0][11]::], 2))
plt.plot(hours[breakpoints[0][11]::], p11_trend(hours[breakpoints[0][11]::]))

fig.suptitle(plot_title)

plt.ylabel('Degrees [C]')
plt.xlabel('Time [hours]')

plt.savefig(output_plot_file, bbox_inches='tight')
