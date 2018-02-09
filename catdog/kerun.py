import numpy as np
import keras, matplotlib, seaborn, glob, os, shutil
import keras.preprocessing.image

train_datagen = keras.preprocessing.image.ImageDataGenerator()

train_generator = train_datagen.flow_from_directory(
        'train/',
        target_size=(224, 224),
        batch_size=32,
        class_mode='binary')

valid_generator = train_datagen.flow_from_directory(
        'valid/',
        target_size=(224, 224),
        batch_size=32,
        class_mode='binary')

vgg = keras.applications.vgg16.VGG16(include_top=True, weights=None, classes=1)


vgg.compile(loss=keras.losses.mean_squared_error, optimizer='sgd', metrics=['accuracy'])

vgg.fit_generator(train_generator, steps_per_epoch=328, epochs=1, verbose=3, validation_data=valid_generator, workers=3)
