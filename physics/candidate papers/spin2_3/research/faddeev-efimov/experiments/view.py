import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.patches as patches

# ======================  YOUR GEOMETRIC MODEL (stable) ======================
def two_branch_step(R, rho, Phi, kappa_u, gamma, omega, dt=0.02):
    rho = np.clip(rho, -5.0, 5.0)
    kappa_eff = kappa_u * np.cosh(2 * rho)
    kappa_eff = np.clip(kappa_eff, -100, 100)
    
    dR = R * (-gamma + kappa_eff * np.cos(Phi))
    drho = -kappa_eff * np.sin(Phi)
    dPhi = 2 * omega - 2 * kappa_eff * np.sin(Phi)
    return R + dR * dt, rho + drho * dt, Phi + dPhi * dt

def collective_eigenvalue(rho, delta_base=-1.2625):
    return delta_base + 0.3 * np.tanh(2 * rho)

# ======================  ATOMS  ======================
class Atom:
    def __init__(self, x, y, label, color='blue'):
        self.pos = np.array([x, y], dtype=float)
        self.label = label
        self.color = color
        self.radius = 0.15

atoms = [
    Atom(0.0, 0.0, "e1", "blue"),
    Atom(1.2, 0.0, "p", "red"),
    Atom(2.5, 0.0, "e2", "blue"),
]

# ======================  FIGURE  ======================
fig, ax = plt.subplots(figsize=(11, 7))
plt.subplots_adjust(left=0.1, bottom=0.35)

ax.set_xlim(-1, 5)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
#ax.set_title("Spin(2,3) Geometric Toy — Drag atoms, watch lines & coherence", fontsize=14)

circles = []
texts = []
for atom in atoms:
    circ = patches.Circle(atom.pos, atom.radius, color=atom.color, alpha=0.9)
    ax.add_patch(circ)
    circles.append(circ)
    txt = ax.text(atom.pos[0], atom.pos[1], atom.label, ha='center', va='center', color='white', fontsize=11)
    texts.append(txt)

coherence_text = ax.text(0.05, 1.85, "Coherence: --", fontsize=13, color='black')

# Sliders
ax_kappa = plt.axes([0.15, 0.22, 0.65, 0.03])
s_kappa = Slider(ax_kappa, 'κ_u (pairing strength)', -2.0, 2.0, valinit=1.2)

ax_gamma = plt.axes([0.15, 0.17, 0.65, 0.03])
s_gamma = Slider(ax_gamma, 'γ (T2 leakage / temperature)', 0.0, 2.0, valinit=0.3)

ax_omega = plt.axes([0.15, 0.12, 0.65, 0.03])
s_omega = Slider(ax_omega, 'ω (transport frequency)', 0.0, 5.0, valinit=1.0)

# Reset button
reset_ax = plt.axes([0.82, 0.03, 0.12, 0.05])
btn_reset = Button(reset_ax, 'Reset')

# Simulation state
R, rho, Phi = 1.0, 0.0, 0.0
t = 0.0
dt = 0.02

# Line objects (will be updated dynamically)
lines = []

def update_plot():
    global R, rho, Phi, t, lines
    kappa_u = s_kappa.val
    gamma = s_gamma.val
    omega = s_omega.val
    
    R, rho, Phi = two_branch_step(R, rho, Phi, kappa_u, gamma, omega, dt)
    t += dt
    delta = collective_eigenvalue(rho)
    
    # Clear old lines
    for line in lines:
        line.remove()
    lines.clear()
    
    # Draw new interaction lines
    for i in range(len(atoms)):
        for j in range(i+1, len(atoms)):
            dist = np.linalg.norm(atoms[i].pos - atoms[j].pos)
            if dist < 2.0:
                # Line color based on coherence
                if kappa_u > 0 and abs(kappa_u * np.cosh(2*rho) * np.cos(Phi)) > gamma:
                    col = 'lime'
                    lw = 3.0
                elif abs(delta) > 1.0:
                    col = 'orange'
                    lw = 2.5
                else:
                    col = 'red'
                    lw = 1.5
                
                line = ax.plot([atoms[i].pos[0], atoms[j].pos[0]],
                               [atoms[i].pos[1], atoms[j].pos[1]],
                               color=col, lw=lw, alpha=0.7)[0]
                lines.append(line)
    
    # Visual feedback
    if kappa_u > 0 and abs(kappa_u * np.cosh(2*rho) * np.cos(Phi)) > gamma:
        status = "LOCKED (constructive pairing)"
        col = 'lime'
    elif abs(delta) > 1.0:
        status = "Efimov-like three-body cluster"
        col = 'orange'
    else:
        status = "Dephased / normal"
        col = 'red'
    
    coherence_text.set_text(f"Coherence: {status}\nΔ(ρ) = {delta:.3f}")
    coherence_text.set_color(col)
    
    # Three-body highlight
    d1 = np.linalg.norm(atoms[1].pos - atoms[0].pos)
    d2 = np.linalg.norm(atoms[1].pos - atoms[2].pos)
    if d1 < 1.3 and d2 < 1.3:
        coherence_text.set_text(coherence_text.get_text() + "\n← THREE-BODY MODE ACTIVE")
    
    fig.canvas.draw_idle()

# Dragging
dragging = None

def on_press(event):
    global dragging
    if event.inaxes != ax: return
    for i, atom in enumerate(atoms):
        if np.linalg.norm(atom.pos - np.array([event.xdata, event.ydata])) < 0.4:
            dragging = i
            return

def on_release(event):
    global dragging
    dragging = None
    update_plot()

def on_motion(event):
    global dragging
    if dragging is None or event.inaxes != ax: return
    atoms[dragging].pos[:] = [event.xdata, event.ydata]
    circles[dragging].center = atoms[dragging].pos
    texts[dragging].set_position(atoms[dragging].pos)
    update_plot()

fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)

def slider_update(val):
    update_plot()

s_kappa.on_changed(slider_update)
s_gamma.on_changed(slider_update)
s_omega.on_changed(slider_update)

btn_reset.on_clicked(lambda x: [setattr(a, 'pos', np.array([i*1.2, 0.0])) for i,a in enumerate(atoms)] or update_plot())

update_plot()
plt.show()