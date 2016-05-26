# WARNING: This document is mostly obsolete. Please visit https://github.com/kbase/kb_sdk for documentation about using KBase's new Software Development Kit (SDK) to integrate external open source tools as KBase apps.

#How to add a method to KBase

**What is a Method?**
[FIXME: What is the process for deciding whether a proposed new method should become a KBase method? How is the evaluation of the method and the initial code handled? The PR process forces at least some degree of code review whenever there's a change to the code, but how is the *initial* vetting done?]

A method is a single analysis step available in the Narrative Interface that performs some useful function, transformation, or visualization.

**Components of a Method**

- Service that conforms to KBase typespec as described by a KBase Interface Description Language (KIDL file)
- Script that can be executed in the [Narrative Job Service](https://github.com/kbase/narrative_job_service) (NJS)
- Method specification registered in the [narrative_method_store](https://github.com/kbase/narrative_method_store)
- Method technical documentation
- Data type definitions for input/output/parameters (see Adding Data document)
- Output visualization widget

**Overview**

A Method in KBase is complete only if it is exposed and executable from within the Narrative interface. All methods require documentation and a method specification. Based on other existing components in KBase, you may also need to do one or all of the following: 1) build and deploy or modify a service if the core functionality does not yet exist, 2) wrap and add the functionality to NJS if the execution is long running, 3) add new data types required for input/output, 4) add new output visualization if the output data types have no viz or if the viz does not show the result of the method.

**Review Process**

KBase Developers should solicit review and approval before embarking on the development of a new method, especially if it 
is not already in plan.  The level of review should be commensurate with the signficance of the addition.  If the method 
adds a new class of operation that requires significant additions in data types, UI/UX, documentaiton, etc, then this 
should be proposed and reviewed by the project leadership.  If the addition modestly extends an existing service, then 
it should be reviewed by the service lead.  Any development should follow the practices laid out in the Process Guide and other documented processes.

**Detailed Steps**

# WARNING: This document is mostly obsolete. Please visit https://github.com/kbase/kb_sdk for documentation about using KBase's new Software Development Kit (SDK) to integrate external open source tools as KBase apps.

**A. Building a new Service**

1.  Create a GitHub repository within the KBase organization
    1. Ideally the repo is created first in the [*KBaseIncubator*](https://github.com/kbaseIncubator) organization; then, if accepted for eventual deployment, migrated to the [*KBase*](https://github.com/kbase) organization
2.  Create the branches development, staging, and master. Development should be where experimental code is added. Staging should only contain stable code ready for testing (e.g., on ci.kbase.us). Master should only contain what is ready to be deployed to production.
    1.  Note: not all existing KBase repositories follow this convention, but we should move in this direction, and there is nothing blocking us from doing this for all new services.
    2.  The setup should be communicated to the Deployment / Sysadmin teams so that tests and deployments can be configured properly
3.  Set up a KBase runtime environment including a dev\_container where you can develop your new service.
    1.  Ideally, someone should point you to a Magellan image (see http://cloud.mcs.anl.gov), set up a dev instance for you, or provide a VM with the runtime environment already set up.
    2.  To build from scratch really requires its own user manual, but the quickstart guide is:
        1.  Use Linux (I think we usually use an Ubuntu base)
        2.  Create the overall container directory for kbase (usually /kb)
        3.  Checkout the kbase [*bootstrap module*](https://github.com/kbase/bootstrap) inside the base KBase directory
        4.  Look at the bootstrap README, and from within the various directories build the dependencies you need (usually at least a series of system packages, perl, python, java)
        5.  In the overall container directory, checkout the [*dev\_container*](https://github.com/kbase/dev_container)
        6.  In the modules directory of dev\_container, checkout out basic dependencies of your project (generally at least kbapi\_common, auth, typecomp, workspace\_deluxe, and their dependencies (shock\_service, handle\_service, handle\_manager, jars).  All of these are the names of other repos in the KBase github organization)
        7.  Inside the dev\_container folder, run ./bootstrap [path\_to\_runtime\_directory] to setup your environment variables, which are generated in a bash script named user-env.sh. The path to the runtime directory is generally configured to be /kb/runtime. The ./bootstrap should not be confused with the bootstrap repository- they are completely different. When you are developing, you should source the user-env.sh script to add the components to your environment. Sidenote: for python development in dev\_container, this system is broken. Python looks at the first directory in its path with a particular name, and only loads modules in that first directory found. Because of the dev\_container architecture, there is a separate python lib directory in each KBase module, and there is no tooling to build a single python dev lib folder with all the modules. So you have to do this yourself by copy/pasting manually when things change or by adding symlinks in the appropriate biokbase directories, keeping in mind you shouldn’t commit symlinks to git.
4.  Set up the basic directory structure and files of a KBase module in the modules directory of your dev\_container. Minimally, this should include (in the main directory for the module):
    1.  Makefile - invoked to build your code, deploy your service, and run tests. A description of the standard Makefile targets that must be defined along with what they do is best described [*here*](https://github.com/kbase/dev_container/blob/master/template/module.Makefile), although unclear if this is up-to-date. There is also only limited conformity with these targets across the project. The most critical targets used by the deployment team are ‘make’ to build the module and install wrapped commands inside the dev\_container/bin directory, ‘make test’ to run tests, and ‘make deploy’ to deploy the client, server, CLI, and any other dependencies to the deployment target (generally /kb/deployment, but that is configurable). The make deploy target should generate start\_service and stop\_service scripts in the deployment/services/[modulename]/ directory.
    2.  DEPENDENCES - simple text file listing the names of the KBase modules that are dependencies. There is no way to indicate if a dependency is a service, client, or CLI dependency so all should be included. The name of a KBase module is the name of the folder in which it is contained in the ‘modules’ directory of the dev\_container, which is almost always the name of the github repository.
    3.  LICENSE.md - copy of the KBase license file (copy it from an existing KBase repository or request it from India Gordon)
    4.  README.md / README.txt - your usual readme file in Markdown or plain text.
    5.  RELEASE\_NOTES.txt - set of release notes for the service. You should on each release/push to master update this file with a new version number and a description of new/updated features, bug fixes, and in some cases anticipated future developments
    6.  deploy.cfg - a service deployment configuration file defined in INI format. You should create one section for your service and define variables within that section. The deploy.cfg files for all services on a machine will be concatenated on deployment of the services to a file named ‘deployment.cfg’ that resides in the ‘deployment’ directory (or the directory that will be the target of deployment, which is configurable).  When you request deployment from the deployment team, you should notify them of any important config options that need to be set.  Do NOT include passwords or tokens in this file!
    7.  docs - a directory to store html or other technical documentation about the service.
    8.  t / test - a directory that include various test code including unit tests
5.  Create a KBase Interface Description Language (KIDL) file defining the data types used for input/output and the new method prototype.
    1.  We have no complete documentation on the KIDL language that I (Mike Sneddon) am aware of, although there is a short guide that covers a few of the basic components of the language: [*KBaseAPIDescriptionLanguageKIDL.pdf*](/KIDL/KBaseAPIDescriptionLanguageKIDL.pdf) and [*Type\_compiler.pdf*](/KIDL/Type_compiler.pdf)
6.  Compile the KIDL specification into clients and server stubs.
    1.  If you are developing a service in Perl or Python, compile the specification using the [*‘compile\_typespec’*](https://github.com/kbase/typecomp/blob/master/scripts/compile_typespec.pl) command deployed from the [*typecomp*](https://github.com/kbase/typecomp) module. If you require certain features (mainly the ability to include types from a different module, or compilation of type annotations) you must check-out the [*dev-prototypes*](https://github.com/kbase/typecomp/tree/dev-prototypes) branch or for full compatibility with the parse of type definitions performed by the [*Workspace*](https://github.com/kbase/workspace_deluxe), use the forked [*typecomp*](https://github.com/msneddon/typecomp) repository used in tests by the Workspace service. For a more complete description and justification of the features of this forked typecomp, see this [*document*](https://docs.google.com/a/lbl.gov/document/d/1RtNl2CeuAwna_CxvbWliT6Re83iGVlgVedl6sSJg4v4/edit?usp=sharing). Run the compile_typespec command with the -h flag to configure and define the arguments which define the module names, output directories, default service URLs, etc.
    2.  If you are developing a Java service or want to include Java client bindings with your service deployment, then you need to run the gen\_java\_types command deployed from the [*java\_type\_generator*](https://github.com/kbase/java_type_generator) repository. Run the command with the -h flag to configure the name of the service, output directories, default service urls, etc. At this point you should still use compile\_typespec to build the js, python and perl client libs.
    3.  The current best-practice is that generated client/server code should be checked into your module so that it doesn’t have to be rebuilt (as various branches of the typecomp cannot run in the same dev\_container / deployment environment at the same time).
7.  Implement the server stubs in your generated Perl, Python or Java Server
    1.  Additional Java runtime dependencies should be added to the [*jars*](https://github.com/kbase/jars) repository following instructions in the readme of that repository. Additional Perl or Python dependencies or other executable dependencies are added by adding the appropriate module to the [*bootstrap*](https://github.com/kbase/bootstrap) repository. After adding to the bootstrap repository, the perl/python or other runtime must be updated locally. A new dependency, however, will not be available on test or production machines until the KBase runtime is rebuilt with your new changes, the last full build being Nov 2014.
    2.  Persistent data created by the service should be saved to the Workspace or Shock (if saving to Shock, a handle should be created and saved in a Workspace object, which is required in order to view and access the data from the Narrative and landing pages). Provenance data when saving to the Workspace should be set appropriately and provide minimally the service name, service version, method name, input workspace data object references, and input parameters if relatively small.
8.  Debug your service locally
    1.  Run it locally and connect to the service using a generated client or even just curl. Services are generally run in Perl with [*Starman*](http://search.cpan.org/~miyagawa/Starman-0.1000/lib/Starman.pm), in Java with [*Glassfish*](https://glassfish.java.net/), and in Python with [uWSGI](https://uwsgi-docs.readthedocs.org)/[*WSGI*](http://wsgi.readthedocs.org).
9.  Write tests for your service
    1.  Running `make test` in your module should run unit tests and ideally put up a server, make several calls against the server, and take it down. If the Workspace or other data store is a dependency, the Workspace / data store endpoint should be a configurable parameter, and you should test against next.kbase.us or ci.kbase.us or against a local install of the workspace.
10. Ensure that the service properly deploys and runs in the KBase runtime environment, including creating the necessary start\_server and stop\_server scripts in the deployment/services directory, and that those server control scripts work and are properly configured based on the generated deployment.cfg file.
11. Write extensive documentation for your service in both the KIDL specification attached to each data type and function, and in the README.txt or other docs describing the purpose and functionality of the service. Most current services have little documentation--you should not use these as a guide.
12. Talk to the deployment and sysadmin team to get your service incorporated into the next, ci, and (eventually) production environments. You will need to tell them what type of machine your service needs to run (number of cores, amount of memory, whether it needs local storage, and what deployment.cfg variables to set).

**B. Extending an existing Service**

1.  If you are the owner of the existing service, you can make changes directly to your service. Update the KIDL specification, implement any new methods required, add test coverage of the new methods, update the RELEASE\_NOTES and readme as appropriate, and request another test/production deployment.
2.  If you are not the owner, then typically you should coordinate with the service owner and discuss whether to add the new functionality. If it seems like a good idea, you should fork the service repository, make any changes or additions there, be sure to add additional test coverage, and submit a pull request (ideally to the develop branch of the service) and work with the service owner and Deployment teams to deploy the service.

<a name="method_specs">**C. Narrative Method/App Specification + Documentation**</a>

To have your new method appear in the Narrative interface, you must define a method specification that describes the user facing descriptions and parameters of your method. The information includes the name of your method, the parameters and the parameter types, the input/output workspace object types, the output visualization, documentation on the method and each parameter, and how these parameters map to parameters sent to the Narrative Job Wrapper (which will route calls to your service or to your NJS command).

1.  Begin by looking at the [*narrative\_method\_store*](https://github.com/kbase/narrative_method_store) and [*narrative\_method\_specs*](https://github.com/kbase/narrative_method_specs) repositories. The narrative\_method\_store is a standard KIDL KBase service which dynamically pulls specification files from a specific narrative\_method\_specs repository/branch. Changes to the repository are reflected in the service every few minutes. You will eventually create pull requests to add your new specifications to an appropriate file in the narrative\_method\_specs repository. The production narrative\_method\_store service is listening here: [*https://kbase.us/services/narrative\_method\_store/rpc*](https://kbase.us/services/narrative_method_store/rpc) and is configured to pull from the master branch of the narrative\_method\_specs repository. You can view documentation attached to a method/app through the functional site, for instance, [*here*](https://narrative.kbase.us/functional-site/#/narrativestore/method/build_a_metabolic_model) or [*here*](https://narrative.kbase.us/functional-site/#/narrativestore/app/build_species_tree). Notice at the bottom of the page that the narrative\_method\_specs repo used to fetch the specification is listed.
2.  Before you directly create and edit a method specification, you need to test and debug the specification in the KBase CI deployment found at [*https://narrative-ci.kbase.us*](https://narrative-ci.kbase.us) . The CI deployment is configured to load method and app specifications from the [*narrative\_method\_specs\_ci*](https://github.com/kbase/narrative_method_specs_ci) repository. Any KBase developer can get commit privileges to this repository so that you can test your changes live. Contact Keith Keller to get access.
3.  Once you have access, directly add, edit, and commit your method spec files to the master branch of the narrative method specs CI repository. Everything you add here can be later deleted by someone else, and you should be mindful that others are also working in the CI environment with you. There is additional documentation on writing method/app specifications in the [*Readme*](https://github.com/kbase/narrative_method_specs/blob/dev/README.md)[ file](https://github.com/kbase/narrative_method_specs/blob/dev/README.md) of narrative\_method\_specs and on what information is parsed and available in the [*specification file*](https://github.com/kbase/narrative_method_store/blob/master/NarrativeMethodStore.spec) of the narrative\_method\_store.
4.  First get the basics right- configure your specification files so that there are no errors and the information appears correctly on the documentation page ([*https://narrative-ci.kbase.us/functional-site/\#/narrativestore/method/[your\_method\_name\_here]*](https://narrative-ci.kbase.us/functional-site/#/narrativestore/method/[your_method_name_here)) and the method appears and has a proper input cell generated in the Narrative CI [*interface*](https://narrative-ci.kbase.us/functional-site/#/narrativemanager/start).
5.  Next configure how your method is called by editing the ‘behavior’ block of your method specification. This block maps parameters to your method to the input for your service or NJS script. Start by configuring it to run against just your service. If you have a long-running service method, then you will need to add your code to NJS and configure appropriately in CI.
6.  Finally, configure the output widget to render the results of your method in the Narrative Interface. If the output data type exists and has a visualization that is appropriate, this is as easy as giving the widget name and indicating parameters to the widget. Most of the current widgets available in the Narrative are defined [*here*](https://github.com/kbase/narrative/tree/master/src/notebook/ipython_profiles/profile_narrative/kbase_templates/static/kbase/js/widgets/function_output). If you need to add your own widget, you will need to set up a local Narrative instance to write your code. See the section on building an output visualization in the Narrative.
7.  Thoroughly document your method, both in terms of technically what it does and more broadly why and when you would use it (the basic biological use case), including descriptions of each parameter.
8.  Once everything is working in the narrative-ci, request a review of the documentation by the man-pages team (led by Sergei Maslov currently). They will need to approve your method and docs before it is accepted in production.
9.  Once all the necessary components are accepted and deployed (i.e., new service, NJS script, Narrative output widget, new data types), make your changes in a fork of the narrative\_method\_spec repository and make a pull request into the ‘dev’ branch that clearly indicates 1) what the new feature/method/app is 2) link to the specification file in CI that you used to test the changes/additions, and 3) indicate that it has received approval from the documentation team to move forward. Based on the pull request, your method will be tested, verified, and pulled into the develop and possibly staging branches where it will be reviewed and tested again on next.kbase.us, and merged into master at which point your method goes live.

**D. Adding a job to the Narrative Job Service (NJS)**

1. Write a wrapper script around your service/method that accepts arguments something like this: 

    ```
    --command <Command name> 
    --param_file <Parameters file> 
    --service_url <Service URL> 
    --ws_url <Workspace URL> 
    --ujs_url <User and Job State URL>
    ```
    This will be how your job is executed. The parameters file has a particular syntax which specifies input parameters received from the Narrative input widget for your method. The wrapper script can either call a synchronous method in your service (there is no support for async service calls from NJS), or run some process locally if the AWE client machine is configured with your dependencies.  Work with the NJS team to determine exactly what parameters need to be supported and how your script should be executed.
2. Submit a pull request to add your command to the [*narrative\_job\_service*](https://github.com/kbase/narrative_job_service/tree/master/scripts) repository in the scripts directory. These are the set of commands available to NJS.
3. Request deployment of your new command to a worker on a test NJS deployment and test your job execution through both a direct service call and through a local or test Narrative instance that has your Method/App specification deployed and is configured to look at the test NJS deployment.
4. Talk to the deployment team about hardware requirements for executing your command, which may affect which workers are used to run your command.  The standard production NJS workers have a minimum of 22GB of memory and 2 cores.  
5. Request a production deployment of the NJS workers with your new command. Your command should be successfully deployed before the production Narrative or narrative\_method\_specs repository is updated with your new method/app specifications.

**E. Building the Output Visualization in the Narrative**

An output visualization widget is a piece of JavaScript code that does the following:

1.  Accepts a data object reference as input.
2.  Fetches and renders the data object in a visual, interactive way.
3.  Optionally maintains its state, and can update its view to reflect that state on a page reload.

These visualization widgets mostly map directly onto different data viewers, but the system is generalized enough that this isn’t a requirement. That said, the development process is identical for both, though registering them is different.

As a preliminary step, it’s best to set up a local Narrative development environment. Instructions can be found [*here*](https://github.com/kbase/narrative/blob/master/docs/developer.md).

This should be built and live in the narrative repo as follows:

1.  Extend the KBase Widget base class. All widgets require a unique ‘name’ property, which is used to invoke the widget in the page, and an ‘init’ method that initializes it. Without going into too much detail, since this is written up in more detail [*here*](https://docs.google.com/a/lbl.gov/document/d/1CGkZdsAgusN4dNs5WFX_JTJIB7-y9IkN7M3vEHIcWw4/edit), here are a few guidances:
    1.  It’s probably best to set your widget’s parent property to be ‘kbaseAuthenticatedWidget’, and link to your rendering code from the ‘loggedInCallback’ method.
    2.  Assume that your widget will appear multiple times in a page, and structure it accordingly (e.g., don’t use static IDs and then search the whole page for those IDs, since they’ll show up multiple times)
    3.  Follow the conventions in the [*KBase style guide*](http://dst.lbl.gov/projects/kbase/styleguide.html).
2.  Register your widget in the method spec - this is done by using the widget’s name in the “widgets” : “output” block of the spec. For example, the [*annotate\_contigset*](https://github.com/kbase/narrative_method_specs/blob/dev/methods/annotate_contigset/spec.json) method uses ‘kbaseGenomeView’ as its output widget.
3.  Not strictly necessary, but widgets should have the same name as their filename, for simplicity. E.g., the kbaseGenomeView widget should be use the filename kbaseGenomeView.js
4.  Register your widget in [*notebook.html*](https://github.com/kbase/narrative/blob/master/src/notebook/ipython_profiles/profile_narrative/kbase_templates/notebook.html) in the narrative repo, below the warning on line 92. This looks like a much larger mess than it is. All widgets in that block get compiled and minified together into a single kbase-narrative.min.js file.
5.  Submit a pull request to the develop branch of the narrative repo with your widget code and changes.

# WARNING: This document is mostly obsolete. Please visit https://github.com/kbase/kb_sdk for documentation about using KBase's new Software Development Kit (SDK) to integrate external open source tools as KBase apps.
