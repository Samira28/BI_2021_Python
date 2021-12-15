def sequential_map(*args):
    "интеграцию функции func_chain в 1 задание"
    return(list(map(func_chain(*args[:-1]), args[-1])))
  
def consensus_filter(*args):
  *container, numbers = args
  answer = args[-1]
  for elem in container:
    answer = list(filter(elem, answer))
  return answer
  
def conditional_reduce(reduce_func, func, nums):
    filtered = list(filter(reduce_func, nums))
    answer = filtered[0]
    for i in range(1, len(filtered)):
        answer = func(answer, filtered[i])
    return answer
  
def func_chain(*args):   # как оберточная функция
    def inside_func(value):
        answer = args[0](value)
        for i in range(1, len(args)):
            answer = args[i](answer)
        return answer
    return inside_func
  
def multiple_partial(*args, **kwargs):
    def inter_func(function, **inter_kwargs):
        def inside_func(*inside_args, **inside_kwargs):
            return function(*inside_args, **inter_kwargs, **inside_kwargs)
        return inside_func
    list_of_functions = []
    for value in args:
        inter_value = inter_func(func, **inter_kwargs)
        list_of_functions.append(inter_value)
    return list_of_functions
