## High Level Product Description Template

For most types of products, product descriptions should include the following:

### Brief User Story/Description of App or Workflow
A brief (a single paragraph for small apps) summary of what the app is intended to do for the user. Do not include scientific justifications, review of competitors, etc... The developer(s) working on the implementation assume that the broader case for the product has been dealt with, and only wants to get an idea of what the app should be doing.

### Links to source for downloading the tool(s) to be wrapped
Where is the source code for the app that needs to be developed? Preferably link to something like the github repo instead of a static tarball.

### Folder containing an end to end run of the tool(s) being wrapped.
The developer should be able to fully replicate an example run to validate that they have complete specifications, as well validating that the wrapped app produces identical results. This should be stored in an anonymously FTP accessible directory, or in a KBase Box folder
1. Example source files used as inputs
1. A script that runs the tool against the input files, with all required command line arguments, as well as the commands to generate desired reports against the output files
1. The relevant output files from running B - this includes the output from the tool, as well as any reports that are created to assess the quality of the output files

### A clear description of how the input and output files map into existing KBase data types, or else a description of any new data types that need to be developed.
1. Any new data types needs to be explained and the relationship of the new types to existing data types must be documented
1. New data types cannot simply be wrappers for output files
1. Appropriate file types that can be uploaded/downloaded into/out of the new type must be documented along with example files for testing upload/download

### A diagram of input data types and output data types
A drawing of the inputs and outputs should be included. For simple flows this can be textual, but for more complex multi-step workflows it should be considered a requirement



### Narrative Mockup
Mockups of the input and output must be included that show the required and optional fields, as well as the what the output report should look like

## Example Product Description

An [example product description](ExampleProductDescription.pdf) has been included in this repo.