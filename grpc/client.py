import grpc
import calculator_pb2_grpc,calculator_pb2

channel=grpc.insecure_channel('localhost:50051')

number=calculator_pb2.Number(value=16)

stub=calculator_pb2_grpc.CalculatorStub(channel)

response=stub.SquareRoot(number)

print(response)