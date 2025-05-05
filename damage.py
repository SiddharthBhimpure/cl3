import numpy as np

# Simulated structure data (2 features): [vibration, temperature]
normal_data = np.array([[0.1, 0.2], [0.15, 0.25], [0.12, 0.22]])
test_data = np.array([[0.14, 0.23], [0.5, 0.6]])  # First is normal, second is damaged

# Detector generation (random vectors that don't match normal data)
def generate_detectors(normal_data, num_detectors=5, radius=0.1):
    detectors = []
    while len(detectors) < num_detectors:
        candidate = np.random.rand(2)  # 2D random detector
        if all(np.linalg.norm(candidate - n) > radius for n in normal_data):
            detectors.append(candidate)
    return np.array(detectors)

# Classification: If any detector matches (within radius), label as damaged (1), else undamaged (0)
def classify(data, detectors, radius=0.1):
    predictions = []
    for point in data:
        if any(np.linalg.norm(point - d) < radius for d in detectors):
            predictions.append(1)  # Damaged
        else:
            predictions.append(0)  # Normal
    return predictions

# Train
detectors = generate_detectors(normal_data)

# Test
predictions = classify(test_data, detectors)

print("Predictions (0: normal, 1: damaged):", predictions)
