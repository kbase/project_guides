# Process and Guidelines for Third Party Tools

The KBase SDK is intended to lower the barrier to integrating analysis tools as KBase Methods and enable the broader community to more easily contribute to KBase. Tools submitted for addition  to KBase will go through a standard release process (Development, Beta and Production).

## Tool states:
1.	Development: Methods in the “Development” state will be limited in visibility. They will be visible in a publicly accessible environment but won’t run against the production data stores and can’t be used in production Narratives (i.e., the method will not be visible at narrative.kbase.us).
2.	Beta: Methods in “Beta” will be visible to all users in the production Narrative Interface (narrative.kbase.us), if they chose to enable “Beta” mode in their Narrative.
3.	Production: Methods in the Production state will be visible to all.  

In order to transition a method from Development to Beta and, finally, Production, the Method must undergo a review by KBase staff. This review is intended to ensure that the Method is meeting a minimal set of guidelines and standards. Here are the general criteria that will be used when reviewing new methods which have been requested to be placed into a beta and production state.

## Criteria:
1.	All components of the tool are licensed for unrestricted open source use--for example, they cannot be “Free for academic use (but commercial users must pay to use it)”.
2.	Documentation for Methods is clear and includes any appropriate references (e.g., published papers on a tool or method) - See [Method Man pages document](Method_man_page.md).
3.	The method includes a public example Narrative demonstrating the method in action against real data.
4.	The repository contains minimal tests (e.g., at least one unit test per method with some coverage of important parameters and inputs).
