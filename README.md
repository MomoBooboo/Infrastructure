#Develop a leaderboard service for Tanx, ranking traders on the Decentralised Exchange by their
trading volume 

Step 1: Set Up Infrastructure
Launch EC2 instances for each component (EC2_A, EC2_B, EC2_C).
Install Docker on each EC2 instance.
Create separate directories on each instance for storing Docker Compose files.

Step 2: Create Docker Compose Files
Create a Docker Compose file for EC2_A containing services for the Leaderboard Service and Trade Producer Service.
Create separate Docker Compose files for EC2_B and EC2_C, specifying Postgres and Redis services respectively.

Step 3: Develop Leaderboard Service
Implement the Leaderboard Service logic to receive user IDs and trading volumes, rank them in real-time, and provide API endpoints.
Create API endpoints for accessing the current leaderboard list, including user ID, cumulative volume, and rank.

Step 4: Develop Trade Producer Service
Develop the Trade Producer Service to periodically send trade data containing user IDs and volumes.

Step 5: Implement Message Queue 
Set up a message queue (e.g., RabbitMQ, AWS SQS) for enhanced functionality in handling trade data.

Step 6: Configure Reverse Proxy 
Set up a reverse proxy (e.g., Nginx) to handle web traffic directed to the Leaderboard Service on port 80.

Step 7: Cache API Responses
Implement caching mechanisms (e.g., Redis caching) to cache API responses for better read throughput.

Step 8: Testing and Deployment
Test the services locally to ensure they function as expected.
Use Docker Compose to deploy the services on the respective EC2 instances.
Verify that the services are running correctly on the instances.
Test the API endpoints to ensure they return the expected results.
