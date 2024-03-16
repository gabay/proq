import proq


def test_proq_create_collect():
    assert proq.create([0, 1, 2, 3]).collect() == [0, 1, 2, 3]


def test_proq_create_map_collect():
    assert proq.create([0, 1, 2, 3]).map(lambda x: x + 1).collect() == [1, 2, 3, 4]
