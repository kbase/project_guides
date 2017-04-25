
# User testing

Author: Dan Gunter <dkgunter@lbl.gov>

User testing, also called "usability testing", is where one user at a time is shown something (e.g. a web site, or API) and asked to either (a) figure out what it is, or (b) try to do a typical task. The purpose of this document is to provide a landing page for details of the process of user testing as it relates to the development and deployment of new functionality in KBase.

## Organization

Responsibility for user testing is the responsibility of the Product Team, which is generally responsible for engaging external customers and stakeholders. Part of this responsibility is to document and report the results of user testing, as well as propose changes that will address findings that arise during testing.

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
 
## Usability Studies

This section is about when to do usability *studies* (running a usability test with a set of users) and how many resources to put into each.

The core principle is that usability testing is *iterative*: you make something, you fix it, you test it again. This means that an essential part of the process is taking the output -- i.e., the reports mentioned in the previous section -- and transforming them into to-do items for the development team. This process is still subjective, not something that arises as an objective truth; from [1], "The point of testing is not to prove or disprove something. It's to inform your judgement". Therefore, usability studies should not be seen as a gateway, proving or disproving the usability of some product, but rather as a way of gaining a better perspective on the current usability problems, while there is still plenty of time and resources to fix it.

The principle that testing informs what to fix, particularly in an agile development model, means that the most bang for the buck comes from more frequent, smaller, focused, usability studies. Each of these studies must have low overhead (otherwise you spend too much time doing usability tests), so as few as 2 users can actually be optimal -- even just 1 user could give a good "sanity check". No matter how big or complicated the product, no more than 5 users should be needed for a given usability study. As described in [2], 5 users will find almost as many usability problems as more users would. And if development resources are scarce (and when aren't they?), even this list of problems will probably need to be triaged.
 
So, to summarize:

* **Perform usability studies early.** Don't wait until just before release, or until it is too late to change course. From [1], "Testing one user early in the project is better than testing 50 at the end."
* **Have 1 to 5 users per study**. Keeping the testing lightweight and small helps it actually happen frequently enough, and anyways more users are only marginally more informative.
* **Use the results of testing to inform your judgement**. Don't try to "prove a point", or use them as a quantitative tool.
* **Fix the problems you find**. Make sure that you are ready to act on what you learned soon after the study, i.e. reserve development resources as part of the overall testing plan.

## References

This is a classic, and a quick read. Highly recommended:

[1] "Don't Make Me Think", Steve Krug. [website](https://www.sensible.com/dmmt.html)

[2] "How Many Test Users in a Usability Study?", Jakob Nielsen (2012). [website](https://www.nngroup.com/articles/how-many-test-users/)
