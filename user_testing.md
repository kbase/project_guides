
# User testing

Author: Dan Gunter <dkgunter@lbl.gov>

User testing, also called "usability testing", is where one user at a time is shown something (e.g. a web site, or API) and asked to either (a) figure out what it is, or (b) try to do a typical task. The purpose of this document is to provide a landing page for details of the process of user testing as it relates to the development and deployment of new functionality in KBase.

## Organization

Although responsibility for participating in user testing is the responsibility of any team developing a UI component, the User Engagement team will be responsible for leading the process, including communication of the results to the whole group.

Before the test, there should be a written plan of what to do during the test, i.e. either a list of tasks or a plan of what to show the users. One person should be designated the _facilitator_. They will be the main person talking and guiding the user. One or two other _observers_ can also be in the room, but don't have more than a couple since that may make many testing participants anxious or unwilling.

The basic guidelines for user testing (largely taken from [1], are:

* **Keep the instructions simple.** You want users to focus on using the tool, not deciphering your instructions.
* **Try the test yourself first.** Like a demo, this "debugs" the test so the user can actually do it. Make sure you can do whatever you are asking easily in the time allotted.
* **Be nice.** Don't let people get frustrated or feel bad about the test. You should emphasize that failure to perform tasks is a failure of the software, not the user. Make it clear to participants that you _know_ they are not stupid.
* **Probe, gently.** When people start staring at the screen for 10 seconds, ask them "What are you thinking?" etc. Get users to explain why they like/hate things, or are confused. But try not to influence or distract them too much.
* **Don't give hints.** Be like ELIZA and ask, "What do _you_ think you need to do next?"
* **Take notes.** Take a few notes immediately after the test (more details under 'Communication' below).

Oh, and don't forget the most important one:

* **Provide snacks!** Get some good snacks, healthy and otherwise. These people are spending their time to help _your_ project, and deserve the good stuff.

## Communication

The best way to communicate what really happened in the user test is to make a video that shows the screen, thus what the user is doing, and also records their voice. This can be recorded for posterity, or watched "live" by a number of people in another room within wireless (but not audio) reach using Chromecast and a recent Android phone. A video captures all the nuance of user confusion, frustration, delight, etc., and communicates it in a visceral way. Of course the user should consent to the video before the test begins.

Whether or not video is recorded, after every test each observer and facilitator should type up a brief list of the problems that they saw and any thoughts they have on how to fix them. Each of these reports should be roughly a page long, so there isn't too much reading material for people who come after. These reports can be saved along with the test plan (what was shown and asked) and video, if there is any, in a folder for dissemination to appropriate people in the project. 
 
## When to do user testing

Early and often, but better late than never. Some good times to do user testing include:

* When you have a design of a change, but you haven't implemented anything
* When you have started implementing a design, and have some "farmer and the cowman" (i.e. unresolvable) disagreements
* You have an implementation but you haven't yet released it to production, and want to see if you "got it right"

## References

This is a classic, and a quick read. Highly recommended:

[1] "Don't Make Me Think", Steve Krug [website](https://www.sensible.com/dmmt.html)
