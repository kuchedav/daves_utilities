import os
import pickle

from . import is_equal


def fun_save(
    fun_input, attr_input={}, path="./", identifier: str = "", only_save_one=False
):
    # create hidden folder under path to save function outputs
    fun_save_path = path + ".fun_save"
    if not os.path.exists(fun_save_path):
        os.makedirs(fun_save_path)

    # add underline to identifier if it exists
    identifier = "_" + identifier if identifier else identifier

    # structure to check pas calculations
    save_structure = f"{fun_input.__name__}{identifier}"
    files_found = [
        f"{fun_save_path}/{i}" for i in os.listdir(fun_save_path) if save_structure in i
    ]

    # Warning if multiple files found while only_save_one = True
    if len(files_found) > 1 and only_save_one:
        print(
            """only_save_one is True but multiple files were found. Only the last file
            will be overwritten if not output/input combination is found."""
        )

    file_id = 0
    # open all files and compare attributes, return if same input/output is found
    for iter_path in files_found:
        # read files
        with open(iter_path, "rb") as f:
            output = pickle.load(f)

        # check if input is the same
        if is_equal.is_equal(output["attr_input"], attr_input):
            print("Function file has been found and reused: " + save_structure)
            return output["fun_output"]

        # increament id if larger
        file_id_iter = int(iter_path.split("_")[-1].replace(".pkl", ""))
        file_id = file_id_iter if file_id_iter > file_id else file_id

    # increment file_id
    if not only_save_one:
        file_id += 1
    print(
        "Input/Output combination not found => recalculating function now: "
        + save_structure
    )

    # create full file name with identifier for multiple input variations
    save_name = f"{fun_save_path}/{save_structure}_{file_id}.pkl"

    # run function
    fun_output = fun_input(**attr_input)
    output = {"attr_input": attr_input, "fun_output": fun_output}

    # save function output
    with open(save_name, "wb") as f:
        pickle.dump(output, f, protocol=4)

    return output["fun_output"]


if __name__ == "__main__":
    input_values = {"embeddings": ["tf-idf", "word2vec", "bert"]}

    # function to apply
    import time

    def concatenate_input(embeddings):
        time.sleep(1)
        return f"{embeddings}"

    output = fun_save(
        fun_input=concatenate_input,
        attr_input=input_values,
        path="./daves_utilities/data/",
        identifier="",
    )

    print(output)
