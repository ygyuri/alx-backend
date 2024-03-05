// Import the Redis client library
import { createClient } from "redis";

// Create a new Redis client instance
const client = createClient();

// Listen for the "connect" event and print the message when it occurs
client.on("connect", () => {
    console.log("Redis client connected to the server");
});

// Listen for the "error" event and print the error message when it occurs
client.on("error", (error) => {
    console.error(
        console.log('Redis client not connected to the server:', err.toString())
    );
});

// Close the Redis client connection when the Node process terminates
process.on("SIGINT", () => {
    client.quit();
    process.exit();
});
