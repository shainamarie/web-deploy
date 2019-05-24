import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
n = 5
milan= (73, 43, 44, 70, 61)
inter = (54, 59, 69, 46, 58)
juventus = (65, 65, 74, 54, 71)
fig, ax = plt.subplots()
index = np.arange(n)
bar_width = 0.3
opacity = 0.9
ax.bar(index, milan, bar_width, alpha=opacity, color='r',
                label='Milan')
ax.bar(index+bar_width, inter, bar_width, alpha=opacity, color='b',
                label='Inter')
ax.bar(index+2*bar_width, juventus, bar_width, alpha=opacity,
	color='k', label='Juventus')
ax.set_xlabel('Seasons')
ax.set_ylabel('Points')
ax.set_title('Milan v/s Inter v/s Juventus')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(('1995-96','1996-97','1997-98','1998-99','1999-00'
    ))
ax.legend(ncol=3)
plt.show()