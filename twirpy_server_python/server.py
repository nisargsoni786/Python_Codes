from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument

import calculator_pb2, calculator_twirp

# class CalculatorService(calculator_twirp.CalculatorServer):
class CalculatorService(object):
    def SquareRoot(self, context, number):
        # if number.value
        print("In server")
        ans = number.value * number.value
        return calculator_pb2.Number(value=ans)


service = calculator_twirp.CalculatorServer(service=CalculatorService())
app = TwirpASGIApp()
app.add_service(service)
