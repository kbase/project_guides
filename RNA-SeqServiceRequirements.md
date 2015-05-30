A brief listing of the key features existing in this service. 
	
Originally the RNASeq service was developed with Hadoop/Grid Engine infrastructure as the backend. 
With that deploy we had the following functionality in place for RNA Seq.

 1 ) Compute Gene Expression:

Once the samples are loaded, the user should be able to see the RNASeq samples loaded through the uploader 
in the Narrative Workspace.
Inputs to the narrative are the RNASeq sample ids and the reference genome. This method will then align the reads to the reference genome, assemble the aligned reads to forms transcripts and estimate their abundances
Outputs from the method are the KBaseExpression.RNASeqSampleAlignment, KBaseExpression.ExpressionSample workspace objects.

2) Plot Gene Expression Histogram 
	
This method takes the expression sample from the previous method and generate a histogram of expression values.
	
3) Identify Differential Expression

Once we have the gene expression profiles for individual samples , the next step is to test for differential expression and regulation in RNA-Seq samples.
This method takes as many  KBaseExpression.ExpressionSample object and the corresponding  KBaseExpression.RNASeqSampleAlignment objects to calculate the differential Expression.
Output from this method is the KBaseExpression.RNASeqDifferentialExpression

4) Create Expression Series
	
Select as many  gene expression profiles (KBaseExpression.ExpressionSample objects ) to create an Expression Series object (KBaseExpression.ExpressionSeries ) to further extend their analysis through the coexpression narrative and visualize the coexpressed gene networks.

5) Generate Data table 

Build an expression data table for the Expression series data across the multiple samples. 

6) Filter Expression Data table 

Filter the Expression data table built in the previous step based on the differences in the high and low expression values

7) Render Heat Map

Generate heat map widget using the filtered gene expression data table.

Due to unavailability of the ORNL GRID engine cluster and the better support for AWE distributed computing in KBase, we are 
comfortable to move our service to KBase Shock/AWE based service. This removes the need of the Hadoop hardware and the Grid 
engine hardware support and also makes our service to be a standard KBase service.

New features that we are proposing to introduce in this service

We propose to migrate all the existing functionality of RNA Seq from our Hadoop / Grid Engine  based backend to the Shock/ AWE based service. I had already started working on the backend functionality for the methods This will include all the above functionality and a few additional features listed below.

List of Methods in the new RNASeq service  :
 
Upload RNA Seq samples into Workspace data type.

RNASeq samples are essentially fastq files with the sampled reads information. 
Currently we have 3 object types in KBase for loading fastq files. 

KBaseAssembly.SingleEndLibrary
KBaseAssembly.PairedEndLibrary
KBaseExpression.RNASeqSample
KBaseExpression.VariationSample

These are originally created to accommodate the different metadata information for the different services. It is essential to build a generic data model for the fastq files under one module to be used in the different services ( RNA Seq, Variation, Communities )

App 1 :  Quantify Known Transcripts 
Method 1:	Align RNA Seq Reads 
This method  will align reads RNA seq  using  a splice junction mapper  Tophat with the options to allow the user specified 
mismatches, uniqueness in mapping and the read length to map. This method takes the fastq files and reference genome in fasta
format as input and produces alignment files in bam format. Many services will have alignment as one of their initial steps. 
It will be useful to have a more generic data type for bam alignment files from different services.

Input: KBaseExpression.RNASeqSample
Output :  KBaseExpression.RNASeqAlignment object. 	
Note : Need to make KBaseExpression.RNASeqAlignment object generic data model for all services. 

Method 2:	Visualize bam alignments.
Pie chart to visualize the bam alignment files. 

Input :   KBaseExpression.RNASeqAlignment  or  (alignment workspace object )
Output  :  Pie chart widget 

Method 3:	Calculate Gene Expression
	This method takes the bam alignment files as input , reference genome and internally queries the CDM to get the annotation for the reference genome, computes gene expression  and creates a KBaseExpression.ExpressionSample object.
Input :  Genome object , KBaseExpression.RNASeqSampleAlignment
Output : KBaseExpression.ExpressionSample
  	
Method 4:	Plot Gene Expression Histogram
	This method takes the KBaseExpression.ExpressionSample and builds a histogram.
Input :   KBaseExpression.ExpressionSample
Output : Histogram widget 

App 2 : Identify Differential Expression 

Method 5:	Merge transcripts
	Merge the assembled transcripts of the individual samples to a single merged transcript. 
Input :   List of KBaseExpression.ExpressionSample objects
Output :  Merged transcriptome object ( RNASeq specific object type. Need to design this object ) 

Method 6: 	Identify Differential Expression 
 
Input :   List of KBaseExpression.ExpressionSample objects , List of KBaseExpression.RNASeqAlignment objects
Output :  KBaseExpression.RNASeqDifferentialExpression ( working on prototyping this object. Specific to RNASeq service. )  , Landing page for differential expression object 
( see dependencies section Landing page )

Method 7 : View RNA Seq experiment heatmap

Input : KBaseExpression.DifferentialExpression , genes of interest , threshold. if no options specified select the top 500 genes with the most variance.

Output : Heatmap widget 

3) Timelines, service dependencies, platform dependencies and other changes needed to resurrect this service in the existing platform. 
        
The restructuring requires alter/rewriting the server scripts for all the above functions, design, alter and add additional workspace data types, design the spec files to auto generate the client library files using typecompiler. We had an initial discussion with Matt, Jason to fit in the input fastq files for RNASeq with metadata to a more generic datatype.

Most RNASeq experiments, involve analysing multiple samples over  different conditions or timepoints. In order to avoid huge data copying over the network to the awe clients, it will be helpful to have the data available at the NERSC cluster. This will reduce the data copy time and improve the running times of RNASeq experiments.

Dependencies :

Core Datatypes:
     		
Extending the KBaseGenome object or an other objects to include more all feature types
transcript, coding & non-coding, exon, intron, TSS, promoter. 
	
Existing Genome model features: CDS, mRNA, locus
New feature needed : transcript, exon, TSS, promoter. 

Direct way to get the external source id for a KBase feature id from the workspace object. 
Currently query the CDM for external source ids.

2) Generic  datatype for fastq files with metadata information . 
Currently we have multiple datatypes for Fastq files ( SingleEnd and PairedEnd )
	
Existing objects :

	KBaseAssembly.SingleEndLibrary
	KBaseAssembly.PairedEndLibrary
	KBaseExpression.RNASeqSample
	KBaseExpression.VariationSample

Suggestion :  Include KBaseAssembly module to KBaseExpression module and modify the KBaseExpression.RNASeqSample 
objects with KBaseAssembly.SingleEndLibrary , KBaseAssembly.PairedEndLibrary types  instead of a string shock handle type.


3)  Generic object for BAM alignments.

Existing  objects: KBaseExpression.RNASeqAlignment 

Suggestion : Create a basic bam alignment object. Include that type in KBaseExpression.RNASeqAlignment with the associated metadata  instead of a string shock handle.

Note  1:  For 1 , 2  and 3   need help from Data team for design, review of data type  and acceptance.
 
4)  KBaseExpression.ExpressionSample  - Already exists in KBase .

5)  New object creation for KBaseExpression.RNASeqDifferentialExpression. Currently working on a prototype for the new differential expression object.

6)  MAK.FloatDataTable for visualization widgets. Already exists in KBase.

UI / UIX :

Widgets for visualizing RNASeq outputs:

  1) Pie chart: Not sure if exists in KBase. Workspace object Type : ? 

  2) Histogram:  Exists in KBase , Workspace object Type : ? 

  3) Heatmap: Exists in KBase , Workspace  object Type : MAK.FloatDataTable

  4) Scatterplot:  Not sure if already exists in KBase , Workspace  object Type :  MAK.FloatDataTable

  5) Table:   Already exists in KBase ,  Workspace object Type  : ?  

  6) Scatter Matrix  : Not sure if exists in KBase ( to visualize individual pairwise gene expression comparisons in a grid )  Note:   If not immediately, it is a good to have feature in the Longer run.

Landing pages
  
  DIfferential Expression:  

  1) 	Table of Samples and experiment conditions
  2)	 Heatmap widget for the experiment 
  3) 	 Table of  top 100 upregulated genes to their pathways.
  4) 	 Grid of Scatter plots 
 
Note 2:  Many users would be interested using the most popular R packages for differential expression analysis  in RNASeq like CummeRbund , DESeq and edgeR. Unsure about , how to be able to leverage the  visualization methods from these R packages in KBase. Possible ways are to have precomputed SVG  images as workspace objects ( if wanted to be handled in the backend ) or do the necessary compute on the frontend.   Will need inputs from the service team  and data team to handle this appropriately ???

Note 3:  Will need support from the UI/UIX team to identify and develop the newer widgets , landing pages, identify workspace object types for widgets that are available in KBase and marked as  ?  under the Widgets paragraph. 

Dependent KBase modules : 
	kbwf_common
	typecomp
	user_and_job_state
	workspace_deluxe
	awe_service
	shock_service
	handle_service
	auth
	kb_seed


Future Narratives around RNASeq: 

	Use RNAseq to identify novel transcripts. 
  		We can easily create this app with just adding another mode to the existing RNASeq pipeline. This requires rework on the existing data models KBaseExpression.ExpressionSample to allow for new transcript ids. As this service will produce novel transcripts which will not have an equivalent Kbase CDS id.
	Use RNASeq data for identification of exon, introns, mapping of their boundaries and the identification of 5’ and 3’ UTRs. 
	Use RNASeq for identification of TSS
	Use RNASeq data for SNP discovery.
