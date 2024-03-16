from __future__ import annotations

import dataclasses
import multiprocessing as mp
from typing import Callable, Iterable, TypeVar

from . import collectible

T = TypeVar("T")
U = TypeVar("U")


def create(objects: Iterable[T]) -> Proq[T]:
    return Proq(objects)


@dataclasses.dataclass
class Proq(collectible.Collectible[T]):
    items: Iterable[T]

    def map(self, f: Callable[[T], U]) -> Proq[U]:
        return Proq([f(item) for item in self.items])

    def collect_iter(self) -> Iterable[T]:
        yield from self.items


# class ProqPool(Generic[T, U]):
#     def __init__(self, pool: mp.Pool | None = None):
#         self._pool = pool or mp.Pool()


# class Proq(Generic[T]):
#     def __init__(self, q: mp.Queue | None = None, pool: mp.Pool | None = None):
#         self._q = q or mp.Queue()
#         self._pool = pool | mp.Pool()


# def long_function_name_to_see_what_happens_aaaaaaaaaaaaaaaaaaaaaaaa(a: str) -> str:
#     return a


# def main():
#     proq = Proq()
#     proq.create("abc").map(
#         lambda a: long_function_name_to_see_what_happens_aaaaaaaaaaaaaaaaaaaaaaaa(
#             a.upper()
#         )
#     ).map(
#         lambda a: long_function_name_to_see_what_happens_aaaaaaaaaaaaaaaaaaaaaaaa(
#             a.lower()
#         )
#     ).map(
#         lambda a: long_function_name_to_see_what_happens_aaaaaaaaaaaaaaaaaaaaaaaa(
#             a.capitalize()
#         )
#     )
#     (
#         proq.create("abc")
#         | (
#             lambda a: long_function_name_to_see_what_happens_aaaaaaaaaaaaaaaaaaaaaaaa(
#                 a.upper()
#             )
#         )
#         | (
#             lambda a: long_function_name_to_see_what_happens_aaaaaaaaaaaaaaaaaaaaaaaa(
#                 a.lower()
#             )
#         )
#         | (
#             lambda a: long_function_name_to_see_what_happens_aaaaaaaaaaaaaaaaaaaaaaaa(
#                 a.capitalize()
#             )
#         )
#     )


# # multiply by 3, keep even, count
# p = proq.create([1,2,3,4,5]).map(lambda x: x * 3).filter(lambda x: x % 2 == 0).count()

# p.run()

# pipeline = proq.pipeline().map(lambda x: x * 3).filter(lambda x: x % 2 == 0).count()
# pipeline.process([1,2,3,4,5])
# pipeline.apply([1,2,3,4,5])

# proq.make([1,2,3,4,5]) | proq.map()... | ...

# a = proq.make([1,2,3,4,5])
# b = proq.make([1,2,3,4,5])
# proq.join(a, b)

# proq.process([1,2,3,4,5])
# proq.pipeline().map(lambda x: x * 3).filter(lambda x: x % 2 == 0).count())


# a, b = proq.create().map().filter().sum().tee()


# q = proq.create()
# q.map(...)
# proq.Proq(inp1, inp2)
