import matplotlib.pyplot as plt


def plot_attr_imp(attribute_names, importances):
    # Show the importance of each attribute.
    plt.bar(attribute_names, importances)
    plt.title("Attribute Importance")
    plt.show()


def plot_level_part_worth(level_names, utilities):
    # Show user's preference for all levels.
    plt.bar(level_names, utilities)
    plt.title("Level Part-Worths Representing a Person’s Preferences")
    plt.xticks(rotation=80)
    plt.show()
