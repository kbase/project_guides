# WARNING: This document is mostly obsolete. Please visit https://github.com/kbase/kb_sdk for documentation about using KBase's new Software Development Kit (SDK) to integrate external open source tools as KBase apps.


# How do I become a developer for KBase?

# How do I configure a development environment?

> [*How do I become a developer for KBase?*](#h.guo9a3wwmmv0)
>
> [*How do I configure a development environment?*](#how-do-i-configure-a-development-environment)
>
> [*New developer checklist:*](#new-developer-checklist)
>
> [*Get Access*](#get-access)
>
> [*Get Connected*](#get-connected)
>
> [*Decide Where to Develop*](#decide-where-to-develop)
>
> [*Magellan*](#magellan)
>
> [*Laptop*](#laptop)
>
> [*Static Development VM*](#static-development-vm)
>
> [*Get Familiar with KBase*](#get-familiar-with-kbase)
>
> [*Start Contributing*](#start-contributing)
>
> [*Getting Something into Production*](#getting-something-into-production)
>
> [*Raw Notes*](#raw-notesremaining)

# WARNING: This document is mostly obsolete. Please visit https://github.com/kbase/kb_sdk for documentation about using KBase's new Software Development Kit (SDK) to integrate external open source tools as KBase apps.

# New developer checklist:

To develop for KBase you will need a few key accounts to access development systems, commit code changes, submit and respond to bug tracking tickets, and test KBase as a user.

This table summarizes the primary accounts you need to obtain.

## Get Access

| Account Type      | URL                                                                                            | Notes                                                                                         |
|-------------------|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| KBase Developer Account | [*https://accounts.kbase.us/*](https://accounts.kbase.us/)                                       | Your request will need to be approved by a person (contact us at http://kbase.us/contact-us/ if you have problems.  Please note that for non-US citizens, additional verification steps are currently required that will take longer.)                                                                                              |
| User Account      | [*http://kbase.us/sign-up-for-a-kbase-account/*](http://kbase.us/sign-up-for-a-kbase-account/) | Your KBase user account lets you sign in to the Narrative Interface.                                                                                               |
| JIRA              | [*https://jira.kbase.us/*](https://jira.kbase.us/)                                             | Same as Developer Account (account information is maintained at [*https://accounts.kbase.us/*](https://accounts.kbase.us/), not within JIRA)                                                                    |
| GitHub            | [*https://github.com/*](https://github.com/)                                                   | Create a regular github account then request to be added to the KBase Groups via India Gordon |
| Magellan Access   | [*https://havana.cloud.mcs.anl.gov/horizon/*](https://havana.cloud.mcs.anl.gov/horizon/)       | Provided by Dev Account, but may need to request an account from Magellan support via [*https://accounts.kbase.us/*](https://accounts.kbase.us/)          |

## Get Connected

The KBase team uses a variety of methods to communicate. First and foremost is the kbase-developer mailing list. You can request access to various mailing lists at [*http://lists.kbase.us/mailman/listinfo/*](http://lists.kbase.us/mailman/listinfo/). Some groups also make use of Slack. Slack is a team communication tool that provides chat rooms with archives. You can request a free account at [*https://kbase.slack.com*](https://kbase.slack.com). Your email address will need to be from a domain currently associated with KBase (i.e., lbl.gov, anl.gov, bnl.gov, etc), or request an invitation from an owner (currently Jim Thomason and Keith Keller).

Another mechanism for communication and coordination is the JIRA issue tracking system. You should be able to access JIRA using your KBase developer account username and password. You can confirm this by logging into [*https://jira.kbase.us/*](https://jira.kbase.us/). Please note that you can't change your JIRA username or password from within JIRA. If you've forgotten your developer account password, go to [*https://accounts.kbase.us/*](https://accounts.kbase.us/) to reset it.

## Decide Where to Develop

There are a number of ways and places to develop for KBase. The choice will typically be driven by a combination of convenience and resource requirements. While development can be done from almost any modern environment, many KBase services make use of a special runtime and have dependencies on other services. These requirements should be considered as you decide where to develope.

### Magellan

Magellan is an OpenStack based internal cloud operated at ANL. Since Magellan is a virtual cloud environment, developers can easily request a virtual machine, select an image to use, control network access to the node, and provision storage.

To request access to Magellan, use the same website you used to request your developer account ([*https://accounts.kbase.us/*](https://accounts.kbase.us/)). Click on the “Configure Magellan Access” button under “Account Information”, then select KBase-Dev and click “Update/Request Tenant Membership”.

Consult the Magellan website for more information on using OpenStack ([*http://cloud.mcs.anl.gov/*](http://cloud.mcs.anl.gov/)).

### Laptop

Many developers use their laptops for development. This offers the most convenience but a laptop may not be powerful enough for developing and testing some analysis methods. The easiest way to get started is to use an existing virtual machine image.

(link)

These images can be run with VirtualBox which is available for free for all major OSs.

[*https://www.virtualbox.org/*](https://www.virtualbox.org/)

### Static Development VM

The KBase cluster at Berkeley can also provision VMs to use for analysis. This allows you to directly use the runtime and access a version of the KBase software. Contact Keith Keller or Shane Canon for access.

## Get Familiar with KBase

Before developing any code or modifying a service, familiarize yourself with some of KBase’s core design principles which are described in these documents.

-   Principles of Data in KBase (link)

-   Principles of Services in KBase (link)

-   ...what else...

## Start Contributing

KBase has adopted Github as its main source code repository and follows some of the typical development patterns followed when using GitHub. For example, all repos should be forked into a personal account and changes should be submitted through Pull Requests (PRs). If you are not familiar with Git or GitHub, then you should consult some of the excellent Getting Started guides on using Git and GitHub. You can start with [*https://help.github.com/articles/set-up-git/*] (https://help.github.com/articles/set-up-git/). [*https://www.atlassian.com/git/tutorials/*](https://www.atlassian.com/git/tutorials/) is another good resource for learning about Git.

In order to contribute to KBase repos and access any private repos, you need to be in the KBase group on GitHub. Email India Gordon for access.

KBase is a complex platform and describing all of the facets of KBase is beyond the scope of a Getting Started document. Please consult these references for more details about developing for KBase.

-   How to add a Method (link)

-   How to add a new data type (link)

Developers should start by creating any new repo in the KBaseIncubator Project space ([*https://github.com/kbaseIncubator*](https://github.com/kbaseIncubator)). This project space is intended as a place to test out new modules prior to introducing them into the KBase production pipeline.

## Getting Something into Production

Getting a new service into production is beyond the scope of this Getting Started guide. However, we will briefly describe the process. Prior to a service being considered for production, it needs to be reviewed to ensure that the developer is following best practices and that it will integrate into KBase. This would include:

-   The module doesn’t unnecessarily duplicate existing functionality in the system.

-   The module adopts existing KBase standards for data storage and job execution.

-   The module is well documented and generates documentation using the appropriate method for the language (i.e., perldoc for Perl, pydoc for python, etc)

-   The module provides unit tests and makes efforts to have good coverage.

-   The module follows the pull-request method for making changes and includes code review.

-   The module uses existing KBase data types for storing data into the workspace. The developer should work with the Data team to add any new types. These data types should provide landing pages and UI components that integrate with the Narrative interface.

-   The module provides documentation on the methods it uses including scientific references where appropriate.

-   The module implements an algorithm or a functionality that has been published in peer-reviewed journals or widely accepted as a standard approach.


Once a module has been vetted, it can be added to configuration for the Continuous Integration (CI) environment. This allows the service to be tested in a complete, but non-production environment. This will help ensure that the module interoperates with other parts of the system. Once the module has proven itself stable, it can be promoted to the “next” environment (next.kbase.us). This is meant as an early preview of the next major release for KBase.

# Raw Notes/Remaining 

I think the remainder of these are beyond the scope and should be in other how tos…

-   Understand relationship between modules and git repos

-   Learn about the KBase coding style conventions

-   Deeper intro to spec files, understand the two main branches of the type compiler, and the Java type compiler

-   Learn about all our current storage modes: Workspace, CDM, and Shock. What is in each one?

-   Learn about the Workspace service, versioning, numeric and alphanumeric references

-   Understand procedure for taking ownership of Workspace name space (also belongs in “New data” handbook)

-   Learn about the directory layout and Makefile targets for a new service

-   Learn how to write landing pages

-   Learn how to write upload/download UI in method\_specs service

-   Learn how to add new upload/download method back ends to the transform service

-   Learn how to send compute jobs to job queue and scale the workflows using AWE

-   Learn how to add appropriate authentication and authorization capability to your services

# WARNING: This document is mostly obsolete. Please visit https://github.com/kbase/kb_sdk for documentation about using KBase's new Software Development Kit (SDK) to integrate external open source tools as KBase apps.
