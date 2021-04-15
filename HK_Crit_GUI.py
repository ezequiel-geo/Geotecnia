from tkinter import *
from PIL import ImageTk, Image
import numpy
import pandas
import matplotlib

root = Tk()
root.title("Criterio Hoek-Brown y GSI")

#Ejemplo de cálculo, adaptar el GUI.
def hoek_brown(min_sig3, max_sig3, num_values):
    sig3 = np.linspace(min_sig3, max_sig3, num_values, endpoint=True)
    sig1 = sig3 + sigci * ((mb * (sig3/sigci))+s)**a
    sig_array = pd.DataFrame(data=np.vstack([sig3, sig1]).T, columns=['sig3', 'sig1'])

    sig_array['ds1ds3'] = 1+a*mb*(mb*(sig3/sigci)+s)**(a-1)
    sig_array['sign'] = ((sig1 + sig3)/2) - ((sig1 - sig3)/2) * (sig_array['ds1ds3'] - 1) / (sig_array['ds1ds3'] + 1)
    sig_array['tau'] = (sig1-sig3)*np.sqrt(sig_array['ds1ds3'])/(sig_array['ds1ds3']+1)

    return sig_array

  # Plot
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(121)

sig1_formula = r'\sigma_1^{´}=\sigma_3^{´} + \sigma_{ci} \
            \times (m_b \times \frac{\sigma_3^{´}}{\sigma_{ci}} + s)^a'


ax.plot(sig_array.sig3.values, sig_array.sig1.values, 'bo-',
        label='Hoek-Brown: ' + sig1_formula.join(r'$$')); 
ax.set_xlabel(u'Principal Stress, $\sigma_3$, MPa', fontsize=12)
ax.set_ylabel(u'Principal Stress, $\sigma_1$, MPa', fontsize=12)

ax.grid(); ax.legend(fontsize='x-large')

ax = fig.add_subplot(122)

tau_formula = r'\tau^{´} = (\sigma_1^{´} - \sigma_3^{´}) \
             \frac{\sqrt{d\sigma_1^{´}/d\sigma_3^{´}}}{d\sigma_1^{´}/d\sigma_3^{´} + 1}'

ax.plot(sig_array['sign'], sig_array['tau'], 'bo-',
    label='Hoek-Brown: ' + tau_formula.join(r'$$'))
ax.set_xlabel(u'Normal Stress, $\sigma_n$, MPa', fontsize=12)
ax.set_ylabel(u'Shear Stress, $\u03C4$, MPa', fontsize=12)

# Add Mohr circles for the invervals that were defined above.

centers = ((sig_array.sig1.values - sig_array.sig3.values) / 2) + sig_array.sig3.values
radius = sig_array.sig1.values - centers

for r, c in zip(radius, centers):
    ax.add_patch(plt.Circle([c, 0], r, facecolor='none', ec='k', alpha=.2))

ax.grid()
ax.set_aspect('equal')
ax.legend(fontsize='large')

fig.suptitle('Hoek-Brown Failure Criteria', fontsize=20, y=1.05)
fig.tight_layout(pad=1.5)
fig.savefig('./images/9/7.png', dpi=200)

root.mainloop()
