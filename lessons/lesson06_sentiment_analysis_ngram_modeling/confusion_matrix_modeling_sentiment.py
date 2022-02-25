import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from pandas import DataFrame


# Draw the confusion matrix.
def showFormattedConfusionMatrix(y_test, y_predicted):
    # You can print a simple confusion matrix with no formatting – this is easiest.
    cm = metrics.confusion_matrix(y_test.values, y_predicted)
    print(cm)

    # For readability I have taken steps to output the confusion matrix
    # in a nicely formatted manner. You do not need to take this step.

    # Show confusion matrix with colored background.
    Index = ['Actual Awful', 'Poor', 'Neutral', 'Good', 'Excellent']
    Cols = ['Pred Awful', 'Pred Poor', 'Pred Neutral', 'Pred Good',
            'Pred Excellent']
    df = DataFrame(cm, index=Index, columns=Cols)
    plt.figure(figsize=(4, 4))

    ax = sns.heatmap(df, cmap='Blues', annot=True, fmt='g')
    bottom, top = ax.get_ylim()
    ax.set(title="Movie Review Sentiment")
    ax.set_ylim(bottom + 0.5, top - 0.5)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30,
                       horizontalalignment='right')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0,
                       horizontalalignment='right')


showFormattedConfusionMatrix(y_test, y_predicted)
