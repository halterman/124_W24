from time import perf_counter_ns


class Stopwatch:
    def __init__(self) -> None:
        self.reset()

    def start(self) -> None:
        self.start_time = perf_counter_ns()

    def stop(self) -> None:
        self.stop_time = perf_counter_ns()

    def elapsed(self) -> float:
        return (self.stop_time - self.start_time)/1e9

    def reset(self) -> None:
        self.start_time = self.stop_time = 0
