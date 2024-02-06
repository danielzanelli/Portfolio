from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import numpy as np

from neural_network import NeuralNetwork


#################### HYPERPARAMETERS ########################

# Dataset parameters
clusters = 4
features = 3
datapoints = 1000

# Model parameters
hidden_layers = [5, 15, 10]

# Training parameters
epochs = 1000
learning_rate = 0.1

# Other
display_update = 100
plot = True
savefigure = True

############################################################


# Generate a classification problem
(X, y) = make_blobs(n_samples=datapoints, n_features=features, centers=clusters, cluster_std=1.5, random_state=1)
y = y.reshape((y.shape[0], 1))

# One-hot encode the labels
ohe = OneHotEncoder()
y = ohe.fit_transform(y).toarray()

# Split the data into training and testing
(trainX, testX, trainY, testY) = train_test_split(X, y, test_size=0.5, random_state=42)

# Initialize the network
nn = NeuralNetwork([features] + hidden_layers + [clusters])

print("[INFO] Initializing benchmark test with hyperparameters:\n\n\t"
        f"- clusters: \t\t{clusters}\n\t"
        f"- features: \t\t{features}\n\t"
        f"- datapoints: \t\t{datapoints}\n\t"
        f"- hidden layers: \t{hidden_layers}\n\t"
        f"- epochs: \t\t{epochs}\n\t"
        f"- learning rate: \t{learning_rate}\n\t"
        f"- display update: \t{display_update}\n\t"
        f"- plot: \t\t{plot}\n\t"
        f"- save figure: \t\t{savefigure}\n")

# Train the network
print("[INFO] Training network...")
nn.train(trainX, trainY, learning_rate=learning_rate, epochs=epochs)

# Test the network to find accuracy
print("[INFO] Testing network...")
predictions = nn.predict(testX)
predictions = predictions.argmax(axis=1)
testY = testY.argmax(axis=1)
accuracy = np.mean(predictions == testY)

# Show the accuracy on the testing set
print("[INFO] Final test accuracy: {:.2f}%".format(100 * accuracy))

# Plot the losses
plt.figure()
plt.plot(np.linspace(0, epochs, len(nn.losses)),nn.losses)
plt.title("Training Loss")
plt.xlabel("Epoch #")
plt.ylabel("Loss")
plt.grid()

if savefigure:
    plt.savefig("benchmark_loss.png")

if plot:
    plt.show()
