from tasker.liner import catch_line
from data_keep.souping import catch_data
from functional.composition import o
from data_keep.souping import after_catching


# to use after_catching <- ready_data <- [catch_data]
def declare_pages(url: str, page_title=None, page_list=None) -> list:
    match (url, page_title, page_list):
        case (url, None, None):
            return [catch_data(url)]
        case (url, page_title, page_list):
            match page_list:
                case []:
                    return []
                case page_list:
                    return [catch_data(url, {page_title: str(page_list[0])})] + declare_pages(url, page_title, page_list[1:])


# declare template for second coroutine
def declare_template_help(coroutines: list, template=None, attrs=None) -> list:
    match coroutines:
        case []:
            return []
        case coroutines:
            return [coroutines[0](template, attrs)] + declare_template_help(coroutines[1:], template, attrs)


# carried declaration of template
def declare_template(template=None, attrs=None) -> object:
    def carried(coroutines: list) -> list:
        return declare_template_help(coroutines, template, attrs)
    return carried


# data, ready to "after catching" morphism
def ready_after_catching(url: str, page_title=None, page_list=None, template=None, attrs=None) -> list:
    print("Ready to load data")
    return o([catch_line, declare_template(template, attrs), catch_line])(declare_pages(url, page_title, page_list))


# use in main
def shopping(url: str, page_title=None, page_list=None, template=None, attrs=None) -> list:
    print("Shopping directive 1 started...")
    try:
        return after_catching(ready_after_catching(url, page_title, page_list, template, attrs))
    except:
        print("Shopping directive 1 stopped")
        return []
