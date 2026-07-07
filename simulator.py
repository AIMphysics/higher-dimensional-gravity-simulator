import numpy as np
import matplotlib.pyplot as plt

# Variables G for gravity, M for mass, delta time = time between calculation frames, main loop executes 1500 times
G, M, dt, STEPS = 1.0, 1000.0, 0.01, 1500

pos = np.array([10.0, 0.0, 2.0, 1.0])
vel = np.array([0.0, 6.0, 0.2, 0.1])
N = len(pos)

x_history, y_history, z_history = [], [], []

for step in range (STEPS):
     # Pythagorean theorem sqrt (x^2 + y^2 + z^2 +w^2)
    r_mag = np.linalg.norm(pos)
    # If planet is too close to the star, it will crash
    if r_mag < 0.1:
        break
    # Gravity follows an inverse cube law, so we divide by r^4. This calulates
    # how hard star is pulling on the planet on all 4 axes
    acc = -G * M * pos / (r_mag ** N)
    # Euler Integration
    vel += acc * dt
    pos += vel * dt
    # We can only graph 3D
    x_history.append(pos[0])
    y_history.append(pos[1])
    z_history.append(pos[2])
    if step % 150 == 0:
        print(f"Step {step:4d} | 4D Position : {np.round(pos, 2)} | Distance: {r_mag: .2f} ")

fig = plt.figure() # Makes a "blank 3D canvas"
ax = fig.add_subplot(projection='3d')

ax.plot(x_history, y_history, z_history, color = 'blue') # Can see each coordinate planet visited
ax.scatter(0, 0, 0, color = 'red', s = 150) # Represents the sun
plt.savefig('orbit_plot.png')