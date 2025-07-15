import unittest

from audicus.utils.get_path import _parse_path, getpath


class TestGetPath(unittest.TestCase):
    def setUp(self):
        super(TestGetPath, self).setUp()

    def test_getpath(self):
        tests = [
            (range(60), ["52"], 52),
            ({"one": {"two": {"three": 4}}}, ["one", "two"], {"three": 4}),
            ({"one": {"two": {"three": 4}}}, "one.two", {"three": 4}),
            ({"one": {"two": {"three": 4}}}, "one.two.three", 4),
            ({"one": {"two": {"three": [2, 3]}}}, "one.two.three", [2, 3]),
            ({"one": {"two": {"three": 4}}}, "one.two.five", None),
            ({"one": ["two", {"three": 4}]}, "one.1.three", 4),
        ]

        for obj, path, val in tests:
            self.assertDictEqual({"result": val}, {"result": getpath(obj, path)})

    def test_parse_path(self):
        self.assertListEqual(list(_parse_path([1, 2, 3])), [1, 2, 3])
