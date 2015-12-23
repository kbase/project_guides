# Long term goals for Social Platform

Ultimately we are building towards incorporation of a social platform into KBase. 

The goals of the social platform are to:

1. Provide the means for users to organize and share their data and results in the system. 
2. Provide a means for individual labs to organize their data and analyses in a way that is persistently available to the lab lead. 
3. Provide a means for individuals and groups to organize projects and get metrics on those projects that are sharable with project management and stakeholders that is also persistently available to project lead and citable.
4. Provide a means for users to find other users with desired expertise or data. 
5. Provide a means for users to get updated on relevant new analyses and data on the system and on updates on their projects or labs. 
6. Driving publication, sharing and use by setting up metrics and systems that promote friendly competition and collaboration.
7. Providing easy to understand metrics of individual resource utilization vs. value of work to drive granting of resources. Some of these should be public. 
8. Providing easy to understand metrics of system resource utilization, sharing value, and new “conclusions” that make it easy to ingest metrics of system success. 
9. Providing classification, metrics and display of new public results on system. 

Some of these functions are simply useful to collaborative users and laboratory leads; some of these functions are to provide justification for the system; some are to drive the principles of collaborative, knowledge driven systems biology; some are to provide incentives for using the system; some are to provide controls for misuse of the system. 

## Basic Capabilities (unordered)

### Verified Identity

One of the the things I’d like to pursue is getting verified identity for our users. This serves the principle that users are signing up to share and publish results therefore should be identifiable. This also sets us up to minimize misuse of the system and opens some ability to open advanced scripting and arbitrary data upload since our users are, to some degree, “trusted”. 

 Each account for be for a known individual except for temporary class/guest accounts (See below). ORCID, RESEARCHERID, SCOPUSID, GOOGLE SCHOLAR ID- are all possible starting points we need to determine the limits of use for all. These also allow tying in to other infrastructure that provide value to the user and perhaps ultimately to us (as we can pull it in to inform our social network.)

In addition, we may need to require certain other pieces of information that allow our social functions to work. These are described in the Groups, Projects and Roles section and the Changing institutions, groups, projects. 
### Guest and Class Accounts

Because there is a privacy issue with requiring students to identify themselves and because classes and workshops may want to issue temporary accounts without long-term storage. These accounts would not be subject to identity verification. But we would need controls on when they are created and verify the overall requester (another social role: class lead). We would probably want automatic decommission dates. Maybe something to tag unreasonable usage. 

### Groups, Projects and Roles

One of the powerful uses of our system would be for scientific leaders to organize the work they are are overseeing and even for individual users to organize their own research. The organization is both from a management perspective and might also be from a science perspective. For example, a project may contain all Narratives and data that go into a particular paper. 

#### Changing institutions/groups/projects

One of the challenging objects is how to deal cases when people change labs, projects, institutions and associated personal information like email address. If we have verified users this latter is less of an issue, but something we will need. Other challenges include when person X leaves a project/group whose responsibility is it to communicate that they are leaving? Can both X and group leader G both execute a change of group status? Can X change the belonging of a Narrative or data set to the group once it has been assigned? Can G block  X from their own data/assignment when they leave the group? What happens when the lead G steps down or moves institution, etc. 

Fundamentally though the idea is that we have to consider the structure and policy of groups and projects. A group should be consonant with a Research Group.  It might have a single lead or (gasp) multiple leads. Research Groups might contain subgroups with their own leads perhaps. Think of a company with multiple divisions using the system. Users belong to research groups and the question is whether all work they produce while affiliated is, for example, automatically shared and owned by the group lead. Or whether a user has to assign a project to a group and they do work in the project. This is, of course, also tied up with sharing. Should a lead be informed if a person on the project shares data/notebooks? Can things be shared at the project level? A model of this needs to be made. 

When someone leaves a lab or project can they: 1) Remove their data, Narratives, etc. from the project? 2) Transfer ownership? 3) If they are removed from a project how do we ensure they no longer have visibility into things (say active Narratives) that were shared with them?
#### How does data ownership accrue to each?

We will need policy and mechanism for ownership of data, Narratives and projects by people and institutions. It would seem likely that as soon as anything is assigned to to a project or group the lead of that group becomes an owner at least. This can be complicated. Imagine a project with multiple research groups affiliated. It may be there is a project in a research group that is also part of a larger project. Who has final say? 

### Finding people, collaborators and requesting contact
Ideally we would have a relatively rich way of finding people based on pieces of profile, data and Narratives users choose to expose. We need a way to respect privacy while allowing being discovered and to reward discoverability. The reasons to discover someone is: 1) To see what they are doing at some level of granularity and use it or request access, 2) To ask a question, 3) To request a collaboration. 
### Scoring and classifying people, projects, and groups 

We want to develop a set of metrics that measure people, projects and groups on similar grounds: 

1. Resource utilization- how much of our disk, CPU and network are they using?
2. Total productivity: How many multistep Narratives and Assertions have they made per set period?
3. Sharing beyond themselves, their group, their project with increasing score for more public. 
4. Direct use of their work by others in the system given that is shared. This includes services and data they have provided, derived data and inference/assertion they have made, and workflows they have shared in Narrative. 
5. Citation by others and perhap one day “influence” in that they have answered direct questions by others or are collaborating outside their immediate organization the most.
6. Ultimately some of these can be used to allow access to more or less system resources. These can also act as flag for us to highlight their work and as breadcrumbs for others to find good collaborators, data and partners. 

Note that we should also have (time dependent and time period) scores of the work product: 

1. How many times and different people have used a dataset and its derived products.
2. How many times and different people have used a method or service. 
3. How many times has a narrative been accessed, parts copied, run, or cited?
4. That is we want metrics that differentiate and highlight hot and useful data and methods for users and ultimately for meta-analysis. 

### Gamification

We should (down the road) be thinking of systems to support some form of gamification of parts of the system so that we and users can set  up competitions to achieve something with the system-- e.g. predict the modifications to an organism to optimize biofuel production; predict the environment of a community given its gene content, , solve the secondary structure of a complex transcript, etc. 

These would be use to fire up user base and generate buzz about the system; to demonstrate high value use of the system to the general public; allow research groups to “crowd source” solutions to their problems in some cases; and perhaps solve real problems! It would be great for us to come with a few seed competitions that User Engagement could run!
### Resource Utilization and the Mileage model of resource utilization

Assuming we are successful, we will ultimately need to deal with our limited resources. We could set across the board allocations but I would like to reward people for working in the system and sharing. So ultimately “frequent fliers”, “good samaritans”, and “wise-folk” should be allowed more resource as a reward for their utility to the system and its community. We could imagine a minimum allocation of space and some priority system on our execution managers. You can be promoted up to some maximum by a combination of frequent use, shared-objected used by others, and (maybe one day) by the number of times you have helped people outside your immediate environs (or something). But we should have a plan for this in some way,  
### Newsfeeds and alerts

Ideally, when a user logs in (or if they request alerts by email they should get them there) they should get an updates on things shared by people, groups, projects they follow and/or belong to; new public data about things they are interested in genes, organisms, environments, chemicals, pathways, etc.; new methods added to the system or updated. They might also be informed how many others have used their work product as well-- essentially being alerted when their metric change. 

People could subscribe as well to various other newsfeeds perhaps we and others create: KBase events; KBase versions/data cycle; KBase Contests; KBase Science; etc. And one could imagine individuals groups and projects opening feeds for their members or the public. We might open a public “crowing” channel where KBase users can push their PR to the user base (pending our approval of course.)
### Advertising results and “jobs” systemwide

Following on that last thought we should enable our users to brag about what they done, ask for help, and offer jobs via our site. Our time-dependent aggregated metrics should also allow us to identify a hot topic in public space, pick it up and advertise it for that group (pending permission perhaps). 
### Aggregating statistics

We need to build relatively automated aggregators of the metrics above for both internal use and for public consumption. We must be mindful of privacy and side-effects of such metrics for projects and people and ensure that public metrics emphasize positive rather than show negative. 
### Publication and DOI numbers

We need a coherent policy for what it means to publish something in the system and derive a minimal persistent representation of the work product for persistent caching. We should also obtain DOI numbers for the documents and referenced objects that are suitable for citation in the literature. 
