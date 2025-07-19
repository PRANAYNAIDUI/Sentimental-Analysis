# Import necessary modules
import tensorflow as tf
import tensorflow_addons as tfa

# Define the loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(
    from_logits=True,
    reduction=tf.keras.losses.Reduction.SUM_OVER_BATCH_SIZE
)

# Define the optimizer
optimizer = tf.keras.optimizers.Adam(
    learning_rate=0.001,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-7
)

# Define the evaluation metrics
metrics = [
    tf.keras.metrics.SparseCategoricalAccuracy(name='accuracy'),
    tf.keras.metrics.SparseCategoricalPrecision(name='precision'),
    tf.keras.metrics.SparseCategoricalRecall(name='recall'),
    tfa.metrics.F1Score(name='f1_score', average='macro')
]

# Compile the model
model.compile(
    optimizer=optimizer,
    loss=loss_fn,
    metrics=metrics
)