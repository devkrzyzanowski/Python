import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 12, 0, 10])
t = "tekst możemy rozmieszczać w oknie wykresu na różne sposoby stosując"\
    " polecenie plt.text np.4, 1, t, ha='left'"\
    "rotation=15, wrap=True"
plt.text(6, 5, t, ha='left', rotation=15, wrap=True)
plt.text(3, 1, t, ha='left', rotation=35, wrap=True)
plt.text(3, 3, t, ha='right', rotation=-15, wrap=True)
plt.text(3, 8, t, fontsize=3, style='oblique', ha='center',
         va='top', wrap=True)
plt.text(3, -7, t, family='serif', style='italic', ha='right', wrap=True)
plt.text(-3, 5, t, ha='left', rotation=-45, wrap=True)

plt.show()
