# Code Reviews #

## Lightweight Code Reviews ##

References:
* [Atlassian article on code reviews](https://www.atlassian.com/agile/code-reviews)
* [Review of effective Code Review Practices](http://www.ibm.com/developerworks/rational/library/11-proven-practices-for-peer-review/)

The goal is to have smaller code reviews that target specific fixes or new functionality along with a standard checklist of high value things to look for. Pull requests should only contain 100-400 lines of new code (not counting unit test code), and a code review should take 30-90 minutes to complete "asynchronously" (don't need to schedule face time). The review would happen before a merge or pull request is accepted. These kinds of lightweight reviews have been shown to catch a majority of software defects balanced against lowering the review burden on developers.

The reviewer must be someone outside of the group working on that particular user story, and ideally someone who is a downstream consumer of that service.

This is a comprehensive list of things that could be checked (in decreasing priority). Only the top 8 need to be "checked off", the rest are general guidelines for problems that may be found in code:

1. **Testing: Code passed static analysis with no errors or coding convention violations**
2. **Testing: Unit tests exist for new code and cover 70% of the overall code. Needless to say, the unit tests must pass.**  
2.1 **If this is a bug fix, is it possible to include a new test for this bug in the test suite?**  
2.2 **For a given level of coverage, it is better to have more granularity than less.**  
3. **Testing: Integration tests that cover reasonable example usages exist and the code passes**
4. **Testing: Unit and integration tests are added for new code paths or behaviors.**
5. **Testing: A Github actions workflow is in the repo and works properly to run kb-sdk validate on a module upon checkin, or the equivalent grandfathered Travis-CI setup ** For "extra credit" the configuration can run through unit tests and code coverage reports. Tests should make use of the [secrets available in the KBase Github Repository](https://github.com/organizations/kbase/settings/secrets/actions) for authentication  and not cleartext credentials
5. **Documentation: All methods are commented in clear language.**
5. **Make sure that workspace references are used to store object references, not conventional names, and that actual @id type is used, not string type**
5. **Verify that objects updated/created have proper provenance generated - typically by using standard utility modules such as DataFileUtils**



The following items are good coding practices that developers should aspire to in their code, but are not strict requirements for code reviews.

1. Documentation: Describe what happens with corner-case input.
2. Testing: Unit tests cover errors and invalid parameter cases.
3. Documentation: Complex algorithms are explained and justified.
4. Documentation: Code that depends on non-obvious behavior in external libraries is documented with reference to external documentation.
5. Documentation: Incomplete code is indicated with appropriate distinctive markers (e.g. “TODO” or “FIXME”).
6. Documentation: User-facing documentation is updated (online help, contextual help, tool-tips, version history).
7. Testing: Possible null pointers always checked before use.
8. Testing: Array indexes checked to avoid out-of-bound errors.
9. Testing: Don’t write new code that is already implemented in an existing, tested API.
10. Testing: New code fixes/implements the issue in question.
11. Error Handling: Invalid parameter values are handled properly early in the method.
12. Error Handling: Error values of null pointers from method invocations are checked.
13. Error Handling: Error handlers clean up state and resources no matter where an error occurs.
14. Error Handling: Memory is released, resources are closed, and reference counters are managed under both error and nonerror conditions.
15. Thread Safety: Global variables are protected by locks or locking subroutines.
16. Thread Safety: Objects accessed by multiple threads are accessed only through a lock

Comments about the code should be attached to the Pull Request in Github
