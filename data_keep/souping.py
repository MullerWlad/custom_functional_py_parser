import bs4.element
import requests
from bs4 import BeautifulSoup
from functional.composition import o
from functional.functor import FQuantity
from functional.functor import Functor
from fake_useragent import UserAgent


# data catcher uses url, template, attrs, returns [tag, tag, ...]
async def catch_data(url: str, pars=None) -> object:
    def responser(url_r: str, pars_r=None) -> str:
        try:
            print("Data catching {}, {}...".format(url, str(pars)))
            return requests.get(url_r, pars_r, headers={"User-Agent": UserAgent().chrome}).text
        except:
            return "<p>No data</p>"

    async def soup(template=None, attrs=None) -> bs4.element.ResultSet:
        print("Data souping {}'s, {}'s...".format(template, str(attrs)))
        return BeautifulSoup(responser(url, pars), 'html.parser').find_all(template, attrs)

    return soup


# getting content list
def into_list(material) -> list:
    ls = []
    for element in material:
        ls.append(element)
    return ls


# change list, returns [[1], [2, 3], [4]] -> [[1], [2], [3], [4]]
def change_list(ls: list) -> list:
    match ls:
        case []:
            return []
        case ls:
            match isinstance(ls[0], list):
                case True:
                    return ls[0] + change_list(ls[1:])
                case False:
                    return [ls[0]] + change_list(ls[1:])


# tag string, initializing Functor object
cherry_pick = Functor(lambda x: x, o([into_list, lambda x: x.strings]))


# data quantity
def data_quantity(material: list) -> list:
    return FQuantity(material, cherry_pick).Fb


# get after catching
after_catching = o([data_quantity, change_list])
