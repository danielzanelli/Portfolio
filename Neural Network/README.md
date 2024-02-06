# Neural Network Project

This is a simple multi layered perceptron structure for a neural network using only `numpy`.

## Features

- Allows for an arbitrary amount of input and output sizes.
- Allows for an arbitrary number of hidden layers of any size.
- This neural network was made without any deep learning libraries.
- Backpropagation algorithm implemented manually through `numpy`.
- Test dataset was obtained from `scikit-learn`.

## Usage

1. Clone this repository.
2. Install the requirements with `pip install numpy scikit-learn matplotlib`.
3. Modify hyperparameters in the `benchmark.py` file. (optional)
4. Run `python benchmark.py` to start training and testing.

## Dataset

The training and testing dataset was obtained from the `make_blobs` method from the `scikit-learn` library, which generates an arbitrary amount of datapoints belonging to clusters. 
The caracteristics of this cluster data can be modified by changing the hyperparameters at the top of the `benchmark.py` file.
As an example, in the following figure we can see a dataset of `1000` datapoints, with `2` features, conforming `3` clusters.

![Dataset](https://github.com/danielzanelli/Portfolio/assets/83187517/15af20f9-42a3-431b-8b7a-22f6d3515fd0)

## Hyperparameters

- Clusters: 		Number of clusters in the dataset
- Features: 		Number of features in the dataset
- Datapoints: 		Number of datapoints in the dataset
- Hidden Layers: 	List of number of sizes of each of the hidden layers (eg. [4, 16, 32, 16, 4])
- Epochs: 		Number of training epochs
- Learning rate: 	Learning rate of training
- Plot: 		Boolean to plot training results
- Display Update: 	Number of epochs elapsed before progress is displayed
- Save Figure: 		Boolean to save training results into image

## Results

After running `python benchmark.py`, here is the typical output:

  	[INFO] Initializing benchmark with hyperparameters:

	  - clusters: 		4
	  - features: 		3
	  - datapoints: 	1000
	  - hidden layers: 	[5, 15, 10]
	  - epochs: 		1000
	  - learning rate: 	0.1
	  - plot: 		True
	  - display update: 	100
	  - save figure: 	True

	[INFO] Training network...
	[INFO] epoch=1, loss=186.2118808
	[INFO] epoch=100, loss=57.3403134
	[INFO] epoch=200, loss=22.7830419
	[INFO] epoch=300, loss=31.0263420
	[INFO] epoch=400, loss=30.4058605
	[INFO] epoch=500, loss=56.9841132
	[INFO] epoch=600, loss=34.8120568
	[INFO] epoch=700, loss=44.6387492
	[INFO] epoch=800, loss=67.8145591
	[INFO] epoch=900, loss=56.9760014
	[INFO] epoch=1000, loss=37.6635601
	[INFO] Testing network...
	[INFO] Final test accuracy: 91.40%

Results vary depending on the hyperparameters used. Nevertheless, the highest accuracy can be achieved by having a number of features greater than the number of clusters.
The training results from the previous run can be seen in the following image:

![Training results](https://github.com/danielzanelli/Portfolio/blob/main/Neural%20Network/benchmark_loss.png)
