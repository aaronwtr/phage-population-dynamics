import numpy as np
import output_handler as oh
import matplotlib.pyplot as plt


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})


def one_d_time_series_plotter(results, sp_type):
    if sp_type == 'B':
        specie = 'bacteria'
    elif sp_type == 'L':
        specie = 'infected bacteria'
    elif sp_type == 'P':
        specie = 'phages'
    else:
        return print('ERROR: Enter specie type (B, L or P)')


    Bt = np.transpose(results)

    tot_nums = []
    for i in range(len(Bt)):
        tot_nums.append(sum(Bt[i]))

    time_series = list(np.linspace(1, len(tot_nums), len(tot_nums)))
    time_axis = list(np.linspace(0, 1000))
    plt.semilogy(time_series, tot_nums)
    plt.xlabel('Time')
    plt.ylabel(r'Number of {} per $\mu$m$^2$'.format(specie))
    plt.xlim([0.01, len(tot_nums)])
    plt.title('Time series plot of {} population change'.format(specie))
    plt.show()

    return


Bresults = oh.read_file("results/bacteria_sim_results.txt")
Lresults = oh.read_file("results/inf_bacteria_sim_results.txt")
Presults = oh.read_file("results/phages_sim_run.txt")

one_d_time_series_plotter(Bresults, 'B')
one_d_time_series_plotter(Lresults, 'L')
one_d_time_series_plotter(Presults, 'P')

# fig, axs = plt.subplots(3)
# fig.suptitle('results over time')
plt.imshow(np.log(Bresults), cmap='viridis', aspect='auto', extent=[0, 1000, 1000, 0])
# plt.title('Bacteria')
plt.ylabel(r'Distance [$\mu$m]')
plt.xlabel('Time [s]')
# plt.show()
plt.savefig('figures/bacteria_same_end.pdf')
plt.clf()

plt.imshow(np.log(Presults), cmap='viridis', aspect='auto', extent=[0, 1000, 1000, 0])
# plt.title('Phages')
plt.ylabel(r'Distance [$\mu$m]')
plt.xlabel('Time [s]')
# plt.show()
plt.savefig('figures/phages_same_end.pdf')
plt.clf()

plt.imshow(np.log(Lresults), cmap='viridis', aspect='auto', extent=[0, 1000, 1000, 0])
# plt.title('Infected bacteria')
plt.ylabel(r'Distance [$\mu$m]')
plt.xlabel('Time [s]')
# plt.show()
plt.savefig('figures/inf_bacteria_same_end.pdf')
plt.clf()

