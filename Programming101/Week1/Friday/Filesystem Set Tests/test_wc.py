import unittest
from wc import count
from os import remove


class StrCounter(unittest.TestCase):
    def setUp(self):
        self.filename = "teststory.txt"
        self.contents = """Now indulgence dissimilar for his thoroughly has
terminated. Agreement offending commanded my an. Change wholly say why eldest
period. Are projection put celebrated particular unreserved joy unsatiable its.
In then dare good am rose bred or. On am in nearer square wanted.
Of resolve to gravity thought my prepare chamber so. Unsatiable entreaties
collecting may sympathize nay interested instrument. If continue building
numerous of at relation in margaret. Lasted engage roused mother an am at.
Other early while if by do to. Missed living excuse as be. Cause heard fat
above first shall for. My smiling to he removal weather on anxious.
Ferrars all spirits his imagine effects amongst neither. It bachelor cheerful
of mistaken. Tore has sons put upon wife use bred seen. Its dissimilar
invitation ten has discretion unreserved. Had you him humoured jointure ask
expenses learning. Blush on in jokes sense do do. Brother hundred he assured
reached on up no. On am nearer missed lovers. To it mother extent temper figure
better."""
        with open(self.filename, "w+") as f:
            f.write(self.contents)

    def tearDown(self):
        remove(self.filename)

    def test_lines(self):
        self.assertEqual(15, count(["lines", self.filename]))

    def test_words(self):
        self.assertEqual(166, count(["words", self.filename]))

    def test_chars(self):
        self.assertEqual(1029, count(["chars", self.filename]))

if __name__ == "__main__":
    unittest.main()
