A brief listing of the key features existing in this service. 
    
    Originally the RNASeq service was developed with Hadoop/Grid Engine infrastructure as the backend. With that deploy we had the following functionality in place for RNA Seq.
     
     1 ) Compute Gene Expression:

Once the samples are loaded, the user should be able to see the RNASeq samples loaded through the uploader in the Narrative Workspace.
Inputs to the narrative are the RNASeq sample ids and the reference genome. This method will then align the reads to the reference genome, assemble the aligned reads to forms transcripts and estimate their abundances
Outputs from the method are the KBaseExpression.RNASeqSampleAlignment, KBaseExpression.ExpressionSample workspace objects.

      2) Plot Gene Expression Histogram 
    
    This method takes the expression sample from the previous method and generate a histogram of expression values.
    
      3) Identify Differential Expression

Once we have the gene expression profiles for individual samples , the next step is to test for differential expression and regulation in RNA-Seq samples.
This method takes as many  KBaseExpression.ExpressionSample objects and their respective KBaseExpression.RNASeqSampleAlignment objects to calculate the differential Expression.
Output from this method is the KBaseExpression.RNASeqDifferentialExpression

     4) Create Expression Series
    
Select as many  gene expression profiles (KBaseExpression.ExpressionSample objects ) to create an Expression Series object (KBaseExpression.ExpressionSeries ) to further extend their analysis through the coexpression narrative and visualize the coexpressed gene networks.

     5) Generate Data table 

    Build an expression data table for the Expression series data across the multiple samples. 

   

 6) Filter Expression Data table 

    Filter the Expression data table built in the previous step based on the differences in the high and low expression values

7) Render Heat Map

Generate heat map widget using the filtered gene expression data table.

Due to unavailability of the ORNL GRID engine cluster and the better support for AWE distributed computing in KBase, we are comfortable to move our service to KBase Shock/AWE based service. This removes the need of the Hadoop hardware and the Grid engine hardware support and also makes our service to be a standard KBase service.

New features that we are proposing to introduce in this service

    We propose to migrate all the existing functionality of RNA Seq from our Hadoop / Grid Engine based backend to the Shock/ AWE based service. This will include all the above functionality and a few additional features listed below.
List of Methods in the new RNASeq service  :


Short Term :
 
Upload RNA Seq samples into Workspace data type.
       
    RNASeq samples are essentially fastq files with the sampled reads information. Currently we have 3 object types in KBase for loading fastq files. 
    KBaseAssembly.SingleEndLibrary
    KBaseAssembly.PairedEndLibrary
    KBaseExpression.RNASeqSample
    KBaseExpression.VariationSample

These are originally created to accommodate the different metadata information for the different services. It is essential to build a generic data model for the fastq files under one module to be used in the different services ( RNA Seq, Variation, Communities )
     
 App 1 :  Quantify Known Transcripts 
Method 1:    Align RNA Seq Reads 
     This method  will align reads RNA seq  using  a splice junction mapper  Tophat with the options to allow the user specified mismatches, uniqueness in mapping and the read length to map. This method takes the fastq files and reference genome  in fasta format as input and produces alignment files in bam format. Many services will have alignment as one of their initial steps. It will be useful to have a more generic data type for bam alignment files from different services.

Output :  KBaseExpression.RNASeqAlignment object.     
Note : Need to make KBaseExpression.RNASeqAlignment object generic data model for all services. 

Method 2:    Visualize bam alignments.
Pie chart to visualize the bam alignment files. 

    


Method 3:    Calculate Gene Expression
    This method takes the bam alignment files as input , reference genome and internally queries the CDM to get the annotation for the reference genome, computes gene expression  and creates a KBaseExpression.ExpressionSample object.
  
            Method 4:    Plot Gene Expression Histogram
        This method takes the KBaseExpression.ExpressionSample and builds a histogram.

 App 2 : Identify Differential Expression 
           Method 5:    Merge transcripts
        
Method 6:     Identify Differential Expression 
    
    Method 7 : View RNA Seq experiment heatmap
        
   Shorter term :
      The app identify differential expression will support Cuffdiff in the near term.

   Longer term :
      Add DESeq and edgeR as choices of methods to identify differential expression. The limitations in adding these tools are to parse the differently formatted output files, normalize them and to produce meaningful graphs and visualizations.

Option1 :  To visualize how samples can be classified based on expression markers? Then try a unsupervised hierarchical clustering heatmap of the 500 genes with the most variance across all your samples.

     2)  Option 2: To visualize what sample groups there are in your data? 
Make a 3d scatter plot of the first 3 principal components (PCA-analysis). 

    3)  Option 3: To visualize the  genes that are differentially expressed across the samples
  Use these genes to make a clustering heatmap




Longer Term:

Methods

Quality control for the RNASeq Samples

Landing pages and widgets for the RNASeq Service Datatypes :


RNASeqSample: 

Provide statistical graphs and reports on the quality of the raw sequencing data. This page will be a useful resource to check the quality of your RNA-seq data before analysis. Also display the metadata for the RNASeq sample loaded into the workspace.


Landing page  for RNASeqDifferentialExpression:

Visual representation of the differential  analysis results are provided, including interactive tabular and a heat map. 

Assess the distributions of FPKM scores across samples - density plot 


Displaying a table of the top 100 differentially expressed genes to the pathways. Not sure how to visualize this or may be  a simple table format.

Functionality to create gene tracks to visualize transcript-level structures in their genomic context.  ( Longer term ) 

3) Timelines, service dependencies, platform dependencies and other changes needed to resurrect this service in the existing platform. 
            
The restructuring requires alter/rewriting the server scripts for all the above functions, design, alter and add additional workspace data types, design the spec files to auto generate the client library files using typecompiler. We had an initial discussion with Matt, Jason to fit in the input fastq files for RNASeq with metadata to a more generic datatype.

    Dependencies for the current backend service proposed will include:
 
kbwf_common
    typecomp
    user_and_job_state
    workspace_deluxe
    awe_service
    shock_service
    handle_service
    auth
            kb_seed
    

Timelines, service dependencies, platform dependencies and other changes needed to develop this service further in view of the ongoing/anticipated changes in the platform that you are aware of.
    
    Most RNASeq experiments, involve analysing multiple samples over  different conditions or timepoints. In order to avoid huge data copying over the network to the awe clients, it will be helpful to have the data available at the NERSC cluster. This will reduce the data copy time and improve the running times of RNASeq experiments.

DataModels to be modified

Building a generic data model for fastq files. 
Enhance the genome object to have more details to support the basic formats fasta , gtf formats to avoid querying the CDM for every request.

Narratives: 
Use RNAseq to identify novel transcripts. 
        We can easily create this app with just adding another mode to the existing RNASeq pipeline. This requires rework on the existing data models KBaseExpression.ExpressionSample to allow for new transcript ids. As this service will produce novel transcripts which will not have an equivalent Kbase CDS id.

Differential expression under a given biological condition across closely related and distant related species  - one of the longer term narratives.
Tissue specific differential expression under two or more conditions/treatments. 
Use RNASeq data for identification of exon, introns, mapping of their boundaries and the identification of 5’ and 3’ UTRs. 
Use RNASeq for identification of TSS
Use RNASeq for identification of new splicing variants
Use RNASeq data for SNP discovery
Build coexpression networks

Sample Visualizations for RNASeq service :

The first step in RNA Seq is to align the reads to a reference genome. Once the alignment files (bam files) become available after the first step, we can visualize the alignments in pie chart. 



      2)  Functions to visualize the Differential expression data.
    
        Once we ran the differential expression on the expression samples, an user may be interested easily visualize and create publication-ready figures of  the RNA-Seq data while maintaining appropriate relationships between connected data points.

A good place to begin is to evaluate the quality of the model fitting. Overdispersion is a common problem in RNA-Seq data. The user can visualize the estimated overdispersion for each sample as a quality control measure by a dispersion plot



Individual Pairwise comparisons can be visualized using a scatter plot. You must specify the sample names to use for the x and y axes.





Here are more additional features suggestions for RNA-seq service: 

i) RNAseq mapping options - mismatch, uniqueness of mapping, read length to map - added to the new feature list.
ii) Evaluate mapping statistics - added to the new feature list
iii) Generate both gene levels and transcript level expression values - 
iv) Additional differential expression analysis options - R packages DESeq and /or edgeR - one of our longer term goals
v) QC step for replicates following FPKM calculation; Pearson correlation based tree to identify outliers. -  one of our longer term goals.
