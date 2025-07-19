import tensorflow as tf
from tensorflow_model_optimization.sparsity.keras import prune_low_magnitude

# Load the pre-trained model
model = tf.keras.models.load_model('sentiment_model.h5')

# Define the pruning parameters
pruning_params = {
    'pruning_schedule': tf.keras.optimizers.schedules.PolynomialDecay(
        initial_learning_rate=0.001,
        decay_steps=1000,
        end_learning_rate=0.0001
    )
}

# Apply pruning to the model
pruned_model = prune_low_magnitude(model, **pruning_params)

# Compile the pruned model
pruned_model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# Continue training the pruned model to adjust to the pruned weights
pruned_model.fit(X_train, y_train, epochs=5, validation_data=(X_val, y_val))

# Strip the pruning wrappers to get the final pruned model
pruned_model = tf.keras.models.Model(pruned_model.input, pruned_model.output)
