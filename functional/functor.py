from functional.composition import o


class Context:
    def __init__(self, function: object, object: object):
        self.f = function
        self.obj = object

    def __enter__(self):
        self.message = "Context created for " + str(self.f) + " " + str(self.obj)
        try:
            return self.f(self.obj)
        except:
            self.message = "Context failed for " + str(self.f) + " " + str(self.obj)

    def __exit__(self, type, val, trace):
        print(self.message)


class Functor:
    def __init__(self, functor: object, function: object):
        self.F = functor
        self.f = function

    def __call__(self, object):
        with Context(self.F, object) as answer:
            return answer

    def Fof(self, object):
        with Context(o([self.F, self.f]), object) as answer:
            return answer


class FQuantity:
    def __Fq(qua: list, container: object) -> list:
        match qua:
            case []:
                return []
            case qua:
                return [container(qua[0])] + FQuantity.__Fq(qua[1:], container)

    def __init__(self, qua: list, functor: Functor):
        self.Fa = FQuantity.__Fq(qua, functor)
        self.Fb = FQuantity.__Fq(qua, functor.Fof)
