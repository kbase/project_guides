# Rationale for Eukaryotic Genome data type
## High-level Rationale
-	Plant sequence data may consist of being a number of classes of features (see next section). We wish to be flexible with the data that is available in the data object, meaning we can have any number (zero or more) of each of these classes in a single object instance. We can't expect to use the current Genome object, in a flexible manner, and have it work with any genome-based method in the current narrative environment.
-	The structure of eukaryotic genes and their alternative transcripts/proteins is more complex, and needs to be captured in a manner that the community can explore/visualize.
-	The Plants domain will need to iteratively expand on, and improve, such an object in response to the needs of the plant community, and doing so with an object that's exclusive to the domain, would be less disruptive to other domains.

## Rationale for each of the feature classes:  
1.	**Chromosome**
2.	**Contigs** Genome sequencing and assembly is an imperfect science and as such, many plant genomes, whilst having large, well-defined chromosomal contigs may also come with a set of smaller regions for which a 'home' could not be found, but which in turn can contain genes.
3.	**Locus**
4.	**Untranslated region (UTR)**
5.	**Intron**
6.	**Exon** A eukaryotic gene is recognized to have several components (UTRs, introns, exons). The determination of where these regions begin and end is important, particularly in the case where alternative transcripts are possible, which are a result of different combinations of exons.
7.	**mRNA** The RNA sequence of a transcribed gene, still contains UTRs, introns, and exons. The users may want the unedited sequence of a gene's transcript.
8.	**non-coding RNA** The RNA sequence of a transcribed gene that will not be translated, there's a range of types such as tRNA, rRNA, miRNA, siRNA, snRNA. These play important roles in plant biology, and users may want to see them.
9.	**Coding Sequence (CDS)** The RNA sequence of the combined exons that is directly translated into the protein. 
10.	**cDNA** The DNA sequence that has been reverse-translated from a peptide or RNA sequence
11.	**Intergenic regions** The position and sequence of several regions located upstream or downstream of a gene, particularly where pertinent to the regulation of the gene, is important. These include transcription start sites (TSS), promoters, transcription factor binding sites (TFBS) and chromosomal elements.

![alt text](https://raw.githubusercontent.com/samseaver/project_guides/Genome_Object_Documentation/Data_Types/Eukaryotic_Genome/Eukaryotic_Gene_Structure.png)
