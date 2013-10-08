from matplotlib.pyplot import figure, show, xkcd

xkcd()
fig = figure(1, figsize=(8,5))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 5), ylim=(-3, 3))
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
line, = ax.plot(range(6), [0]*6, lw=3, color='purple')
ax.set_title("Why we do this?")
ax.annotate('', xy=(0.3, 0.3), xycoords='data', xytext=(1.2, 0.3),
        textcoords='data', arrowprops=dict(arrowstyle="<->",
                                            connectionstyle="bar",
                                            ec="k",
                                            shrinkA=5, shrinkB=5,))

ax.annotate('', xy=(1.5, 0.3), xycoords='data', xytext=(3.5, 0.3),
        textcoords='data', arrowprops=dict(arrowstyle="<->",
                                            connectionstyle="bar",
                                            ec="k",
                                            shrinkA=5, shrinkB=5,))

ax.annotate('Dummy', xy=(.5, -0.5), xycoords='data', xytext=(-50, 30),
        textcoords='offset points', bbox=dict(boxstyle="round", fc="0.8"),
        arrowprops=None)

ax.annotate('Newbie', xy=(1.5, -0.5), xycoords='data', xytext=(-50, 30),
        textcoords='offset points', bbox=dict(boxstyle="round", fc="0.8"),
        arrowprops=None)

ax.annotate('Advanced newbie', xy=(3.5, -0.5), xycoords='data',
        xytext=(-50, 30), textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.8"),
        arrowprops=None)

ax.annotate('Software\ncarpentry', xy=(0.8, .7), xycoords='data',
        xytext=(-50, 30), textcoords='offset points', arrowprops=None)

ax.annotate('??? (Google, Stackoverflow, Biostar, etc.)', xy=(2, 1.5), xycoords='data',
        xytext=(-50, 30), textcoords='offset points', arrowprops=None)

show()
