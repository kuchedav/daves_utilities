import itertools
import os
import re
import shutil
from os import listdir
from pathlib import Path

import pandas as pd
from progressbar import progressbar  # pip install progressbar2


def for_long(iter_fun, iter_attr, save_every_n=10, path="./"):  # noqa
    """
    for_long facilitates iterating over long running loops.

    following functionalities are implemented:
    - save progress in folder
    - start from last saved progress
    - run over combination of input lists
    - get show loading bar

    iter_fun:       function to iterate over
    iter_attr:      a dictionary of all attributes needed for iter_fun input.
                    => {"attribute name 1":attribute_values1,
                        "attribute name 2":attribute_values2, ...}
                    for the loop to create a permutation you can enter one or more
                        attributes as a list.
                    => {"attribute name 1":[1,2,3,4], "attribute name 2":
                        ["EU","CH","AM"], ...}
                    attributes with lists can be combined with attributes with a
                        single value.
    save_every_n:   save my progress every n iterations
    path:           save my files under this path
    """

    # extract combinations
    combination_values = {j: i for j, i in iter_attr.items() if isinstance(i, list)}
    static_values = {j: i for j, i in iter_attr.items() if not isinstance(i, list)}
    # create combination
    value_combination = list(itertools.product(*list(combination_values.values())))

    # create dict from all combinations to input into function
    iter_input = [dict(zip(combination_values.keys(), i)) for i in value_combination]

    # define path for backup files
    path_backup = f"{path}for_long_{iter_fun.__name__}"

    # check for precalcuated combinations
    end_file_path = f"{path}/{iter_fun.__name__}_end.csv"
    counter = 0
    if os.path.isfile(end_file_path):
        # load las calculated end file
        print(f"Finsihed file {end_file_path} has been found")
        df_out = pd.read_csv(end_file_path)
    elif os.path.exists(path_backup):
        # find file with highest iter backup number
        print(f"Started backup files {path_backup} have been found")
        for i in listdir(path_backup):
            m = re.search(rf"{iter_fun.__name__}_(\d*).csv", i)
            if m and int(m.group(1)) > counter:
                counter = int(m.group(1))
        df_out = pd.read_csv(f"{path_backup}/{iter_fun.__name__}_{str(counter)}.csv")
    else:
        # create new empty data frame
        print("No precalculated data has been found for " + str(iter_fun.__name__))
        df_out = pd.DataFrame(columns=[*iter_input[0], *static_values, "output"])

    [i.update(static_values) for i in iter_input]

    # remove entries from iter_input which have already been calculated
    df_in = pd.DataFrame(iter_input)
    if len(df_in.columns) == len(df_out.columns) - 1:
        df_limited = df_in[~df_in.isin(df_out)].dropna()
        iter_attributes = df_limited.to_dict("records")
    else:
        print(
            """Number of attributes for the functions have changed. Function will run
                again over all combinations and append results."""
        )

    def iter_function(iter_in, static_values, df_out, counter):
        # run function
        iter_out = iter_fun(**iter_in, **static_values)

        # append output
        df_out = df_out.append(
            {**iter_in, **static_values, "output": iter_out}, ignore_index=True
        )

        # save output every n iterations
        if counter % save_every_n == 0 and counter != 0:
            # create folder for backup storage of files
            Path(f"{path}for_long_{iter_fun.__name__}").mkdir(
                parents=True, exist_ok=True
            )
            # write backup file to directory
            df_out.to_csv(
                f"{path_backup}/{iter_fun.__name__}_{counter}.csv", index=False
            )

        counter += 1

        return df_out

    # iterate over function
    for iter_in in progressbar(iter_attributes):
        df_out = df_out.append(iter_function(iter_in, static_values, df_out, counter))

    # save last data frame END
    df_out.to_csv(f"{path}/{iter_fun.__name__}_end.csv", index=False)

    # remove backup during calculation
    try:
        shutil.rmtree(path_backup)
    except:  # noqa
        pass

    return df_out


if __name__ == "__main__":
    # create input
    embeddings = ["tf-idf", "word2vec", "doc2vec", "bert"]
    embeddings_dim = [10, 20, 40, 100, 500, 1000]
    range_attr = list(range(0, 10))
    # combination
    attribute_dict = {
        "embeddings": embeddings,
        "embeddings_dim": embeddings_dim,
        "verbose": True,
        "quick_calc": False,
        "range_attr": range_attr,
    }

    # function to apply
    import time

    def concatenate_input(
        embeddings, embeddings_dim, verbose, quick_calc, range_attr=0
    ):
        time.sleep(0.01)
        return f"{embeddings} {str(embeddings_dim)} {verbose} {quick_calc} {range_attr}"

    df_out = for_long(iter_fun=concatenate_input, iter_attr=attribute_dict)
