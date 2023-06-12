import grpc
import hello_world_pb2
import hello_world_pb2_grpc

def run():
    with grpc.insecure_channel('0.0.0.0:9007') as channel:
        stub = hello_world_pb2_grpc.HelloWorldServiceStub(channel)
        request = hello_world_pb2.HelloRequest()
        request.req_msg = "Requested from project 2"
        response = stub.SayHello(request)
        print(f"Response from project 3:\n{ response.res_msg }")


if __name__=='__main__':
    run()