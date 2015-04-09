# KBase Development and Process Guidelines
**The KBase Process Guide**

## Introductory note: this is still a DRAFT

It is important to clarify that this document is at this stage, an early draft meant to elicit discussion across the KBase project. It is meant to be adapted and fine-tuned, until we can all “sign off” on it, and commit to adopting it as our common process.

It has been drafted as an attempt to capture and summarize the experience and known best practices of successful open, collaborative scientific software projects.

## Good process as the foundation for technical sustainability

The KBase project will follow a set of process guidelines for all its development activities that are aimed at:

-   making everyday development smooth, productive and effective.

-   making communication amongst all project participants effective with minimal overhead

-   creating a technically sustainable project, with a common understanding of the architecture and implementation across the team, free of individuals as bottlenecks.

-   lowering the barrier to new developers entering the project and understanding the system.

The principles this process embodies can be summarized as: *a shared responsibility to fulfill the mission of KBase, implemented via a collaborative workflow with shared ownership and understanding of architecture, code and documentation*.

As a project, KBase has accumulated a large amount of technical debt, with an overly complex architecture, poor testing and documentation practices and little regular code review. This document describes the process we will move towards, even if not every aspect of it can be achieved immediately.

Many healthy open source projects do meet *all* of these guidelines, so these are not impossible goals. By 2016, KBase must be in a mode where virtually all of these guidelines have become routine practice for all project members.

# Executive summary

-   All KBase code is open source, released under the MIT license.

-   All code development, unless explicitly authorized, will be done on public repositories on Github maintained by the KBase organization.

-   All code is peer-reviewed via a pull request before being committed.

-   All repositories have fine-grained unit test suites, connected to the pull request mechanism so that no code is ever reviewed if it fails tests.

-   All tests suites report line-level test coverage, which should monotonically increase. When new code is added, tests must be added as well.

-   System-level integration tests are run nightly and reported in an easily accessible dashboard. Any new failure at this level must be immediately tracked to the source before more new code is added.

-   All code is documented, and building documentation is the responsibility of the code developers as part of the process.

-   All work activities are tracked on JIRA (and per-repository Github issues as needed).

# Peer review of all code

## Purpose

*All* code that goes into KBase *must* be peer-reviewed: this allows the entire team of developers (both internal to the project and external community members) to organically grow a shared understanding of the system. This improves the overall quality of all code, transfers knowledge between team members, and builds a shared sense of responsibility for the overall outcomes. When problems and bugs inevitably are found, a team that shares ownership for the code treats them as a problem to be tackled as a team, rather than devolving into blaming dynamics.

## Process

All changes to any repository will be submitted as pull requests (PRs) on Github, including documentation (which is to be treated as an integral part of the development process).

No pull request can be merged without meaningful review by at least one, preferably more, members of the team working on a given repository. The discussion in the PR should be satisfactorily resolved before the PR is merged. Ultimately, if a discussion is deadlocked, the team lead for the team that owns the repo will make a decision.

A good PR is one that tackles one individual problem in a fairly atomic way, and that consists of a moderate amount of code so that it can be reviewed relatively quickly. It is much better to break up a problem into several smaller PRs than to allow one to grow to a very large size.

Developers should use their judgment in calling out (via the @user mechanism) to anyone on the project who might have a special interest in a specific PR, or whose input might be particularly valuable.

Since all repositories must have testing enabled and integrated with the Github PR system (see below), a reviewer will indicate to the author any PR that breaks the test suite and that needs to be put in a test-compliant state.

In order for this process to work well without creating undue bottlenecks, the teams must be structured with enough people and expertise to provide meaningful review. Furthermore, more senior developers must make good code review an integral part of their workflow, both in terms of providing meaningful feedback to junior developers and colleagues, and in accepting and discussing reviews from junior members. This process ensures that junior members of the team are mentored into becoming good peer reviewers as a natural part of their everyday development work.

Github offers documentation about the PR process here (KBase usess the “Fork and Pull” model): [*https://help.github.com/articles/using-pull-requests*](https://help.github.com/articles/using-pull-requests).

# Testing

## Purpose

All code has bugs, and untested code is considered to be completely broken by default (even if it gives the illusion of working). Furthermore, even very comprehensive tests can never *prove* that a code is correct, they can only raise our level of trust in the code under the range of scenarios it has been tested in.

Therefore, any non-trivial software project must adopt a strategy of comprehensive, layered, in-depth testing, where tests are used at all stages of the development and deployment process. Furthermore, all tests must be automatically executed, and the results of all test executions must be publicly available in overview dashboards that accumulate historical data on the testing status of the project.

The topic of software testing is large and complex, and in order to make meaningful progress for KBase, we’ll take a very pragmatic approach. We will focus on adding testing support as follows:

-   Unit tests for single repositories.

-   Continuous integration (CI) for all repos that run unit test suites, hooked to Github for code review via Travis CI.

-   Test coverage for all repos.

-   System-level integration tests with our own Jenkins infrastructure.

We will now briefly outline the process for each of these areas related to testing.

## Process: unit tests

Each repository must contain a collection of unit tests. These should test as much as possible of its internal code in isolation. These tests should be executable with the standard testing tool for the given language, and by default produce output at the command line that indicates test success/failure. [FIXME: are there any repos on Github already with good local testing we can use as an example? If not, we can link to other projects, but it would be best to show an example of our own].

Since our repositories currently assume a large amount of infrastructure around them to even work, there will be challenges in implementing this. One way to mitigate the need for external resources at runtime is to use mocking tools, that can stand in for other resources and provide runtime equivalents to allow the code in the repository to function. Having to use such mock tools can also help us clarify what our official APIs are between components, since those APIs are precisely what the mock tool will provide.

The following are the testing tools we will be using for each language:

-   Python: nose

-   JavaScript: casper/phantom/selenium are options.

-   Java: JUnit + EasyMock/Mockito + Javassist/PowerMock, TestNG??

-   Perl: Test::More, others??

These are some potentially useful resources on the topic [FIXME: anyone can suggest better ones?]:

-   [*http://ivory.idyll.org/blog/automated-testing-and-research-software.html*](http://ivory.idyll.org/blog/automated-testing-and-research-software.html)

-   [*http://en.wikibooks.org/wiki/Introduction\_to\_Software\_Engineering/Testing/Unit\_Tests*](http://en.wikibooks.org/wiki/Introduction_to_Software_Engineering/Testing/Unit_Tests)

-   [*http://agiledata.org/essays/tdd.html*](http://agiledata.org/essays/tdd.html) (note that KBase doesn’t follow a strict TDD process, but many of the ideas therein are useful nonetheless).

## Process: continuous integration (CI) for unit tests on each repository

Each repository’s unit test suite must be hooked up to a CI system that runs the entire test suite on every pull request and reports this information directly on the PR page.

On Github, Travis CI provides this service, and it should be enabled for all of our repositories to help validate the status of each pull request. This helps the code review process, as reviewers can know before even starting, what impact the proposed changes will have on the test suite.

Each repository should report its CI build status at the top of its README file, using the standard Github icons for it.

## Process: continuous integration (CI) for systems-level tests

KBase is complex enough that per-repository tests will never be sufficient to uncover problems that may arise due to the *interaction* between components. For this reason, we will also need to run systems-level tests in an environment that is as similar as possible to the development one that is used for staging all new work.

ci.kbase.us will provide an environment for conducting integration tests. This system will update regularly against defined branches for each repo and will run integration tests defined for a special github repo. Developers should add to this integration suite in the same way they do for unit-tests.

We have three primary deployment environments. The first is -ci, which generally tracks the develop branch and is deployed frequently. Automated integration testing will happen here, and the bar for passing and being promoted to the next stage will be high. The second stage is -next, which is intended to be as close to what will be deployed to production as possible, and is (currently) deployed weekly. When a service has been deployed in -next for long enough (~1-2 weeks, though this is flexible) the author can request that it be deployed to the production environment. ([*This doc*](Developer_deployment.md) will describe the deploy environments in more detail.)

Nightly runs of the systems integration tests will be executed in a fully automated fashion, with the additional ability for project members to trigger an execution of the tests against a specific github branch or pull request. This should be done in cases where the code reviewers suspect that a change may have the potential for introducing problems across components. In such cases, reviewers can trigger a test run, and will only accept the PR if the test run reports success.

## Process: test coverage

All test suites at the repository level will report test coverage statistics, in a format that the coveralls.io integration on Github can understand ([*https://coveralls.zendesk.com/hc/en-us*](https://coveralls.zendesk.com/hc/en-us)).

In general, we must strive for our test coverage to monotonically increase. While small fluctuations in this are normal, significant additions of code without corresponding tests are *not* acceptable, and are grounds for automatic rejection of a PR.

Each repository should report its coverage status at the top of its README file, using the standard Github 'badges' for it.

As an illustration, the IPython repository on github ([*https://github.com/ipython/ipython*](https://github.com/ipython/ipython)) shows these badges, that link to:

-   Build status and history on Travis: [*https://travis-ci.org/ipython/ipython*](https://travis-ci.org/ipython/ipython)

-   Test coverage status and history on Coveralls: [*https://coveralls.io/r/ipython/ipython?branch=master*](https://coveralls.io/r/ipython/ipython?branch=master)

# Documentation

## Purpose

All code should be well documented, as an integral and natural part of its development. The responsibility for documenting the code in each repository lies with its authors, and much like testing, the submission of undocumented code is grounds for refusal of a PR until proper documentation is added.

Every repository must contain a documentation directory, where docs can be automatically built using the standard tools for each language. Since documenting APIs tends to follow language-specific conventions, we will list below the approach used for each:

-   Python: Sphinx & numpy docstring standard ([*https://github.com/numpy/numpy/blob/master/doc/HOWTO\_DOCUMENT.rst.txt\#docstring-standard*](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#docstring-standard)).

-   JavaScript: jsdoc, others?

-   Java: Javadoc, Doxygen?

-   Perl: POD? Standards for API/function signatures?

HTML output - built docs location TBD.

## Process

At a bare minimum, each repo must have:

-   *Functional documentation*: high-level documents explaining the necessary installation and deployment dependencies as well as the overall usage of the tool contained therein. Any third-party component needed must be clearly documented here.

-   *API documentation*: auto-generated documentation that explains the function signature and purpose of, at a minimum, all public functions in the code. Private methods should also be documented for the benefit of other developers, albeit a terser amount of documentation is acceptable there.

In scientific software, the gold standard for high-quality documentation is probably provided by Mathematica: [*http://reference.wolfram.com/language*](http://reference.wolfram.com/language). Its documentation is structured in a coherent and consistent way, with clear usage examples for all code, and both tutorial-oriented docs and API details, that satisfy different usage needs.

In the open source scientific space, a good reference for a well documented project is the machine learning Python library Scikit Learn ([*http://scikit-learn.org*](http://scikit-learn.org)). Through a systematic culture of documenting all code and APIs as a natural part of its development, the project has achieved the goal of providing excellent user- and developer-facing docs, despite having zero dedicated documentation authors.

# Systematic issue tracking

## Purpose

By tracking all project activities at a high level in JIRA, we ease communication and coordination across the entire project, can more easily detect bottlenecks and critical overload on individuals, and allocate resources more effectively.

Very importantly: **Tickets are a symmetric tool for peer collaboration, they are not a tool to "toss work over the fence" for someone else**.

Therefore, use the "golden rule": treat others as you would like to be treated. That is, create a ticket such that, if you were to be its recipient, you'd be happy to work on it because you'd have everything you need to address a problem and make effective progress.

### Note about Github issues and JIRA

<span id="h.td3jik4m36hp" class="anchor"></span>

<span id="h.mi94tu8okca1" class="anchor"></span>Github issues provide excellent repository-level bug tracking, but nothing that helps us manage the project as a whole, which is where JIRA excels. We are still pondering what the best way to integrate the two as smoothly as possible is. We will update this guide as our thoughts on this question clarify.

<span id="h.qdtg26km9svm" class="anchor"></span>

<span id="h.of49szsvxiyt" class="anchor"></span>As a starting point, we will take as our solution to use JIRA almost exclusively, unless there’s a very good reason to stick to Github issues for a specific repo. For example, the repo that contains this very document will require lots of early discussion that may be much easier to do directly on github as a combination of issues and PRs than by going all the way over to JIRA. So this repo may be one that uses issues, at least for the early discussion period. But in general, we’ll keep issues disabled on most repos and track all issues on JIRA. If this proves to not work well, we will reconsider and look for better solutions.

<span id="h.oa9xym2zci9m" class="anchor"></span>

<span id="h.mw5camk5ybxw" class="anchor"></span>[FIXME: on this topic, input and ideas are especially welcome and encouraged].

<span id="h.fz6no2v2n429" class="anchor"></span>

<span id="h.gjdgxs" class="anchor"></span>

## Process

Anyone who has a significant task that requires work should file a JIRA ticket describing the issue, whether they intend to tackle it themselves or have someone else work on it.

It's very important, in order to keep an entire distributed team moving forward, that ticket submissions are *informative* and *actionable*. For those things to be true, a few minimum conditions need to be met. A good ticket MUST:

-   Have a clear, descriptive, one-sentence title. 'usability problem' is not an informative title, 'Color syntax highlighting changes after first execution' is. When writing up an issue title, imagine the following: if you had the same problem, and you could only search across issue titles, could you find your problem based on that title, and get only one hit? Try to write a title and issue description that would provide such an outcome.

-   Be as atomic as possible. Don't open one ticket for three different, unrelated problems that will likely require three different people working on them (note that JIRA allows for sub-issues that can be assigned to different people, if necessary). Ideally, one ticket is one problem that one person can fix and close. Obviously, sometimes what appears to be one problem on the surface may turn out to be much more complicated.

-   Contain all relevant information to understand and reproduce the problem without talking directly to the submitter. Whether code, screenshots, attachments, etc. Ideally, the receiver of the ticket may never need to contact you again, and they will be able to fix your problem without further input from you.

# Repository and license management on Github

On Github, we will create teams that correspond to each of the official teams in the KBase org chart. These teams will have ‘admin privileges’ (in Github parlance), which enable their members to create repos owned by that team. As a matter of policy, team members should check with their team leader before creating a new repository. They can always start work if needed on a personal repo and transfer ownership to the team afterwards if an experiment pans out.

On Github, all team members can merge PRs, and should consider all their repos to be a common responsibility, engaging with code review on all of them.

If additional areas of work in KBase require teams that cut across the existing Org chart divisions, the leads of areas 3-7 can either make them directly, or ask any of the owner's team to make a new one.

## Notes

-   all new repos must carry the official KBase license file (the text is the MIT license, with KBase headers that read in the first line: “Copyright (c) 2014 The KBase Project and its Contributors”)

-   All third party licenses are reviewed once by ANL legal department for open source requirements.

-   All repositories should be named in lowercase letters.

### 

### Special case: The jars repository

The jars repository is a repository where third party jars are kept. For this repository, India approves pull requests. Before a pull request is approved that would add new code to the repo, India verifies that the third party license is present, that the third party license is a standard open source license (i.e., a license known in the OSI listing: [*http://opensource.org/licenses*](http://opensource.org/licenses)).

In the event that a third party license has not been used in the jars repo in the past, after verifying that it is OSI-listed, Tom Brettin consults ANL legal department to verify the license is otherwise acceptable to the project.

# Data updates

The process for ingesting and updating the public KBase data stores is described in a separate document.
