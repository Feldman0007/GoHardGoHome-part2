import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

np.random.seed(123)
X = np.load('../generated_games/features.npy')
Y = np.load('../generated_games/labels.npy')

samples = X.shape[0]
size = 9
input_shape = (size, size, 1)

X = X.reshape(samples, size, size, 1)

train_samples = int(0.9 * samples)
X_train, X_test = X[:train_samples], X[train_samples:]
Y_train, Y_test = Y[:train_samples], Y[train_samples:]


model = Sequential()
model.add(Conv2D(48, kernel_size=(3, 3),
    activation='relu',
    padding='same',
    input_shape=input_shape))

model.add(Dropout(rate=0.5))
model.add(Conv2D(48, (3, 3),
    padding='same', activation='relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(rate=0.5))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(rate=0.5))
model.add(Dense(size * size, activation='softmax'))
model.summary()
model.compile(loss='categorical_crossentropy',
    optimizer='sgd',
    metrics=['accuracy'])