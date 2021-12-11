#importing azure queue storage packages
from azure.storage.queue import *

#defining the connection string to the queue
connection_string = "AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;"

#listing queues function
def listQueues():
    queue_service = QueueServiceClient.from_connection_string(conn_str=connection_string)
    print("----------------------------------------------------------------")
    print('Listing all Queues:')
    queues = queue_service.list_queues()
    print('\t  Name \t\t Size')
    for queue in queues:
        queue_client = QueueClient.from_connection_string(conn_str=connection_string, queue_name=queue.name)
        properties = queue_client.get_queue_properties()
        count = properties.approximate_message_count
        print('\t* ' + queue.name + '\t ' + str(count))
    print("----------------------------------------------------------------")

#sending messages function
def send():
    print("Enter the name of the queue you wish to send a message to")
    queueName = str(input())
    print("Enter the Message")
    message = str(input())
    print("----------------------------------------------------------------")
    queue = QueueClient.from_connection_string(conn_str=connection_string, queue_name=queueName)
    queue.send_message(message)
    print("\t Message sent")
    print("----------------------------------------------------------------")
    
#receiving messages function
def receive():
    print("Enter the name of the queue you wish to read it's messages")
    queueName = str(input())
    queue = QueueClient.from_connection_string(conn_str=connection_string, queue_name=queueName)
    response = queue.receive_messages()
    print("----------------------------------------------------------------")
    print("Printing Queue (" + queueName + ") Messages:")
    print('\t Message:')
    for message in response:
        print('\t* ' + message.content)
        queue.delete_message(message)
    print("----------------------------------------------------------------")

#creating a Queue function
def create():
    print("Enter the name of the queue you wish to create")
    queueName = str(input())
    print("----------------------------------------------------------------")
    queue_client = QueueClient.from_connection_string(connection_string, queueName)
    queue_client.create_queue()
    print("\t Queue " + queueName + " created successfully")
    print("----------------------------------------------------------------")
    
#deleting a Queue function
def delete():
    print("Enter the name of the queue you wish to delete")
    queueName = str(input())
    print("----------------------------------------------------------------")
    queue_client = QueueClient.from_connection_string(connection_string, queueName)
    queue_client.delete_queue()
    print("\t Queue " + queueName + " deleted successfully")
    print("----------------------------------------------------------------")


#Welcome Message
print("\n")
print("*******************************************************************************")
print("*****Python Program for testing Azure storage Queue using Azurite emulator*****")
print("*****              Author: Duraid Maihoub                                 *****")
print("*******************************************************************************")
print("\n")
print("Note: Enter The number of the option to execute it")
print("--for example if you want to create a Queue Enter 1")
print("\n")
x = 'a'
while 1:
    print("Options:")
    print("\t1) List Queues")
    print("\t2) Create a Queue")
    print("\t3) Delete a Queue")
    print("\t4) Send Message to a Queue")
    print("\t5) Receive Messages from a Queue")
    print("\tx) Terminate Execution")
    x = input()
    #Listing Queues
    if x == '1':
        listQueues()
    
    elif x == '2':
        create()
    
    elif x == '3':
        delete()
        
    elif x == '4':
        send()
        
    elif x == '5':
        receive()
    elif x == 'x':
        print("----------------------------------------------------------------")
        print("\tProgram Terminated Successfully")
        print("----------------------------------------------------------------")
        break
    else:
        print("----------------------------------------------------------------")
        print("ERROR!!! wrong input, please Enter 1,2,3,4,5 or x to terminate")
        print("----------------------------------------------------------------")