from memory_profiler import memory_usage

def measure_memory(exec_function, parameters):
    return memory_usage((exec_function, (parameters, )), max_usage=True)
