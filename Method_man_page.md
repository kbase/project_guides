Every KBase method / SDK module needs to have at least basic documentation in the form of a "man page."
These man pages can be accessed from the Apps & Methods panel in the Narrative Interface by clicking the "more..."
that appears after the app/method description in the input cell or after clicking the "..." that appears next to the method/app name and then the "more" that is thereby exposed.
[screenshot]

The method man page is a no-frills web page that explains how a method is used. It is created from the narrative_method_spec configuration file (display.yaml) for that method.
You can find the URL for the directory in GitHub where the config files live by looking at the bottom of the man page for the "Yaml/Spec location":
[screenshot]

For example, the man page for Build a Metabolic Model (which is a good example to look at) can be seen at https://github.com/kbase/narrative_method_specs/tree/master/methods/build_a_metabolic_model ,
and the config file that it is built from lives in https://github.com/kbase/narrative_method_specs/blob/develop/methods/build_a_metabolic_model/display.yaml .

Method man pages should include:
* A meaningful name that starts with a verb (e.g., "Build Metabolic Model", not "Metabolic Model Builder") that uses Title Case (every important word--excluding articles and prepositions--is capitalized, e.g., "Compare Genomes from Pangenome"). Make sure the name captures what the purpose of the method is--e.g., "Assemble Transcripts with Cufflinks", rather than "Run Cufflinks".
  * If you use the name of an existing tool in your method name, be sure it is spelled and capitalized the way the tool authors want it (e.g., "SPAdes", not "spades").
* A short description ("tooltip" in yaml): a phrase (starting with a verb) that explains the purpose of the method (e.g., "Generate a draft metabolic model based on an annotated genome", not "This method generates [etc]")
* A longer description ("description" in yaml) that includes *why* you'd use the method as well as how. It should mention where you can get input data (e.g., other methods that generate output that can be used as input to this method).
* Other methods, if any, that can consume the results of this one ("suggestions"->"next" in yaml)
* A description of each parameter ("parameters"). Parameters include inputs, outputs, and optional parameters (e.g., score cutoff) that affect the results of running the method. Each parameter should have:
  * a sensisble and consistent name ("ui-name")
  * a brief description ("short-hint") that will appear in the input widget next to the parameter field
  * if needed, a longer description ("description") that pops up when the user clicks the “i" after the parameter description. The description can include HTML markup, such as hyperlinks.
[screenshot]
  * if appropriate, text that will appear in gray inside the parameter box when it's empty, to explain what sort of thing you should put in the box ("placeholder”)
[screenshot]
* An explanation of how to interpret the output results or use the output visualization widget (if not totally obvious)
* Links to any tutorials/narratorials or other useful documentation
* References/links to publications ("publications" in yaml) or additional resources (see the example display.yaml for how to encode references to publications)
* Screenshots ("screenshots" in yaml) of output cells or visualization widgets, if needed (optional)
* Icon for your method ("icon") (optional)
