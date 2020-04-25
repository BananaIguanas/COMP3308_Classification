from sys import exit


if __name__ == "__main__":
    training = None
    mode = None
    folds = None
    k_value = None
    total = 0

    try:
        training = input("Name of the training file: ")
        folds = int(input("Number of folds: "))
        mode = input("Algorithm to run: ")

        if mode != "NN" or mode != "NB":
            raise Exception

        if mode == "NN":
            k_value = int(input("K value for Nearest Neighbour: "))
    except:
        print("Invalid Arguments. Algorithm must be NN or NB. Folds and K value must be an integer.")
        exit()

    for i in range(folds):
        # Run the evaluator.

    print(f"Average accuracy of {folds} folds: {total/folds}%")
        


    

