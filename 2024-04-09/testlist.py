from random import randrange
from listutils import selection_sort, is_ascending_1, is_ascending_2
from time import perf_counter_ns


if __name__ == '__main__':
    LIST_LENGTH = 1000

    ## Experiment with the is_ascending_* functions
    #seq = list(range(10, LIST_LENGTH, 10))
    ##print(seq)

    ## Measure the time is_ascending_1 takes to execute
    #start = perf_counter_ns()
    #x = is_ascending_1(seq)
    #stop = perf_counter_ns()
    #print((stop - start)/1e9)

    ## Measure the time is_ascending_2 takes to execute
    #start = perf_counter_ns()
    #x = is_ascending_2(seq)
    #stop = perf_counter_ns()
    #print((stop - start)/1e9)


    seq = [randrange(501) for x in range(LIST_LENGTH)]
    # print(seq)
    print('-----------------------------------')
    selection_sort(seq)
    # print(seq)
    print('Is the list sorted?', is_ascending_2(seq))

