def checer(*exc_type):
    def checker(functions):
        def checker(*args, **kwargs):

            try:
                result = function(*args, **kwargs)
            except Exception as exc:
                print(f"We have problem with {exc}")
            else:
                print(f"No problems. Result - {result}")

        return checker
    return checker
@checker(NameError, TypeError)
def calculate(expression):
    return eval(expression)

calculate("2+2")