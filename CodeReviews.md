# Code Reviews #

## Lightweight Code Reviews ##

References:
* [Atlassian article on code reviews](https://www.atlassian.com/agile/code-reviews)
* [Review of effective Code Review Practices](http://www.ibm.com/developerworks/rational/library/11-proven-practices-for-peer-review/)

The idea is to have a standard checklist of high value things to check for, and perform the review for smaller chunks of without needing to schedule facetime. It is very specific and targeted and the goal is for it to take something on either side of 30 minutes when the reviewer has some time to do it "asynchronously". The review would happen before a merge or pull request would be 
accepted. These kind of lightweight reviews seem to hit the 80/20 rule for code review benefits.

The reviewer must be someone outside of the group working on that particular user story, and ideally someone who is a downstream consumer of that service. The commits being reviewed for merge should be small - no more than a week's worth of development (preferably only a couple of days worth). This approach enshrines rapid, actionable feedback on what is being developed so that groups are not working for long periods of time without constructive feedback on their work products. Hopefully this will surface disconnects between what a team believes it should be building, and what other teams believe they should be building - in lieu of strict formal requirements, we perform constant lightweight reviews of the code and incremental integration testing.

 Here is a comprehensive list of things that could be checked for (in decreasing priority). Only the top 7 need to be "checked off", the rest are general guidelines for problems that may be found in code:

1. **Testing: Code passed static analysis with no errors or coding convention violations**
2. **Testing: Unit tests exist and cover 70% of the code and pass**
3. **Testing: Integration tests that cover reasonable example usages exist and the code passes**
4. **Testing: Unit and integration tests are added for new code paths or behaviors.**
5. **Testing: A Travis-CI .travis.yml file exists and works properly to run kb-sdk validate on a module upon checkin.** For "extra credit" the Travis configuration can run through unit tests and code coverage reports, however concerns about properly managing KBase credentials in Travis-CI make this optional and not required (until Mini-KBase is ready)
5. **Documentation: All methods are commented in clear language.**
6. **Documentation: Describe what happens with corner-case input.**
7. Testing: Unit tests cover errors and invalid parameter cases.
8. Documentation: Complex algorithms are explained and justified.
9. Documentation: Code that depends on non-obvious behavior in external libraries is documented with reference to external documentation.
10. Documentation: Incomplete code is indicated with appropriate distinctive markers (e.g. “TODO” or “FIXME”).
11. Documentation: User-facing documentation is updated (online help, contextual help, tool-tips, version history).
12. Testing: Possible null pointers always checked before use.
13. Testing: Array indexes checked to avoid out-of-bound errors.
14. Testing: Don’t write new code that is already implemented in an existing, tested API.
15. Testing: New code fixes/implements the issue in question.
16. Error Handling: Invalid parameter values are handled properly early in the method.
17. Error Handling: Error values of null pointers from method invocations are checked.
18. Error Handling: Error handlers clean up state and resources no matter where an error occurs.
19. Error Handling: Memory is released, resources are closed, and reference counters are managed under both error and nonerror conditions.
20. Thread Safety: Global variables are protected by locks or locking subroutines.
21. Thread Safety: Objects accessed by multiple threads are accessed only through a lock

Comments about the code should be attached to the Pull Request in Github
