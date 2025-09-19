# Generic_Bead_CleanUp

**Generic_Bead_CleanUp** is a flexible Hamilton method created for bead-based cleanups at the Wellcome Sanger Institute.  
It addresses a common problem in laboratory automation: *method proliferation*.  
Too often, new methods are only marginally different yet require separate maintenance.  
This framework standardises cleanup methods, making them easier to maintain, extend, and deploy across multiple pipelines.

---

## Features
- **Centralised Version Control**  
  One method for all cleanups, ensuring updates are rolled out consistently across instruments.
- **Pipeline-Specific Parameters**  
  Run details are stored in a JSON file, guaranteeing that each workflow uses the correct parameters for its samples.
- **Extensible Workflows**  
  New pipelines and labware can be added without modifying the Hamilton method itself.

---

## Adding New Workflows
All configurable variables are defined in `\.config`.  
To add a new workflow:

1. Create a copy of `Example.json`.
3. Update the values to match your workflow.  
   - **Do not rename properties**  
   - Use a JSON-aware text editor to minimise errors.
4. Add the name of your workflow to `"Approved_Pipelines"` at the top of `LabwareInstrumentConfig.json`.

---

## Requirements

### Hamilton
- VENUS 4.5.0.7977  
- Required libraries:  
  - `load_instructions.smt`  
  - `HSLStrLib.hsl`  
  - `HSLSeqLib.hsl`  
  - `HSLML_STARLib.hsl`  
  - `HslHamHeaterShakerLib.hsl`  
  - `VirtualLabware_V2.hsl`  
  - `HSLDevLib.hsl`  
  - `ASWStandard\TraceLevel\TraceLevel.hsl`  
  - `CheckCarrierPresence (All)\CheckCarrierPresenceAbsence.smt`  
  - `Nested Tip Racks (All)\NTRDirectUse_WGSPCRXP\NTRDirectUse_WGSPCRXP.smt`  

### Sanger
- Required libraries: 
    - `WSI\JSONSearch\JSONSearch.smt`  
    - `WSI\HSLGetSerialNumber\HSLGetSerialNumber_WSI.hsl`  

👉 Sanger-created libraries can be found here: [Hamilton-Submethod-Libraries](https://github.com/ChrisH33/Hamilton-Submethod-Libraries)

---

## Support
For questions or support, contact:  

- **Chris Henderson**  
  📧 ch33@sanger.ac.uk  
  🧑‍💻 [GitHub: ChrisH33](https://github.com/ChrisH33)  
  💬 [Slack](https://sanger.enterprise.slack.com/team/U042KMP16KW)
