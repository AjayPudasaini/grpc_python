package com.example.java_client.client;

import com.stubspython.HelloRequest;
import com.stubspython.HelloResponse;
import com.stubspython.HelloWorldServiceGrpc;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class GrpcPythonClient {

    public static void main(String[] args) throws Exception {
        long startTime = System.nanoTime();
        // Create a gRPC channel

        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 9005)
                .usePlaintext()
                .build();

        // Generate the client stub
        HelloWorldServiceGrpc.HelloWorldServiceBlockingStub client = HelloWorldServiceGrpc.newBlockingStub(channel);

        // Invoke the gRPC API
        HelloRequest request = HelloRequest.newBuilder()
                .setReqMsg("Rabina")
                .build();
        HelloResponse response = client.sayHello(request);


        // Handle the response
        System.out.println("Response from 2020 gRPC server: " + response.getResMsg());


        long project3ResponseTime = System.nanoTime() - startTime;
        System.out.println("This is total time = " + project3ResponseTime);

    }
}
