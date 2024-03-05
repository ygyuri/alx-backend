import { createClient, print } from "redis";

const client = createClient();

client.on("error", (err) => {
    console.log(
        "Redis client not connected to the server:",
        err.toString()
    );
});

client.on("connect", () => {
    console.log("Redis client connected to the server");

    // Create Hash
    client.hset("HolbertonSchools", "Portland", 50, redis.print);
    client.hset("HolbertonSchools", "Seattle", 80, redis.print);
    client.hset("HolbertonSchools", "New York", 20, redis.print);
    client.hset("HolbertonSchools", "Bogota", 20, redis.print);
    client.hset("HolbertonSchools", "Cali", 40, redis.print);
    client.hset("HolbertonSchools", "Paris", 2, redis.print);

    // Display Hash
    client.hgetall("HolbertonSchools", (err, reply) => {
        console.log(reply);
        client.quit(); // Close the Redis client after operations are done
    });
});
