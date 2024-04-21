import json
import matplotlib.pyplot as plt

# Initialize lists to store metrics
train_losses = []
val_losses = []
epochs = []

# Read the log file
with open('outputs_2/log.txt', 'r') as file:
    for line in file:
        data = json.loads(line)
        # Extract relevant metrics for each epoch
        epoch = data['epoch']
        train_loss = data['train_loss_bbox']
        val_loss = data['test_loss_bbox']
        # Append metrics to lists
        epochs.append(epoch)
        train_losses.append(train_loss)
        val_losses.append(val_loss)

# Plotting
plt.figure(figsize=(10, 5))

# Plot train and validation loss
plt.plot(epochs, train_losses, label='Train Loss')
plt.plot(epochs, val_losses, label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Train and Validation Loss')
plt.legend()

plt.show()
