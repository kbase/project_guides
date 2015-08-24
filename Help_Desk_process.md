# Process for Help Desk Requests from External Users

When a new issue is received from an external user, it automatically creates a JIRA ticket.
Help Desk managers send a generic response (within one day) to the user notifying them that we will get them an answer soon
Unless the Help Desk managers can answer the question themselves, they assign the issue to the relevant box lead.
The box lead assigns external issues within two days to someone who can address the issue.

Within three business days, the assignee looks at the assigned issue and triages it, entering a comment in the ticket to indicate:

0. I can't address this, please give it to someone else.
1. This is a question. (This can include cases where a user is reporting a bug but actually they are just confused about the proper usage of a feature.)
  a. The answer is... (Enter text to be forwarded to the user by Help Desk personnel.)(The assignee can then resolve (not close) the ticket.)
  b. I will need to do more research to answer this. I will answer within X days.

    (Also, indicate if this is a question that is likely to come up again and thus should be added by UE to the relevant documentation.)
    
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

UE will send the EC a monthly report about JIRA performance.
