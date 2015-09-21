# Process for Help Desk Requests from External Users

When a new issue is received from an external user, it automatically creates a JIRA ticket.
Help Desk managers send a generic response (within one day) to the user notifying them that we will get them an answer soon.
Unless the Help Desk managers can answer the question themselves, they assign the issue to the person they think is most likely to be able to address it.

Within two business days, the assignee needs to look at the assigned issue and triage it, entering a comment in the ticket to indicate whether they are the right assignee. If they are not, then they should indicate (as a comment in the ticket) that they can't address it, and they should reassign to the right person if they know who that is, or say that they don't know who it should be assigned to.

If you are assigned a ticket and you are the correct assignee, then you should provide a short answer that the Help Desk managers can send to the user. Please alert the Help Desk manager, Meghan, by referring to her in your comment (as @drakemn) so that she knows to forward your response to the user.

Your answer to the user can be something like, "We know about this issue and a fix will be coming in [approximate time]," or "Can you send more information about what you were doing when the problem occurred, your environment, etc. so that we can reproduce and diagnose the problem?" (Note that http://kbase.us/report-an-issue/ has guidelines on how to report an issue effectively.)

When you respond to a ticket that you are assigned, it's important to add some indication of how hard you think the issue is likely to be to fix, and when you will have time to work on it. Please also let us know if this is blocked by another issue--another task must be completed (by you or by someone else) before this can be fixed. (If possible, include link(s) to other JIRA tickets.)

It's ok if you don't have time to work on the issue right away--the important thing is to let the EC know your time frame so that if the issue is important, we can reassign resources appropriately.

The simple workflow for responding to an assigned JIRA ticket is therefore to add a comment that answers the question, "Is this something I can address? If so, when?"

If an issue is appropriately assigned, the assignee can provide valuable information to the person who reported the issue and to the EC by classifying it as follows:

1. This is a question. (This can include cases where a user is reporting a bug but actually they are just confused about the proper usage of a feature.)
  a. The answer is... (Enter text to be forwarded to the user by Help Desk personnel.)(The assignee can then resolve (not close) the ticket.)
  b. I will need to do more research to answer this. I will answer within X days.
    (Also, it's helpful if you can indicate if this is a question that is likely to come up again and thus should be added by UE to the relevant documentation.)
    
2. This is a task.
  a. I did the task. (The assignee can then resolve (not close) the ticket.)
  b. This is a non-trivial task; I will complete it within X days.
  c. This task is out of scope or not high enough priority.
  
3. This is a bug report.
  a. I was able to confirm that the bug happens as described. It should be fixed within X days. (The assignee should not mark the ticket resolved until the fix is committed and merged.)
  b. I could not reproduce the problem, and need more information.

4. This is a request for an improvement or new feature.
  a. This was easy to do so I did it. (The assignee can then resolve (not close) the ticket.)
  b. It is on our roadmap and will likely be included in release X.
  c. It's not on our roadmap, but it's a good idea, so EC should consider adding it to our list.
  d. It's not on our roadmap and shouldn't be.

An important part of the JIRA workflow is to return to the ticket when the issue is fixed, add an appropriate comment, and (if you think the issue is completely fixed and deployed, and the reporter should be able to see the new behavior) close the ticket.

The UE will send the EC a monthly report about JIRA performance, including the identification of top issues and bottlenecks.
https://atlassian.kbase.us/issues/?filter=10909 gives a good snapshot.
