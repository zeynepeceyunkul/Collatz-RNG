from dataclasses import dataclass
import time

def _collatz_step(x: int) -> int:
    return (x // 2) if (x % 2 == 0) else (3 * x + 1)

def _mix32(x: int) -> int:
    x &= 0xFFFFFFFF
    x ^= (x >> 16)
    x = (x * 0x7feb352d) & 0xFFFFFFFF
    x ^= (x >> 15)
    x = (x * 0x846ca68b) & 0xFFFFFFFF
    x ^= (x >> 16)
    return x

@dataclass
class CollatzRNG:
    seed: int

    def __post_init__(self):
        if self.seed == 0:
            self.seed = 1
        self.state = self.seed & 0xFFFFFFFF

    def next_u32(self) -> int:
        x = self.state
        for _ in range(12):
            x = _collatz_step(x)
            x = (x + 0x9e3779b9) & 0xFFFFFFFF
        out = _mix32(x ^ self.state)
        self.state = _mix32(out + 0x85ebca6b)
        return out

    def next_mod30(self) -> int:
        while True:
            r = self.next_u32()
            limit = (0x100000000 // 30) * 30
            if r < limit:
                return r % 30

def default_seed() -> int:
    return int(time.time_ns()) & 0xFFFFFFFF
