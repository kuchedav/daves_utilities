import os
import pickle
import is_equal.is_equal as is_equal

def fun_save(fun_input, attr_input, path = "./", identifier : str = ""):

    if identifier!="": identifier = "_" + identifier
    save_path = f"{path}/{fun_input.__name__}{identifier}.pkl"
    recalculate = True

    # check if output already exists
    if os.path.isfile(save_path):
        with open(save_path,"rb") as f:
            output = pickle.load(f)
        if is_equal.is_equal(output["attr_input"],attr_input):
            print("Function file has been found and reused: " + str(fun_input.__name__) + identifier)
            recalculate = False
            return output["fun_output"]
        else:
            print("File exists but input attributes are different => recalculating function now: "  + str(fun_input.__name__) + identifier)

    if recalculate:
        # run long running function
        fun_output = fun_input(**attr_input)
        output = {"attr_input":attr_input,"fun_output":fun_output}

        # save long running function
        with open(save_path,"wb") as f:
            pickle.dump(output,f,protocol=4)

        return output["fun_output"]

if __name__=="__main__":

    input_values = {"embeddings":["tf-idf","word2vec","doc2vec","bert"]}

    # function to apply
    import time
    def concatenate_input(embeddings):
        time.sleep(1)
        return f"{embeddings}"

    fun_save(fun_input = concatenate_input, attr_input = input_values)