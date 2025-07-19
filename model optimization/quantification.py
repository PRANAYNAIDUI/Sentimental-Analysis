# Convert the pruned model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(pruned_model)
tflite_model = converter.convert()

# Save the quantized model
with open('sentiment_model_quantized.tflite', 'wb') as f:
    f.write(tflite_model)
