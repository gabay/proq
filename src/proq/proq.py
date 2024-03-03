from __future__ import annotations

import multiprocessing as mp
from typing import Generic, Iterable, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class ProqQueue(Generic[T]):
    _END_SENTINEL = ()

    def __init__(self, q: mp.Queue | None = None):
        self._q = q or mp.Queue()
        self._closed = False

    def put(self, item: T):
        assert not self._closed, "ProqQueue is closed."
        self._q.put(item)

    def get(self) -> T:
        return self._q.get()

    def close(self):
        assert not self._closed, "ProqQueue is closed."
        self._q.put(self._END_SENTINEL)

    def collect(self) -> Iterable[T]:
        return list(self.collect_iter())

    def collect_iter(self) -> Iterable[T]:
        while (item := self._q.get()) is not self._END_SENTINEL:
            yield item


# class ProqPool(Generic[T, U]):
#     def __init__(self, pool: mp.Pool | None = None):
#         self._pool = pool or mp.Pool()


# class Proq(Generic[T]):
#     def __init__(self, q: mp.Queue | None = None, pool: mp.Pool | None = None):
#         self._q = q or mp.Queue()
#         self._pool = pool | mp.Pool()


def create(iterable: Iterable[T]) -> ProqQueue[T]:
    proq_queue = ProqQueue[T]()
    for item in iterable:
        proq_queue.put(item)
    proq_queue.close()
    return proq_queue
