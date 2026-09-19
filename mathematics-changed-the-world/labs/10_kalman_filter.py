import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
steps = 80
dt = 1.0

# State = [position, velocity].
A = np.array([[1.0, dt], [0.0, 1.0]])
H = np.array([[1.0, 0.0]])
Q = np.array([[0.02, 0.0], [0.0, 0.02]])
R = np.array([[2.0]])

true_x = np.array([0.0, 1.0])
est_x = np.array([0.0, 0.0])
P = np.eye(2) * 10.0

true_positions = []
measurements = []
estimates = []

for _ in range(steps):
    process_noise = rng.multivariate_normal(np.zeros(2), Q)
    true_x = A @ true_x + process_noise
    z = H @ true_x + rng.normal(0.0, np.sqrt(R[0, 0]), size=1)

    # Predict
    est_x = A @ est_x
    P = A @ P @ A.T + Q

    # Update
    innovation = z - H @ est_x
    S = H @ P @ H.T + R
    K = P @ H.T @ np.linalg.inv(S)
    est_x = est_x + (K @ innovation).ravel()
    P = (np.eye(2) - K @ H) @ P

    true_positions.append(true_x[0])
    measurements.append(z.item())
    estimates.append(est_x[0])

print("final estimated state [position, velocity] =", est_x)

plt.figure()
plt.plot(true_positions, label="true position")
plt.scatter(np.arange(steps), measurements, s=10, label="noisy measurement")
plt.plot(estimates, label="Kalman estimate")
plt.xlabel("time step")
plt.ylabel("position")
plt.title("Kalman filter: model prediction + measurement update")
plt.legend()
plt.tight_layout()
plt.show()
