import numpy as np

# Parameters
num_cities = 10
num_ants = 100
num_iterations = 100
alpha = 1         # Influence of pheromone
beta = 2          # Influence of distance (heuristic)
evaporation_rate = 0.1

# Initialize distance matrix (random symmetric distances)
distance_matrix = np.random.randint(1, 100, size=(num_cities, num_cities))
np.fill_diagonal(distance_matrix, 0)
# Make it symmetric (TSP is usually symmetric)
distance_matrix = (distance_matrix + distance_matrix.T) // 2

# Initialize pheromone matrix with small positive values
pheromone_matrix = np.ones((num_cities, num_cities))

best_tour = None
best_tour_length = float('inf')

# ACO algorithm
for iteration in range(num_iterations):
    all_tours = []
    all_lengths = []

    for ant in range(num_ants):
        visited = set()
        current_city = np.random.randint(num_cities)
        tour = [current_city]
        visited.add(current_city)

        while len(visited) < num_cities:
            probabilities = []
            for next_city in range(num_cities):
                if next_city in visited:
                    probabilities.append(0)
                else:
                    pheromone = pheromone_matrix[current_city][next_city] ** alpha
                    heuristic = (1 / distance_matrix[current_city][next_city]) ** beta
                    probabilities.append(pheromone * heuristic)

            probabilities = np.array(probabilities)
            probabilities /= probabilities.sum()
            next_city = np.random.choice(range(num_cities), p=probabilities)
            tour.append(next_city)
            visited.add(next_city)
            current_city = next_city

        # Return to starting city to complete the tour
        tour.append(tour[0])

        # Calculate tour length
        tour_length = sum(
            distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)
        )

        all_tours.append(tour)
        all_lengths.append(tour_length)

        # Update pheromones on the tour
        for i in range(len(tour) - 1):
            from_city = tour[i]
            to_city = tour[i + 1]
            pheromone_matrix[from_city][to_city] += 1 / tour_length
            pheromone_matrix[to_city][from_city] += 1 / tour_length  # symmetric

        # Track the best tour
        if tour_length < best_tour_length:
            best_tour_length = tour_length
            best_tour = tour

    # Evaporate pheromones
    pheromone_matrix *= (1 - evaporation_rate)

# Output the best tour
print("Best tour found:", best_tour)
print("Best tour length:", best_tour_length)

