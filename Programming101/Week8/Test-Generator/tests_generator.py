from sys import argv
import re
from generator_power import boilerplate, testcase_boilerplate


def is_empty_line(line):
    return len(line.strip()) != 0


def lines(textContents):
    return textContents.split("\n")


def unlines(lineData):
    return "\n".join(lineData)


def get_file(file):
    return open(file).read()


def generate_script_name(dsl_file):
    return dsl_file.replace(".dsl", ".py")


def first_uppercase(wordstring):
    return wordstring.title()


def generate_class_name(dsl_file):
    words = dsl_file.strip(".dsl").split("_")
    classname = list(map(first_uppercase, words))
    return "".join(classname)


def is_line_import(line):
    if line.startswith("from") or line.startswith("import"):
        return True
    return False


def get_all_imports(contents):
    return filter(is_line_import, contents)


def is_line_description(line):
    if line.startswith('"'):
        return True
    return False


def generate_class_description(contents):
    return filter(is_line_description, contents)


def is_testcase(line):
    if "->" in line:
        return True
    return False


def string_strip(string):
    return string.strip()


def generate_testcase(case, static={"counter": 0}):
    static["counter"] += 1
    testcase = testcase_boilerplate

    conditions = case.split("->")
    parts = list(map(string_strip, conditions))
    methodvalue = parts[1].split(" == ")

    regex = "(.*?)"
    method_name = re.sub(regex, "", methodvalue[0])
    if methodvalue[1] == "True" or methodvalue[1] == "False":
        assert_case = methodvalue[1]
    else:
        assert_case = "Equal"
        method_name += ", {}".format(methodvalue[1])

    testcase = testcase.replace("{ErrorMessage}", parts[0])
    testcase = testcase.replace("{method}", method_name)
    testcase = testcase.replace("{bool}", assert_case)
    testcase = testcase.replace("{x}", str(static["counter"]))
    return testcase


def main():
    dsl = argv[1]
    template = boilerplate

    contents = lines(get_file(dsl))
    noEmptyLines = list(filter(is_empty_line, contents))
    script_name = generate_script_name(dsl)
    imports = unlines(list(get_all_imports(noEmptyLines)))
    classname = generate_class_name(dsl)
    description = list(generate_class_description(noEmptyLines))[0]
    tests = list(filter(is_testcase, noEmptyLines))
    cases = list(map(generate_testcase, tests))

    template = template.replace("{imports}", imports)
    template = template.replace("{class_name}", classname)
    template = template.replace("{ClassDescription}", description)
    template = template.replace("{test_cases}", unlines(cases))

    file = open(script_name, "w")
    file.write(template)
    file.close()

if __name__ == "__main__":
    main()
