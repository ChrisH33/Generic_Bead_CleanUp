# GenericSPRI
One challenge facing laboratory automation is standardising methods. Without a clear framework, new methods proliferate and expand the remit of automation teams. These methods are functionally identical, with only slight differences in pipetting volumes or mix cycles. 

This method aims to address that problem. We have developed a flexible Hamilton method that is capable of performing a range of bead-based cleanups.

### Features
- **Easy Version Control**: By using this method for all clean-ups, it's easy to update methods and ensure every instrument is running the lasest version
- **Pipeline Specificity**: The details of each pipeline run are contained within a JSON file, ensuring each run has the correct parameters for the samples it is processing.

### Requirements
- Hamilton VENUS 4.5.0.7977
- Hamilton Libraries
    - load_instructions
    - HSLML_STARLib
    - HSLSeqLib
    - HSLStrLib
    - HslHamHeaterShakerLib
    - TraceLevel
- Sanger-Created Hamilton Libraries
    - JSONSearch (github.com/ChrisH33/JSONSearch)
    - FindDBPath (github.com/ChrisH33/FindDBPath)
    - HSLGetSerialNumber_WSI (github.com/ChrisH33/HSLGetSerialNumber_WSI)

### Adding new Workflows
Adding new methods or labware should not require any modification to the Hamilton method. All of the variables you might want to change can be found in 'MethodConfig.json'

To add new methods:
1. Copy an existing workflow from the "Pipeline Configs" section and paste it beneath the existing workflows
2. Replace all of the  values with values appropriate to your workflow.
    - Do not rename any of the properties, as this is what the Hamilton method uses to find the correct value.
    - It is recommended you do this a text editor that comprehends .json files, as it will be much easier to identify any mistakes.
5. Add the name of your workflow to "Approved_Pipelines" at the top of the MethodConfig.


### Support
For questions or support, please contact Chris Henderson

    Email: ch33@sanger.ac.uk
    GitHub: ChrisH33
    