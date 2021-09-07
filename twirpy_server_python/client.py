from twirp.context import Context
from twirp.exceptions import TwirpServerException

import calculator_twirp, calculator_pb2

client = calculator_twirp.CalculatorClient("http://localhost:3000")

try:
    print("a")
    response = client.SquareRoot(ctx=Context(), request=calculator_pb2.Number(value=3))
    print(response)
except TwirpServerException as e:
    print(e.code, e.message, e.meta, e.to_dict())
