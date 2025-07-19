from sklearn.model_selection import train_test_split

# Assuming your preprocessed features are in 'X' and labels in 'y'
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2,  # 80% training, 20% test
    random_state=42,  # For reproducibility
    stratify=y  # Maintains class distribution
)

print("Training set shape:", X_train.shape, y_train.shape)
print("Test set shape:", X_test.shape, y_test.shape)