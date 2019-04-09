import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import numpy as np

class Plot:
    def plot_confusion_matrix(self, y_test, y_pred, labels, clf):
        cm = confusion_matrix(y_test, y_pred)

        ticks = np.linspace(0, 49, num=50)
        plt.imshow(cm, interpolation='none')
        plt.colorbar()
        plt.xticks(ticks, labels, fontsize=6)
        plt.yticks(ticks, labels, fontsize=6)
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.grid(True)
        plt.title("Unnormalized confusion matrix of "+clf)
        plt.show()