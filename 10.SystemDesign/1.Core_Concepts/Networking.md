# Networking

### What is Networking?
* connecting devices and enabling them to commicate via protocols

### Interview Relevance
* roles: infrastructure, distributed systems
* full-stack and product-focused roles only require surface level understanding

## OSI Model

| Networking layers | Protocol Data Unit (PDU) | Protocols | Function |
|-------------------|--------------------------|-----------|----------|
| 7: Application Layer | Data | DNS, HTTP, Websockets, WebRTC | point of communication between client and server: web browsers, API gateways |
| 6: Presentation Layer|
| 5: Session Layer |
| 4: Transport Layer | Segment | TCP, QUIC, UDP | ensures reliability, correct ordering, and flow control of transmitting data segments between points in a network | 
| 3: Network Layer | Packet, Datagram | IP | addressing, routing, and traffic control of packets between networks |
| 2: Data Link Layer |
| 1: Physical Layer |

### Most Important Layers to Focus on
* Application layer (7)
* Transport Layer(4)
* Network Layer(3)

## Application Layer Protocols

### HTTP/HTTPS
* standard protocol for data communication on the internet
* request-response protocol
    * client sends request to server
    * server receives request and sends back response
* stateless: each request is independent, and server doesn't store data about past requests



#### Common Request Methods
* **GET**: get data from server
    * should be idempotent: same request should get same response each time it's sent
    * don't have body
* **POST**: send data to server
* **PUT**: update data on server
* **PATCH**: update resource partially
* **DELETE**: delete data from server
    * should be idempotent


#### Common Response Status Codes
* 2xx: Success
    * 200 OK
    * 201 Created: new resource was created
* 3xx: Moved resource
    * 301 Moved Permanently
    * 302 Found: requested resource was moved temporarily
* 4xx: Client Error
    * 401 Unauthorized: request requires authentication 
    * 403 Forbidden: server forbids request
    * 404 Not Found: the requested resource was not found
    * 429 Too Many Requests: client sent too many requests in given amount of time
* 5xx: Server Error
    * 500 Server error: generic error in server
    * 502 Bad Gateway: server received invalid response from upstream server

<detail>
<summary>
What is the difference between HTTP and HTTPS, and why would I use HTTPS?
</summary>
HTTPS is HTTP with an additional security layer that uses the TLS/SSL protocol to encrypt communications. You should use HTTPS for any public website to protect against eavesdropping, and man-in-the-middle attacks.  
</details>


### Server-Sent Events
* supports one-way streaming from server to client
* can be used on top of HTTP (so browsers support it)
    * client can receive the stream from the server as one big HTTP response (same TCP connection)
    * within that response, the client gets separate packets it can process before receiving all the packets

#### Why Use SSE?
* clients want to get notifications or events ASAP e.g auction site

### Websockets
* bidirectional communication streams
* initiated via HTTP "upgrade" protocol to switch a previous connection over TCP protocol, to the Websocket connection 
    * also transfer over existing HTTP session info to the new connection e.g cookies, headers, etc
* more widely supported than gRPC, but support can still be patchy

#### Websocket Connection Steps
1. client establishes TCP connection with server
1. client starts Websocket handshake over HTTP
1. connection upgrades to Websocket protocol
1. 

## Transport Layer Protocols

### Primary Protocols
* TCP: most common on the internet, provides reliable, ordered, and error-checked delivery of data
* UDP (User Datagram Protocol): simpler, connectionless service with no guarantees of delivery, ordering, or duplicate protection.
* QUIC: not common, and not likely to be a focus in interviews

### TCP vs UDP comparison

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | "stream": a stateful connection between client and server | connectionless |
| Reliability | guaranteed: TCP will have clients and server retransmit messages if they don't receive acknowledgement | ungauranteed |
| Ordering | maintains order | no ordering guarantees |
| Flow control | Yes | No |
| Congestion Control | Yes | No |
| Header Size | 20-60 bytes | 8 bytes |
| Speed | Slower due to overhead | Faster |
| Use Cases | used by default | audio/voice streams, gaming|

<details>
<summary>
Why would I want to use UDP over TCP, and vice versa?
</summary>
I want UDP when I need the data stream to come in immediately, and reliability or ordering is not important. If I'm watching a 
video from Youtube, I'm ok with occasional glitches or skipped frames because I can always rewind. But I'll probably stop watching altogether if buffering a video takes too long.

I want TCP when I need to ensure data reaches the recipient in the right order. If I/m trading stocks online, I may need to ensure a sell order completes before a buy over and that both orders were received. I don't mind if it takes a couple of minutes to receive acknowledgement of my orders.
</details>

<details>
<summary>
Give an example of how TCP and UDP can be used together in one application.
</summary>
They can both be used in a video conferencing app like Zoom. The app would use TCP for initiating calls, adjusting app settings, and text chatting. All these features require total reliability, maintaining order of requests/messages, and don't require a lot of speed. The audio and video streaming is conducted through UDP. These features require low latency and low buffering, with some missed packets being acceptable.

</details>

## Important Examples

### A Web Request
<details>
<summary> What happens when you type a URL into your browser and press ENTER?
</summary>
The client (the web browser) looks up the IP address for the domain name. Then, the client initiates a TCP connection with the website server, using a 3-way handshake: the client sends a synchronize packet (SYN) to the server to request a connection; the server responds with a synchronize-acknowlege (SYN-ACK) packet to acknowledge the request; The client sends an ACK packet to establish the connection. Once the TCP connection is established, the client sends an HTTP GET request to fetch the web page. The server receives the request, retrieves the requested web page, then sends back a response with the web page. When the data transfer is complete, the client and server close the connection using a 4-way handshape: 1st the client sends a FIN (finish) packet to the server to terminate the connection; 2nd the server sends an ACK package upon receiving the FIN packet; 3rd the server sends a FIN packet to close its side of the connection; 4th the client acknowledge the FIN packet with an ACK packet. 
</details>