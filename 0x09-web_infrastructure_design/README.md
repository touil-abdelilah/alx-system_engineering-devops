Web Stack Diagram and Redundancy Explanation
Introduction
In the SysAdmin/DevOps track projects, we built a web stack using various components to deploy and manage web applications. Understanding each component's role and ensuring system redundancy are crucial for maintaining a stable and reliable web infrastructure.

Components of the Web Stack:
Load Balancer (LB):

Distributes incoming traffic across multiple servers to ensure optimal resource utilization and prevent overloading of any single server.
Provides fault tolerance by rerouting traffic in case of server failures.
Redundancy can be achieved by deploying multiple load balancers in active-passive or active-active configurations.
Web Servers (e.g., Apache, Nginx):

Handle HTTP requests from clients and serve web pages or dynamic content.
Redundancy is achieved by deploying multiple web servers behind a load balancer. If one server fails, the load balancer directs traffic to the healthy servers.
Database Servers (e.g., MySQL, PostgreSQL):

Store and manage application data.
Redundancy is essential to prevent a Single Point of Failure (SPOF) and ensure data availability. Techniques like database replication, clustering, or sharding are used to achieve redundancy.
Application Servers (e.g., Flask, Django):

Execute application logic and interact with the database to retrieve or manipulate data.
Redundancy can be achieved by deploying multiple application servers and using load balancing techniques to distribute traffic.
Caching Layer (e.g., Redis, Memcached):

Stores frequently accessed data in memory to reduce database load and improve application performance.
Redundancy can be implemented by configuring cache replication or clustering to ensure data availability in case of node failures.
Monitoring Tools (e.g., Nagios, Prometheus):

Monitor the health and performance of servers, services, and applications.
Redundancy is achieved by deploying monitoring agents on multiple servers and setting up alerts for immediate notification of issues.
System Redundancy
Load Balancer Redundancy: Deploy multiple load balancers in an active-passive or active-active configuration to ensure high availability. In case of a failure, the standby/load balancer takes over to maintain uninterrupted service.

Web Server Redundancy: Deploy multiple web servers behind the load balancer. If one server fails, the load balancer distributes traffic to the remaining healthy servers, ensuring continuous availability.

Database Redundancy: Implement database replication, clustering, or sharding techniques to ensure data redundancy and availability. Redundant database servers replicate data in real-time, providing failover capabilities in case of primary server failure.

Application Server Redundancy: Deploy multiple application servers and configure the load balancer to distribute traffic evenly. If one server becomes unavailable, the load balancer redirects traffic to the remaining servers, ensuring uninterrupted service.

Caching Layer Redundancy: Configure cache replication or clustering to ensure data redundancy and availability. Multiple cache nodes store copies of data, allowing the system to continue functioning even if one node fails.
