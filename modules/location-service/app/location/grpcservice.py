# Importing necessary grpc modules and protobuf definitions
import grpc
from . import location_pb2
from . import location_pb2_grpc

class GRPCService:
    """
    Service class for handling gRPC calls related to locations.
    """
    def __init__(self, server_address: str):
        """
        Initialize the gRPC channel and stub for the provided server address.
        
        :param server_address: Address of the gRPC server.
        """
        self.channel = grpc.insecure_channel(server_address)
        self.stub = location_pb2_grpc.LocationStub(self.channel)

    def send_location(self, location: dict) -> str:
        """
        Send a location to the gRPC server and get a response.
        
        :param location: Dictionary containing location details.
        :return: Message from the gRPC server response.
        """
        request = location_pb2.LocationRequest(
            person_id=location["person_id"],
            creation_time=location["creation_time"],
            latitude=location["latitude"],
            longitude=location["longitude"]
        )
        response = self.stub.SendLocation(request)
        return response.message
