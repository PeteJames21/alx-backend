#!/usr/bin/node
import Bull from "bull";

async function sendNotification(job, done) {
  console.log(
    `Sending notification to ${job.data.phoneNumber}, with message: ${job.data.message}`
  );
  done(null, {result: 'ok'});
}

const messages = new Bull('messages');
messages.process(sendNotification);
