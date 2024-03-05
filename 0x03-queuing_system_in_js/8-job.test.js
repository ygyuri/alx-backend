import kue from "kue";
import { expect } from "chai";
import createPushNotificationsJobs from "./8-job.js";

describe("createPushNotificationsJobs function", function () {
    beforeEach(function () {
        kue.testMode.enter();
    });

    afterEach(function () {
        kue.testMode.exit();
    });

    it("should display an error message if jobs is not an array", function () {
        expect(() => {
            createPushNotificationsJobs(null, kue.createQueue());
        }).to.throw("Jobs is not an array");
    });

    it("should create two new jobs to the queue", function () {
        const queue = kue.createQueue();
        const list = [
            {
                phoneNumber: "4153518780",
                message: "This is the code 1234 to verify your account",
            },
            {
                phoneNumber: "4153518781",
                message: "This is the code 5678 to verify your account",
            },
        ];

        createPushNotificationsJobs(list, queue);

        expect(queue.testMode.jobs.length).to.equal(2);
    });
});
