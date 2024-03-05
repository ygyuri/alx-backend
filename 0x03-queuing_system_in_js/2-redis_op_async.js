import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("error", (err) => {
    console.log(
        "Redis client not connected to the server:",
        err.toString()
    );
});

client.on("connect", async () => {
    console.log("Redis client connected to the server");

    const setAsync = promisify(client.SET).bind(client);
    const getAsync = promisify(client.GET).bind(client);

    const setNewSchool = async (schoolName, value) => {
        await setAsync(schoolName, value, print);
    };

    const displaySchoolValue = async (schoolName) => {
        const reply = await getAsync(schoolName);
        console.log(reply);
        client.quit(); // Close the Redis client after operations are done
    };

    await displaySchoolValue("Holberton");
    await setNewSchool("HolbertonSanFrancisco", "100");
    await displaySchoolValue("HolbertonSanFrancisco");
});
