import glob
import sys
sys.path.append('./gen-py')

from hello import UserExchange
from hello.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = UserExchange.Client(protocol)

    # Connect!
    transport.open()

    client.ping()
    print('ping() from client')

    user = User()
    user.user_id = 1
    user.firstname = "Aditya"
    user.lastname = "Pn"
    user.sex = SexType.MALE

    new_user = client.add_user(user)   

    this_user = client.get_user(1)     
    print this_user

main()