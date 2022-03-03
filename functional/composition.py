# composition
# a . b . c (x) = a(b(c(x))), because c(x) = x(c)
# a . b . c (x) -> x(a . b . c) = x(c)(b)(a) => composition is dual operation for carring
def o_helper(functions, x):
    match functions:
        case []:
            return (lambda x: x)(x)
        case functions:
            return functions[0](o_helper(functions[1:], x))


def o(functions):
    def f(x): return o_helper(functions, x)
    return f
