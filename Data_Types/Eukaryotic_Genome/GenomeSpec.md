#Eukaryotic Genome – Multilayered

**This was designed to optimize across the following factors**

**Accuracy:** Accurately reflecting the data structure and its relationships.

**Functionality:** Allowing people to access the data they need to (both for reporting and passing into functions). Being able to reasonably cross cut the data in the primary ways needed.

**Speed:** Allowing reasonably fast access to the data

**Storage:** Where it limits the entities stored to reasonable sizes within the workspace constraints.

**The major constraints affecting my design choices are the 1 GB typed object size limit of the workspace and the fact that the workspace can only do relationships in one direction since it was designed as a DAG.**

**NOTE: This is for the multilayered approach to Genome. This is a more accurate representation of the entities involved, although it has some overhead in terms of versioning of the objects and search issues on the levels people are actually searching. The search genome blows up as it can be many annotations.**


**“\*” fields are required.**

**Structures name in bold would be WS Typed Objects**

##Spec:

<p>typedef structure {
* string taxonomy\_id\*;
* string scientific\_name\*;
* string scientific\_lineage\*;
* string domain\*;
* list\<string\> aliases;
* int genetic\_code;
* string reference\_genome\_ref;
* string genome_set_ref; 

} **Taxon**;

Note both references are nonversioned WS object reference.</p>


<p>typedef structure {

* string id;
* string name;
* string description;
* string notes
* mapping\<string genome\_id, string genome_ref\>

} **GenomeSet**</p>


typedef structure {

* string genome\_id;
* mapping\<string assembly\_id, string assembly\_ref\> assembly\_refs\_map; \#should the key be the assembly\_id or some string like reference, representative.
* string external\_source;
* string external\_source\_id;
* string external\_source origination\_date;
* string reference\_assembly\_id; \# here to mark the default assembly that should be selected for processing unless otherwise specified
* string notes;
* string environmental\_comments; \#location and environment information (perhaps separate fields for latitude, longitude, altitude)(perhaps we need a MixS object)
* string taxon\_ref;

} **Genome**; \#organism/strain name instead?

typedef structure {
* string assembly\_id\*;
* string name;
* string md5\*;
* string external\_source;
* string external\_source\_id;
* string external\_source origination\_date;
* float gc\_content;
* string type;\# Example Finished, Draft.Should be controlled vocabulary
* reads\_handle\_ref reads\_handle\_ref; \# allow for multiple read refs?
* fasta\_handle\_ref fasta\_handle\_ref\*; \# allow for multiple fasta refs?
* mapping\<string contig\_id, Contig\> contigs\*;
* assembly\_stats assembly\_stats;
* int is\_reference; \#1 reference assembly for the genome/strain, 0 is non reference
* string reference\_annotation\_id; \# here to mark the default annotation that should be selected for processing unless otherwise specified
* int dna\_size;
* int num\_contigs;
* mapping\<string annotation\_id, string annotation\_ref\> genome\_annotations;
* string comments;

} **Assembly**;

typedef structure {
* string contig\_id\*;
* int length\*;
* string md5\*;
* string name;
* string description;
* int is\_complete; \# indication of complete chromosome, plasmid, etc.
* string is\_circular\*; \# True, False and Unknown are viable values, could make an int(bool). If field not present viewed as unknown.
* int start\_position;
* int num\_bytes;

} contig;

typedef structure {

\#FangFang and others should help us spec this out

\#include assembler, sequencing tech, etc?

} assembly\_stats; \# Separate object or contained in the assembly?

typdef structure {
* string genome\_annotation\_id\*;
* int reference;
* float quality\_score; \#could be in genome\_annotation\_quality\_detail
* string annotation\_quality\_detail\_ref; \#ws\_ref
* list\<publication\> publications;
* feature\_sets\_map\* feature\_set\_references;
* string proteins\_ref;
* list\<feature\_grouping\> feature\_groupings; \# see below for feature\_grouping
* string annotation\_evidence\_ref;
* string feature\_lookup\_ref\*;
* string comments;
* string methodology; \#Not sure if needed? example would be rast

} **GenomeAnnotation**;

typedef structure{
* string id;
* string name;
* string type\*; \#Examples operon, transcriptional unit, regulons, paralogs, pathway?
* mapping\<string component\_type,list\<string feature\_id\>\> components\*;
\#component\_type would be controlled vocabulary
\# examples enhancer, silencer, operator, promoter(proximal, core), 5’ UTR, CDS, 3’ UTR, RBS
\#is order in list enough, should we have ordinal information?
\#Could be determined by structural annotation of features.
* list\<string\> grouping\_aliases;
* list\<tuple\<string annotation\_evidence\_ref, string evidence\_id\>\> grouping\_evidences;
* list\<publication\> publications;
* string comments;
\#Do we want a non ws reference to the genome\_annotation here.

}feature\_grouping;

\#may want a feature groupings object for each genome\_annotation to keep number of created objects under control.

typedef structure {
* float metadata\_completeness\*; \#value
* list\<string\> metadata\_completeness\_warnings\*;\#list of issues
* float data\_quality; \#value
* list\<string\> data\_quality\_warnings; \#list of issues
* int feature\_types\_present\*; \#number of distinct feature types annotated.
* int evidence\_supported\*; \#evidence present to support annotations
\#Do we want a non ws reference to the genome\_annotation here.

} **AnnotationQuality**;

mapping\<feature\_type, feature\_set\_ref\> **feature\_set\_map**;

\#feature type is a controlled vocabulary perhaps derived from [*http://www.insdc.org/files/feature\_table.html\#7.2*](http://www.insdc.org/files/feature_table.html#7.2)

typedef structure {
* string type; \#Ex: CDS, etc.
* mapping \<string FeatureID,Feature\> features;

}**FeatureTypeSet**;

typedef structure {
* string feature\_id\*;
* list\<tuple\<string assembly\_ref, string contig\_id, int start, string strand, int length\>\> locations\*;
* string type\*;
* string function;
* string md5\*;
* tuple\<string protein\_ref, string protein\_id\> corresponding\_protein; \#only for mRNA and CDS feature types.
* string dna\_sequence\*;
* int dna\_sequence\_length\*;
* list\<publication\> publications;
* list\<string\> aliases;
* list\<annotation\> annotations; \#does this include ontologies? Ontologies;probably a list to ontology terms or even WS objects. Details can be worked out later
* list\<subsystem\_data\> subsystem\_data;\#Blue is existing but not sure about
* list\<string\> subsystems;
* list\<ProteinFamily\> protein\_families;
* list\<tuple\<string, float\>\> orthologs; \# probably belongs on its own
* list\<regulon\_data\> regulon\_data;
* list\<atomic\_regulon\> atomic\_regulons;
* list\<coexpressed\_fid\> coexpressed\_fids;
* list\<co\_occurring\_fid\> co\_occurring\_fids;
* float feature\_quality; \# probably should be a structure
* string inference; \#Genbank has an inference tag within a feature.
* list\<string quality\_warnings\>; \# do we want severity (warnings, errors)?
* list\<tuple\<string annotation\_evidences\_ref, string evidence\_id\>\> evidences ;
* string comments;

} Feature;

Feature Questions.

Do all features have coordinates? Shuffleons do and do not Genbank has a mobile\_element\_type feature type.
Do we want to try and capture motifs. Orthologs? Orthologs get a little tricky in terms of multiple annotations for the same genome/taxonomy.

**Currently this does not explicitly cover Locus from CS (really Gene in Genbank) to CDS to mRNA relationships (note the relationship to Protein is).**

**Therefore splice variants would have to be determined on the fly based on sequence position.**

**We may want to have data structures for these. Ideally with the ability to find corresponding by features with any of the elements being searched (gene, CDS, mRNA).**

typedef structure {
*mapping\<string protein\_id, protein\> proteins\*;

\#Do we want a non ws reference to the genome\_annotation here.

}**Proteins**;

typedef structure {
* string protein\_id\*;
* mapping\<string domain, \<list\<tuple\<int coordinate\_start, int coordinate\_stop\>\>\>\>; \# can accommodate multiple of the same domain
* string peptide\_sequence\*;
* string function;
* list\<string alias\> aliases;

\#INTERACTIONS? ACTIVE SITE? ALLOSTERIC SITE? Folding pattern?

}protein;

typedef structure{
* mapping\<string feature\_key\*, list\<tuple\<string feature\_set\_ref, string feature\_id\>\> lookups\*\> feature\_lookups\*;

\#note feature key could be id or alias. Allows for fast lookup of any feature by id or alias.

\#Do we want a non ws reference to the genome\_annotation here.

} **feature\_lookup**;

typedef structure {
* string evidence\_id\*;
* string description\*;
* string evidence\_type\*; \#structural or functional?
* list\<ws\_refs\> supporting\_objects;\#Generic WS reference, not to a specific typed object.

} evidence;

typedef structure {

mapping\<string evidence\_id, evidence\> evidences\*;

\#Do we want a non ws reference to the genome\_annotation here.

} **Evidences;**

typedef tuple\<int, string, string, string, string, string, string\> publication;

\#carry over old publication. Should we change it? No author.

High level ER Diagram.

![](media/image01.jpg)

Other questions to explore.

Look up features by contig chunk (get all features in that contig chunk?)

What about reannotation, annotation corrections. How do we want to capture. Is versioning enough or do we show active and inactive, corrected?

Solution for splice variants.
Blue section of feature with carry over data.

How to deal with ontologies.

##Assessment:
* Cons to approach
* Some redundancies of data to allow for different cross sectioning of the data.
* Many objects. Although some could be hidden.
* With many object levels you get the resulting versioning cascade problem. Could make another type of reference to the object, devoid of version number. If we do this we can not have objects be able to change core type, just versions of the same WS typed object.

##Pros
* Can cross section data.
* Better access
* Faster access
* More modular
* Reasonably sized objects.
