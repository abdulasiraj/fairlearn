# Copyright (c) Fairlearn Contributors.
# Licensed under the MIT License.

from pathlib import Path

from sklearn.datasets import fetch_openml
from ._constants import _DOWNLOAD_DIRECTORY_NAME
import fairlearn.utils._compatibility as compat


def fetch_credit_card(
    *, cache=True, data_home=None, as_frame=False, return_X_y=False
):
    """Load the 'Default of Credit Card clients' dataset (binary classification).

    ===============   ===============
    Samples total               30000
    Dimensionality                 24
    Features                     real
    Classes                         2
    ===============   ===============

    Source: https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients
    I-Cheng Yeh and Che-hui Lien, "The comparisons of data mining techniques for the
    predictive accuracy of probability of default of credit card clients", Expert Systems
    with Applications, 36(2), 2473-2480, 2009

    Parameters
    ----------
    cache : boolean, default=True
        Whether to cache downloaded datasets using joblib

    data_home : optional, default: None
        Specifiy another download and cache folder for the datasets. By default,
        all scikit-learn data is stored in '~/.fairlearn-data' subfolders.

    as_frame : boolean, default=False
        If True,
            Returns the data as Pandas DataFrame, and the target
            is returned as a Pandas Series.
        If False,
            Returns a scikit-learn Bunch object with ``frame`` attribute containing
            the data and the target.


    return_X_y : boolean, default=False.
        If True,
            returns ``(data.data, data.target)``
        Else,
            return Sci-kit Learn Bunch object


    Returns
    -------
    dataset : class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : NumPy Array or Pandas DataFrame, Shape (30000, 24)
            Each row corresponds to the 24 feature values in order.
            If ``as_frame`` is True, ``data`` is a Pandas DataFrame
        target : NumPy Array or Pandas Series, Shape (30000,)
            Each value represents whether an applicant defaulted on credit loan.
            If ``as_frame`` is True, ``target`` is a Pandas Series.
        feature_names : List of Strings, Length 24
            Array of ordered feature names used in the dataset.
        DESCR : string
            Description of the UCI Default of Credit Card

    """
    if not data_home:
        data_home = Path().home() / _DOWNLOAD_DIRECTORY_NAME

    return fetch_openml(
        data_id=42477,
        data_home=data_home,
        cache=cache,
        as_frame=as_frame,
        return_X_y=return_X_y,
        **compat._PARSER_KWARG,
    )
