import tensorflow as tf

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)

model.fit(X_train, y_train, epochs=5, batch_size=32)

import numpy as np

index = 300
prediction = model.predict(X_test[index].reshape(1, 784))
predicted_digit = np.argmax(prediction)

plt.imshow(X_test[index].reshape(28, 28), cmap='gray')
plt.title(f"Predicted: {predicted_digit}, Actual: {y_test[index]}")
plt.show()

