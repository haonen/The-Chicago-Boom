def get_all_dummies(X_train, X_test, colname):
    '''
    Convert the categorical variable into dummies
    Inputs:
        X_train: a data frame of training set
        X_test: a data frame of test set
        colname: the name of the colname
    Return:
        the data frame with those dummies into data frame
    '''
    # Get the categories from training data set
    cat_list = list(X_train[colname].value_counts().index.values)
    # create dummies
    for cat in cat_list:
        X_test[cat] = np.where(X_test[colname] == cat, 1, 0)
        X_train[cat] = np.where(X_train[colname] == cat, 1, 0)


def get_top_k_dummies(X_train, X_test, colname, k):
    '''
    For columns with too many categories, only create dummies for
    top k categories
    Inputs:
        X_train: a data frame of training set
        X_test: a data frame of test set
        colname: the name of the column
        k: (int) the value of k
    Outputs:
       Create dummies in both train and test set
    '''
    # get top k categories from tarin set
    top_k = X_train[colname].value_counts()[:k].index
    # create dummies
    for cat in top_k:
        X_train[cat] = np.where(X_train[colname] == cat, 1, 0)
        X_test[cat] = np.where(X_test[colname] == cat, 1, 0)
    X_train['{}_others'.format(colname)] = X_train.apply(
        lambda x: 0 if x[colname] in top_k else 1, axis=1)
    X_test['{}_others'.format(colname)] = X_test.apply(
        lambda x: 0 if x[colname] in top_k else 1, axis=1)


def get_dummies(X_train, X_test, colname, k):
    '''
    Wrap up get_all_dummies and get_top_k_dummies
    Inputs:
        X_train: a data frame of training set
        X_test: a data frame of test set
        colname: the name of the column
        k: (int) the value of k
    Outputs:
       Create dummies in both train and test set
    '''
    # Decide whether this use get all dummies or top k
    if len(X_train[colname].value_counts()) > k:
        get_top_k_dummies(X_train, X_test, colname, k)
    else:
        get_all_dummies(X_train, X_test, colname)