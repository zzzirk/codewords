import random
from .words import ADJECTIVES, NOUNS, DELIMITERS


class CodeWordGenerator(object):
    adjective_list = ADJECTIVES
    noun_list = NOUNS
    delimiter_list = DELIMITERS

    def __init__(self, adjfilename="adjectives.txt", nounfilename="nouns.txt",
                 delimiterfilename="delimiters.txt", *args, **kwargs):
        random.seed()
        for (filename, variable) in zip([adjfilename, nounfilename,
                                         delimiterfilename],
                                        ["adjective_list", "noun_list",
                                         "delimiter_list"]):
            try:
                if not filename:
                    continue
                with open(filename, "r") as fp:
                    setattr(self, variable,
                            [line.strip() for line in fp.readlines()])
            except IOError:
                pass

    def generate(self):
        """Generate a code word based on various rules."""
        return "{}{}{}".format(
            random.choice(self.adjective_list),
            random.choice(self.delimiter_list),
            random.choice(self.noun_list))

    def dump(self):
        return ["====="] + self.adjective_list + ["====="] + self.noun_list


def _test():
    g = CodeWordGenerator()
    print(g.generate())


if __name__ == '__main__':
    _test()
