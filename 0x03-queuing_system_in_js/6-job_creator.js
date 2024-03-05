import kue from "kue";

const queue = kue.createQueue();

const jobData = {
    phoneNumber: "1234567890",
    message: "This is a test notification",
};

const job = queue.create("push_notification_code", jobData);

job.save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    }
});

queue.on("job complete", (id) => {
    kue.Job.get(id, (err, job) => {
        if (err) return;
        console.log("Notification job completed");
        job.remove();
    });
});

queue.on("job failed", (id) => {
    console.log("Notification job failed");
    kue.Job.get(id, (err, job) => {
        if (err) return;
        job.remove();
    });
});
