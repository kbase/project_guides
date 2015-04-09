# KBase External Data Source Details

This document should be used for describing each KBase external data source in the following ways:

- How the external data source is being used in KBase, and any references to existing documentation and source code in the KBase github project that describes this in more detail.
- What the license policy is of the data.
- What version or versions (if more than one copy of the data is used) are being used.
- A link or links to where the data can be accessed.
- A link or links to the documentation for this data.

## Data Sources

### ModelSEED

#### How ModelSEED is used in KBase

ModelSEED was the basis for the biochemistry database and the metabolic model reconstruction services in KBase. The KBase biochemistry database was initially based on a reformatted load of the entire ModelSEED biochemistry database. The KBase database has sense undergone additional curation and manual addition of reactions from other data sources, namely published manuscripts and published metabolic models.  

#### License for ModelSEED data

All data specific to ModelSEED is released under the ModelSEED Public License:
https://github.com/ModelSEED/ModelSEED/blob/master/LICENSE.TXT

However, some data in the ModelSEED is derived from other sources (e.g. KEGG), and that data carries it's own potential licensing restrictions.

#### Versions of ModelSEED utilized

KBase loaded the 2012 version of the ModelSEED database.

#### Links to where ModelSEED can be accessed

http://seed-viewer.theseed.org/seedviewer.cgi?page=ModelView

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

KEGG data was utilized for the ModelSEED project under the pre 2012 academic license. It is unclear at this time whether a license is required for the limited extent to which KEGG data is exposed in KBase.

#### Versions of KEGG utilized

KEGG data in the ModelSEED was last updated in April 2012.

#### Links to where KEGG can be accessed

http://www.genome.jp/kegg/

