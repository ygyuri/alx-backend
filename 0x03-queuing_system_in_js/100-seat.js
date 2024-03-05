import express from "express";
import kue from "kue";
import { createClient } from "redis";
import { promisify } from "util";

const app = express();
const port = 1245;

// Create a Kue queue
const queue = kue.createQueue();

// Redis client and promisify
const client = createClient();
const getAsync = promisify(client.get).bind(client);

// Reserve seats function
async function reserveSeat(number) {
    await client.set("available_seats", number);
}

// Get current available seats function
async function getCurrentAvailableSeats() {
    const availableSeats = await getAsync("available_seats");
    return parseInt(availableSeats) || 0;
}

// Initialize available seats and reservation status
reserveSeat(50);
let reservationEnabled = true;

// Routes
app.get("/available_seats", async (_req, res) => {
    const numberOfAvailableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats });
});

app.get("/reserve_seat", (_req, res) => {
    if (!reservationEnabled) {
        res.json({ status: "Reservation are blocked" });
    } else {
        const job = queue.create("reserve_seat").save((err) => {
            if (!err) {
                res.json({ status: "Reservation in process" });
            } else {
                res.json({ status: "Reservation failed" });
            }
        });
    }
});

app.get("/process", async (_req, res) => {
    res.json({ status: "Queue processing" });

    queue.process("reserve_seat", async (job, done) => {
        const availableSeats = await getCurrentAvailableSeats();
        if (availableSeats <= 0) {
            reservationEnabled = false;
            done(new Error("Not enough seats available"));
        } else {
            await reserveSeat(availableSeats - 1);
            if (availableSeats === 1) {
                reservationEnabled = false;
            }
            done();
        }
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
