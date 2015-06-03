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
--------------------------

###Taxon

typedef structure {
* string taxonomy\_id\*;
* string scientific\_name\*;
* string scientific\_lineage;
* string domain\*;
* list\<string\> aliases;
* int genetic\_code;
* string reference\_genome\_ref;
* string genome_set_ref; 

} **Taxon**;

Note both references are nonversioned WS object reference.

---------------------------

###GenomeSet

typedef structure {

* string id;
* string name;
* string description;
* string notes;
* mapping\<string genome\_id, string genome_ref\>;

} **GenomeSet**

Note the reference is a unversioned WS object reference.

--------------------------

###Genome

typedef structure {

* string genome\_id;
* string external\_source;
* string external\_source\_id;
* string external\_source origination\_date;
* string reference\_assembly\_ref; 
* string notes;
* string environmental\_comments; 
* string taxon\_ref;
* string assembly_set_ref;

} **Genome**; 

Should object be called organism or strain name instead?

Taxon ref is a versioned WS object reference.

reference_assembly_ref is an unversioned WS object reference.

location and environment information (perhaps separate fields for latitude, longitude, altitude)(perhaps we need a MixS object)

-------------------------

###AssemblySet

typedef structure {
* string id;
* string name;
* string description;
* string notes;
* mapping\<string assembly_id, string assembly_ref>;

} **AssemblySet**

Note the reference is a unversioned WS object reference.

--------------------------

###Assembly

typedef structure {
* string assembly\_id\*;
* string name;
* string md5\*;
* string external\_source;
* string external\_source\_id;
* string external\_source origination\_date;
* float gc\_content;
* string type;
* reads\_handle\_ref reads\_handle\_ref; 
* fasta\_handle\_ref fasta\_handle\_ref\*; 
* mapping\<string contig\_id, Contig\> contigs\*;
* assembly\_stats assembly\_stats;
* int is\_reference; 
* string reference\_annotation\_ref; 
* int dna\_size;
* int num\_contigs;
* mapping\<string annotation\_id, string annotation\_ref\> genome\_annotations;
* string comments;
* string genome_ref;

} **Assembly**;

Type is a controlled vocabulary.  Example Finished, Draft.

is_reference - 1 is reference assembly for the genome/strain, 0 is non reference

reference\_annotation\_ref is a nonversion Workspace object reference.

genome_ref is a versioned workspace object reference.

-----------------------

###Contig

typedef structure {
* string contig\_id\*;
* int length\*;
* string md5\*;
* string name;
* string description;
* int is\_complete; 
* string is\_circular\*; 
* int start\_position;
* int num\_bytes;

} contig;

is_complete - is an indication of complete chromosome, plasmid, etc.

is\_circular - True, False and Unknown are viable values, could make an int(bool). If field not present viewed as unknown.

----------------------

typedef structure {

\#FangFang and others should help us spec this out

\#include assembler, sequencing tech, etc?

} assembly\_stats; 

Separate object or contained in the assembly?

-------------------------

###GenomeAnnotationSet

typedef structure {
* string id;
* string name;
* string description;
* string notes;
* mapping\<string genome_annotation_id, string genome_annotation_ref>;

} **GenomeAnnotationSet**

Note the reference is a unversioned WS object reference.


-----------------------
###GenomeAnnoation

typdef structure {
* string genome\_annotation\_id\*;
* int reference;
* float quality\_score; 
* string annotation\_quality\_detail\_ref; 
* list\<publication\> publications;
* feature\_sets\_map\* feature\_set\_references;
* string protein_set\_ref;
* string evidence_set\_ref;
* string feature\_lookup\_ref\*;
* string comments;
* string methodology; 
* string assembly_ref;

} **GenomeAnnotation**;

quality\_score could be in genome\_annotation\_quality\_detail instead

annotation\_quality\_detail\_ref would be a versioned workspace reference 

evidence\_set_ref would be a unversioned workspace reference 

protein\_set_ref would be a unversioned workspace reference 

feature\_lookup\_ref would be a unversioned workspace reference 

methodology - Not sure if needed? example would be rast

assembly_ref would be a versioned workspace reference 



mapping\<feature\_type, feature\_set\_ref\> feature\_set\_map;

This would be an unversioned workspace reference;

The feature type is a controlled vocabulary perhaps derived from [*http://www.insdc.org/files/feature_table.html#7.2*](http://www.insdc.org/files/feature_table.html#7.2)

------------------------

###AnnotationQuality

typedef structure {
* float metadata\_completeness\*; 
* list\<string\> metadata\_completeness\_warnings\*;
* float data\_quality; 
* list\<string\> data\_quality\_warnings; 
* int feature\_types\_present\*; 
* int evidence\_supported\*; 
* string genome_annotation_ref;

} **AnnotationQuality**;

genome_annotation_ref would be an unversioned workspace reference - Maybe reference not needed.

-----------------------------

###FeatureTypeSet

typedef structure {
* string id;
* string type; 
* string name;
* string description;
* string notes;
* mapping\<string feature_id, feature feature>;

} **FeatureTypeSet**

type would be controlled vocabulary - Ex: CDS, etc.

-----------------------

###Feature

typedef structure {
* string feature\_id\*;
* list\<tuple\<string assembly\_ref, string contig\_id, int start, string strand, int length\>\> locations\*;
* string type\*;
* string function;
* string md5\*;
* string dna\_sequence\*;
* int dna\_sequence\_length\*;
* list\<publication\> publications;
* list\<string\> aliases;
* string notes;

* tuple\<string protein\_ref, string protein\_id\> corresponding\_protein; \#only for mRNA and CDS feature types.

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


-------------------------------
###Feature Properies

Below are Feature properties for specific type of features.

The references for the feature properties would all be nonversioned Workspace references.

typedef structure{
* \<tuple\<string protein_set_ref, string protein_id\>\> codes_for_protein_ref;
* string EC_Number;
* \<tuple\<string feature_set_ref, string feature_id\>\> associated_mRNA_ref;
* \<tuple\<string feature_set_ref, string feature_id\>\> parent_gene_ref;
* \<tuple\<string feature_set_ref, string feature_id\>\> operon_ref;
* \<tuple\<string feature_set_ref, string feature_id\>\> pathway_ref;

} CDS_properties;

typedef structure{
* \<tuple\<string protein_set_ref, string protein_id\>\> codes_for_protein_ref;
* \<tuple\<string feature_set_ref, string feature_id\>\> associated_CDS_ref;
* \<tuple\<string feature_set_ref, string feature_id\>\> parent_gene_ref;
* \<tuple\<string feature_set_ref, string feature_id\>\> operon_ref;
* \<tuple\<string feature_set_ref, string feature_id\>\> pathway_ref;

} mRNA_properties;

typedef structure{
* \<tuple\<string protein_set_ref, string protein_id\> codes_for_protein_ref;
* \<list\<tuple\<string feature_set_ref, string feature_id\>\> children_CDS_ref;
* \<list\tuple\<string feature_set_ref, string feature_id\>\> children_mRNA_ref;
* \<tuple\<string feature_set_ref, string feature_id\> operon_ref;
* \<tuple\<string feature_set_ref, string feature_id\> pathway_ref;

} gene_properties;

typedef structure{
* \<list\<tuple\<string protein_set_ref, string protein_id\>\> protein_refs;
* \<list\<tuple\<string feature_set_ref, string feature_id\>\> component_CDS_ref;
* \<list\tuple\<string feature_set_ref, string feature_id\>\> component_mRNA_ref;
* \<tuple\<string feature_set_ref, string feature_id\>\> pathway_ref;

} operon_properties;

Note order matters in the lists.  

typedef structure{
* \<list\<tuple\<string protein_set_ref, string protein_id\>\> protein_refs;
* \<list\<tuple\<string feature_set_ref, string feature_id\>\> component_CDS_ref;
* \<list\tuple\<string feature_set_ref, string feature_id\>\> component_mRNA_ref;

} pathway_properties;

Note order matters in the lists. 

------------------------------------------

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
