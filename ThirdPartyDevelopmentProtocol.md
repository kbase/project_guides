# Guide to Near-Term Handling of External Developers. 

Many external projects have been planning to add functionality to KBase and in some cases it is in their milestones.
Given the current status of the project wherein we are slowly bringing the framework into increased reliability and extensibility; 
and given our roadmap and finite resources we have to have a communicate our policy for when and how such tools get incorporated. 
As the system matures we can open up the spigot a bit wider but for now we must be cicumspect:


The following is a draft of a policy:

1. We are only incorporating third party tools in a very staged and incremental way. But that we are prioritizing on our roadmap SFA, BRC, User facility and a few key core capabilities we need for the system.
2.  We are trying to ensure that the foundational elements that support these workflows are in place before the more advanced functionality.
3.  We would like a major part of the process for third party contributors to be a design document and preparing their systems for efficient incorporation.

This would involve:

1. A statement of function of the software and the expected "size" of the userbase that would like to see this incorporated. Citations. Authors. 
2. A clean statement of data types ingested by the software and producted by the software. 
3. A clean statement of the actual software packages used and their dependencies and the verification that they are open-source and unrestricted. 
4. A statement of any external resources (databases, services, etc.) on which they depend. 
5. A clean statement of any dependencies on standing up new internal databases and their update cycle requirements, and software requirements. 
6. A git repo containing example, input and output data, and the software and all documentation. 
7. An assessment of how we might stage integration so that we support the generally useful pieces of the system first and accelerate the integration later. 
8. An assessment of external data resources that contain relevant input data or output data types that are of sufficient size and stability that they might be useful to integrate into KBase itself so that users could find utility quickly. 
9. Please estimate the execution environment needs of your software including architecture, node types and numbers, and expected execution times.

We will try and point possible 3rd party developers to our principles documents so they understand our standards. 
We will also be developing standards for service/method design that are relevant (e.g. ensure you are not repackaging existing function).
We will add the repo to our roadmap and ultimately update the schedule to reflect our estimates of when we will be able to approach integration.
