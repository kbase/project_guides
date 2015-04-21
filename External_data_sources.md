# KBase External Data Source Details

This document should be used for describing each KBase external data source in the following ways:

- How the external data source is being used in KBase, and any references to existing documentation and source code in the KBase GitHub project that describes this in more detail.
- What the license policy is of the data.
- What version or versions (if more than one copy of the data is used) are being used.
- A link or links to where the data can be accessed.
- A link or links to the documentation for this data.

---

## Data Sources

### ModelSEED

#### How ModelSEED is used in KBase

ModelSEED was the basis for the biochemistry database and the metabolic model reconstruction services in KBase. The KBase biochemistry database was initially based on a reformatted load of the entire ModelSEED biochemistry database. The KBase database has subsequently undergone additional curation and manual addition of reactions from other data sources, namely published manuscripts and published metabolic models.  

#### License for ModelSEED data

All data specific to ModelSEED is released under the ModelSEED Public License:
https://github.com/ModelSEED/ModelSEED/blob/master/LICENSE.TXT

However, some data in the ModelSEED is derived from other sources (e.g., KEGG), and that data carries its own potential licensing restrictions.

#### Versions of ModelSEED utilized

KBase loaded the 2012 version of the ModelSEED database.

#### Links to where ModelSEED can be accessed

http://seed-viewer.theseed.org/seedviewer.cgi?page=ModelView

---

### Kyoto Encyclopedia for Genes and Genomes (KEGG)

#### How KEGG is used in KBase

KEGG served as one data source for ModelSEED biochemistry database (see above), which forms the basis for all biochemistry in KBase. This biochemistry data is loaded into tables in the KBase central store and serves as the foundational data for all metabolic modeling services. The ModelSEED used raw ligand data reformatted from KEGG FTP dumps, adjusted for charge/pH, and loaded into our own database structures and formats. Overall, KBase includes the following specific data from KEGG:

- Molecular data from compounds found uniquely in KEGG including formula, chemical structure, and aliases
- Aliases and KEGG IDs from compounds found in multiple databases
- Stoichiometry and aliases for reactions found uniquely in KEGG
- Aliases and KEGG IDs for reactions found in multiple databases
- Coordinates for compounds and reactions from KEGG metabolic diagrams
- KEGG pathway organization for reactions found in KEGG

#### License for KEGG data

KEGG data was utilized for the ModelSEED project under the free academic license. No KEGG formatted data is directly accessible via KBase.

#### Versions of KEGG utilized

Release 62.0, April 1, 2012

#### Links to where KEGG can be accessed

http://www.genome.jp/kegg/

---

### IntAct

#### How IntAct is used in KBase

IntAct is one of our primary source for the protein-protein interaction in our central store.  

#### License for IntAct data
Creative Commons Attribution License 
http://www.ebi.ac.uk/intact/developer_resources

#### Links to where IntAct can be accessed

http://www.ebi.ac.uk/intact/

---

### Gene Expression Omnibus (GEO)
http://www.ncbi.nlm.nih.gov/geo/

#### How GEO is used in KBase
GEO is the primary source of public expression data.  This is what is used to populate the public KBase Expression data.  This is done by the Expression service.

#### License for GEO
http://www.ncbi.nlm.nih.gov/geo/info/disclaimer.html

"Copyright Status
Unless otherwise stated, documents and files on NCBI Web servers may be freely downloaded and reproduced. However, some material on this site, such as abstracts, may be copyright protected under the U.S. and foreign copyright laws. For such material, the submitting authors or publishers retain all rights for reproduction or redistribution. Permission to reproduce these documents may be required. All persons reproducing, redistributing, or making commercial use of this information are expected to adhere to the terms and conditions asserted by the copyright holder."

---

### Obofoundry - The Open Biological and Biomedical Ontologies
Top level collection of ontologies that are used in KBase.

####Gene Ontologies : GO terms
molecular function/Cell components/Biological process ontologies - Associated with Features.
http://geneontology.org/

license - http://geneontology.org/page/use-and-license

####Plant Ontologies : PO terms
Tissue and development ontologies - Associated with Expression Samples, GWAS and I think more.
http://www.plantontology.org/

license - http://www.plantontology.org/node/279

####Plant Environmental Ontologies : EO terms
Environmental ontologies for plants - Associated with Expression Samples, GWAS and I think more.
http://wiki.plantontology.org/index.php/Plant_Environment_Ontology_Wiki

license - can't find

####Environmental Ontologies : ENVO terms
Environment Ontologies - Currently no expression data is associated with this, but it has the capability to do so.
http://environmentontology.org/

license - closest I could find: http://environmentontology.org/home/about-envo

"We hope that the community will adopt EnvO and benefit from its potential to promote standardised data integration and access. As an open project, we welcome your use of and participation in this project. Please contact us should you like to learn more!"

---




