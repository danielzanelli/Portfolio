import numpy as np

class NeuralNetwork:
    def __init__(self, layers, learning_rate=0.1):
        self.W = []
        self.layers = layers
        self.learning_rate = learning_rate        
        for i in np.arange(0, len(layers) - 2):
            w = np.random.randn(layers[i] + 1, layers[i + 1] + 1)
            self.W.append(w / np.sqrt(layers[i]))
        w = np.random.randn(layers[-2] + 1, layers[-1])
        self.W.append(w / np.sqrt(layers[-2]))
        self.losses = []

    def forward(self, X):
        A = [np.atleast_2d(X)]
        for layer in np.arange(0, len(self.W)):
            net = A[layer].dot(self.W[layer])
            out = self.sigmoid(net)
            A.append(out)
        return A
    
    def backward(self, X, y, o, alpha):
        deltas = []
        error = o[-1] - y
        delta = error * self.sigmoid_derivative(o[-1])
        deltas.append(delta)        
        for layer in np.arange(len(o) - 2, 0, -1):
            delta = deltas[-1].dot(self.W[layer].T)
            delta = delta * self.sigmoid_derivative(o[layer])
            deltas.append(delta)        
        deltas = deltas[::-1]        
        for layer in np.arange(0, len(self.W)):
            self.W[layer] += -alpha * o[layer].T.dot(deltas[layer])
        
    def train(self, X, y, learning_rate = None, epochs=1000, display_update=100):
        if learning_rate is None:
            learning_rate = self.learning_rate
        X = np.c_[X, np.ones((X.shape[0]))]
        for epoch in np.arange(0, epochs):
            for (x, target) in zip(X, y):
                A = self.forward(x)
                self.backward(x, target, A, learning_rate)
            if epoch == 0 or (epoch + 1) % display_update == 0:
                self.losses.append(self.calculate_loss(X, y))
                print("[INFO] epoch={}, loss={:.7f}".format(epoch + 1, self.losses[-1]))
    
    def calculate_loss(self, X, targets):
        targets = np.atleast_2d(targets)
        predictions = self.forward(X)
        loss = 0.5 * np.sum((predictions[-1] - targets) ** 2)
        return loss
        
    def predict(self, X):
        X = np.atleast_2d(X)
        X = np.c_[X, np.ones((X.shape[0]))]
        return self.forward(X)[-1]
        
    def sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        s = self.sigmoid(x)
        return s * (1 - s)