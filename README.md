
# Video_to_MP3_Converter-
A microservice project to convert video to mp3
=======
Hi, there!
Here is a project using a Micro-service system design idea. The tech stacks included are Docker, Kubernetes, RabbitMQ, MongoDB,
and it uses Python. 
I'm a big fan of Python, lol. 

This project demonstrates building a scalable microservices architecture using Python and Kubernetes.
It aims to convert the video file to an mp3 file. 
the whole architecture looks like this:
![Screenshot 2025-01-15 at 1 11 42 PM](https://github.com/user-attachments/assets/2624d5c9-3c56-4c17-8332-9b02b3088a2c)

# Service Workflow

1. **User Request:**
   - Users send a request to convert a video to MP3.

2. **API Gateway:**
   - The request hits the API Gateway.
   - The Gateway stores the video in MongoDB.
   - It places a message on RabbitMQ with details of the conversion request.

3. **Message Queues:**
   - RabbitMQ contains two queues:
     - `video`: Stores requests to convert videos to MP3, including user JWT and credentials.
     - `mp3`: Stores messages indicating completed conversions, awaiting notification service.

4. **Converter Service:**
   - Acts as a consumer for the `video` queue.
   - Retrieves the video ID from MongoDB.
   - Converts the video to MP3.
   - Stores the MP3 file back in MongoDB.
   - Places a message on the `mp3` queue indicating the conversion is complete.

5. **Notification Service:**
   - Consumes messages from the `mp3` queue.
   - Sends an email notification to the user, informing them that the MP3 is ready for download.

6. **User Download:**
   - The user receives a unique ID from the notification.
   - Using this ID and their JWT, the user makes a request to the API Gateway.
   - The API Gateway retrieves the MP3 from MongoDB.
   - The user downloads the MP3 file.

# Technology Stack

The project leverages the following technologies:

1. **Python**  
   A versatile, high-level programming language known for its readability and extensive libraries, used for developing the application's core functionalities.

2. **Docker**  
   A platform that enables developers to automate the deployment of applications inside lightweight, portable containers, ensuring consistency across various environments.

3. **Kubernetes**  
   An open-source system for automating the deployment, scaling, and management of containerized applications, facilitating efficient orchestration of services.

4. **K9s**  
   A terminal-based user interface to interact with Kubernetes clusters, simplifying navigation, observation, and management of deployed applications. 

5. **RabbitMQ**  
   A robust message broker that facilitates communication between services through message queuing, enabling asynchronous processing and decoupled architecture.

6. **MongoDB**  
   A NoSQL database designed for scalability and flexibility, is used to store video and MP3 files, leveraging its capability to handle large binary data efficiently.

7. **MySQL**  
   A widely-used relational database management system, employed for managing structured data, such as user authentication details and metadata.

This combination of technologies provides a solid foundation for building a scalable, efficient, and maintainable video-to-MP3 conversion service.





JWT looks like:
<img width="1188" alt="Screenshot 2025-01-14 at 2 01 33 PM" src="https://github.com/user-attachments/assets/9b199f71-c9c6-4649-a61c-03cc7348aedc" />


