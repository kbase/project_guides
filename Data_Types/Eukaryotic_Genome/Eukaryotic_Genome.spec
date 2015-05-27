/*
@author chenry,kkeller,sseaver
*/
module KBaseGenomes {

    /*
    Reference to a reads file in shock
    @id shock
    */
    typedef string Reads_ref;
    /*
    Reference to a fasta file in shock
    @id shock
    */
    typedef string Fasta_ref;

    /*
    Class of a genome feature with possible values: coding, non-coding
    */
    typedef string Feature_class;

    /*
    Type of a genome feature with possible values: 
        chr
	contig
	locus
	utr
	intron
	exon
	mrna
	ncrna
	cds
	cdna
	igr (intergenic region)
    */
    typedef string Feature_type;

    /* 
    A region of DNA is maintained as a tuple of four components:

		the feature
		the beginning position (from 1)
		the strand
		the length
		
    We often speak of "a region".  By "location", we mean a sequence
    of regions from other features, whether they be genes, contigs, or chromosomes
    */
    typedef tuple<Feature_id feature_id,int begin, string strand,int length> region_of_dna;
    /*
    A "location" refers to a list of regions of DNA on features
    */
    typedef list<region_of_dna> location;

    /*
    Notation by a curator of the genome object
    */
    typedef tuple<string comment, string annotator, float annotation_time> annotation;

    /*
    Structure for a publication
    */
    typedef tuple<int id, string source_db, string article_title, string link, string pubdate, string authors, string journal_name> publication;
	
    /*
    KBase Feature ID
    @id external
    */
    typedef string Feature_id;
    /*
    Structure for a single feature of a genome

    @optional md5 location function protein_translation dna_sequence protein_translation_length dna_sequence_length publications aliases annotations
    */
    typedef structure {
		Feature_id id;
		list<tuple<Feature_id,int,string,int>> location;
		string class;
		string type;
		string function;
		string md5;
		string protein_translation;
		string dna_sequence;
		int protein_translation_length;
		int dna_sequence_length;
		list<publication> publications;
		list<string> aliases;
		list<annotation> annotations;
		list<Feature_id> parent_features;
    } Feature;

    /*
    Reference to a source_id
    @id external
    */
    typedef string source_id;
    /*
    KBase genome ID
    @id kb
    */
    typedef string Genome_id;
    
    /*
    Genome structure
    	@optional source_id source publications md5 taxonomy gc_content dna_size
    	@metadata ws gc_content as GC content
    	@metadata ws taxonomy as Taxonomy
    	@metadata ws md5 as MD5
    	@metadata ws dna_size as Size
    	@metadata ws genetic_code as Genetic code
    	@metadata ws domain as Domain
	@metadata ws source_id as Source ID
	@metadata ws source as Source
	@metadata ws version as Version
	@metadata ws scientific_name as Name
	@metadata ws length(features) as Number features
    */
    typedef structure {
		Genome_id id;
		string scientific_name;
		string domain;
		int genetic_code;
		int dna_size;
		string source;
		source_id source_id;
		string md5;
		string taxonomy;
		float gc_content;
		string version;
		list<publication> publications;
		list<Feature> features;
		Fasta_ref fasta_ref;
		Reads_ref reads_ref;
    } Genome;
};