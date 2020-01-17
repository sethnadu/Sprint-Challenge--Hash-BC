#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i in range(0, length): 
        hash_table_insert(ht, weights[i], i)
      
    for i in range(0, length):
        other_weight = limit - weights[i]
        if hash_table_retrieve(ht, other_weight):
            # Find higher value
            weight_index = hash_table_retrieve(ht, other_weight)
            print("answer", [weight_index, i])
            return [weight_index, i]


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# get_indices_of_item_weights([ 4, 6, 10, 15, 16 ],5, 21)
get_indices_of_item_weights([4,4], 2, 8)