# Importing necessary grpc modules, futures for threaded execution, and protobuf definitions
import grpc
from concurrent import futures
import location_pb2
import location_pb2_grpc

class LocationServiceServicer(location_pb2_grpc.LocationServiceServicer):
    """
    Implements the LocationServiceServicer to handle gRPC requests for sending locations.
    """
    
    def SendLocation(self, request, context):
        """
        Handle the SendLocation gRPC call by logging the received data.
        
        :param request: The location data sent by the client.
        :param context: The gRPC context for this call.
        :return: The response message.
        """
        
        # Constructing the response message based on the received location data
        response_message = f"Received location for Person ID: {request.person_id}. " \
                           f"Coordinates: ({request.latitude}, {request.longitude}) at {request.creation_time}."
        
        # Populating and returning the response
        response = location_pb2.LocationResponse()
        response.message = response_message
        return response

def serve():
    """
    Start the gRPC server and listen for incoming connections.
    """
    
    # Initializing a gRPC server with threaded execution
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Adding the LocationServiceServicer implementation to the server
    location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServiceServicer(), server)
    
    # Defining the address and port for the server
    server_address = 'localhost:50051'
    server.add_insecure_port(server_address)
    
    # Starting the server and waiting for it to terminate
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    # Starting the gRPC server when the script is run
    serve()
