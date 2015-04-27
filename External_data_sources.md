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

#### License for Obofoundry 
http://wiki.obofoundry.org/wiki/index.php/FP_001_open
Creative Commons CC-BY license version 4.0 or later.

#### Link to where obofoundry can be accessed

http://www.obofoundry.org/

---

#### Gene Ontologies : GO terms
Molecular function/Cellular components/Biological process ontologies - Associated with Features.
http://geneontology.org/

license - http://geneontology.org/page/use-and-license

#### Plant Ontologies : PO terms
Tissue and development ontologies - Associated with Expression Samples, GWAS.
http://www.plantontology.org/

license - http://www.plantontology.org/node/279 is licensed under a Creative Commons Attribution 4.0 International License. 

#### Plant Environmental Ontologies : EO terms
Environmental ontologies for plants - Associated with Expression Samples, GWAS.
http://wiki.plantontology.org/index.php/Plant_Environment_Ontology_Wiki

license - http://crop.cgrb.oregonstate.edu/node/1 is licensed under a Creative Commons Attribution 3.0 United States License.

#### Environmental Ontologies : ENVO terms
Environment Ontologies - Currently no expression data is associated with this, but it has the capability to do so.
http://environmentontology.org/

license - http://environmentontology.org/home/about-envo

"We hope that the community will adopt EnvO and benefit from its potential to promote standardised data integration and access. As an open project, we welcome your use of and participation in this project. Please contact us should you like to learn more!"

---

### Plant Metabolic Network

#### How Plant Metabolic Network is used in KBase

Plant Metabolic Network includes all of the plant metabolic pathway databases including AraCyc, PlantCyc, BarleyCyc, BrachypodiumCyc, ChlamyCyc, CornCyc, GrapeCyc, MossCyc, OryzaCyc, PapayaCyc, PoplarCyc, SelaginellaCyc, SetariaCyc, SorghumBicolorCyc, SoyCyc, SwitchgrassCyc.  

#### License for Plant Metabolic Network data
http://plantcyc.org/downloads/license_agreement.faces
This license is freely available to everyone, including commercial users

#### Links to where Plant Metabolic Network data can be accessed

http://plantcyc.org/downloads/data_downloads.faces

---

### Plant Reactome

#### How Plant Reactome is used in KBase

Plant Reactome is plant pathway database which hosts plant metabolic and regulatory pathways. Plant Reactome pathways are constructed by manual curation of pathways and reactions reported in the published literature or derived by orthology-based computational projections from curated pathways in the MetaCyc, Plant Metabolic Network, and Human Reactome databases. Pathways, reactions and gene entries in Plant Reactome are cross-referenced to many bioinformatics databases such as UniProt, ChEBI, PubChem, PubMed, Gramene and Plant Ensembl genomes and the Gene Ontology (GO).

#### License for Plant Reactome
http://plantreactome.gramene.org/copyright.html
Creative Commons Attribution 3.0 United States License.

#### Links to where Plant Reactome data can be accessed

http://plants.reactome.org/about.html

---

### UniProtKB

#### How UniProtKB is used in KBase

The UniProt Knowledgebase (UniProtKB) provides functional information on proteins, with accurate, consistent and rich annotation. It has two sections - Swiss-Prot and TrEMBL. UniProtKB/Swiss-Prot is a high quality manually annotated and non-redundant protein sequence database, which brings together experimental results, computed features and scientific conclusions. UniProtKB/TrEMBL contains high quality computationally analyzed records that are enriched with automatic annotation and classification. These UniProtKB/TrEMBL unreviewed entries are kept separated from the UniProtKB/Swiss-Prot manually reviewed entries so that the high quality data of the latter is not diluted in any way. 

#### License for UniProtKB
http://www.uniprot.org/help/license
Creative Commons Attribution-NoDerivs License

#### Links to where UniProtKB can be accessed

http://www.uniprot.org/downloads

---

### Ensembl Plants/Gramene

#### How Ensembl Plants/Gramene is used in KBase

Ensembl Plants is a joint project of EBI and Gramene. KBase uses Ensembl Plants/Gramene as a resource for plant genomes, ontology, pathway, interpro, and gene trees. 

#### License for Ensembl Plants
The terms of use of Ensembl data and code are summarised on the following page: http://www.ensembl.org/info/about/legal/index.html.  
The EMBL-EBI terms of use also apply: http://www.ebi.ac.uk/about/terms-of-use.
Gramene terms of use is here: http://www.gramene.org/node/225
Ensembl and Gramene do not place any license restrictions on the data that they produce although they do retain copyright. Their code is explicitly licensed using the Apache v2.0 license.  As noted, their databases may contain information that is subject to third-party constraints of various kinds and users of the Ensembl data and software are solely responsible for determining what these constraints are and complying with them.


#### Links to where Ensembl Plants/Gramene can be accessed

Ensembl Plants: http://plants.ensembl.org/index.html
Gramene: http://gramene.org/

---

### Phytozome

#### How Phytozome is used in KBase

Phytozome is the public portal to JGI's plant genome data and analysis. Currently KBase uses Phytozome as an additional resource for released plant genomes which are not available at Ensembl Plants/Gramene. Phytozome will also be used to provide diversity, expression data and many other data types to KBase in future. 

#### License for Phytozome
Everything is open source. 

#### Links to where Phytozome can be accessed
http://phytozome.jgi.doe.gov/pz/portal.html

---
