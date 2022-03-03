from functional.functor import Functor
from functional.functor import FQuantity
import os


# returns FQuantity [x, y, ...] -> [str(x), str(y), ...]
def stringer(data: list) -> FQuantity:
    return FQuantity(data, Functor(lambda x: str(x), lambda x: x))


# init converter bs4 -> str
converter = Functor(stringer, lambda x: str(x))


# writing data into usual text file, use in main
def write_in_text(path: str, filename: str, string_list: list):
    help_list = converter(string_list).Fb
    match os.path.exists(path):
        case True:
            pass
        case False:
            os.mkdir(path)
    with open("{}\{}.txt".format(path, filename), 'a', encoding="utf-8") as opened:
        def recursive(callback_list: list):
            match callback_list:
                case []:
                    pass
                case callback_list:
                    try:
                        opened.write(str(callback_list[0][1:len(callback_list[0]) - 1]) + '\n')
                    except:
                        print("Some problems in data: {} or path {}\{}.txt".format(callback_list[0], path, filename))
                    finally:
                        recursive(callback_list[1:])
        recursive(help_list)