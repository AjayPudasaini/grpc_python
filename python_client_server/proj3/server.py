import grpc
import hello_world_pb2
import hello_world_pb2_grpc
from concurrent import futures

from py_code.helloworld import hello_world as hello_world

class HelloMessage(hello_world_pb2_grpc.HelloWorldService):
    def SayHello(self, request, context):
        msg = request.req_msg
        respnse = hello_world_pb2.HelloResponse()
        respnse.res_msg = hello_world(msg)
        return respnse
    


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_world_pb2_grpc.add_HelloWorldServiceServicer_to_server(HelloMessage(), server)
    server.add_insecure_port('[::]:9007')
    server.start()
    print("Project-3: Server started, listening on " + '9007')
    server.wait_for_termination()


if __name__ == '__main__':
    server()