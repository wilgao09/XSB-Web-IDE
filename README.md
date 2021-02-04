# What is this?

Forked IDE from [here](https://github.com/quantumech3/XSB-Web-IDE). The goal for this fork is to create a less client heavy version of the IDE. As of forking, the current issues are as follows:

 - Mobile clients fail to load (further investigation required)
 - Memory allocation (2 instances of XSB, each @ 1GB)
 
We will (try to) fix the above issues by:

 - Reducing client load 
 - Limit memory usage (maybe 512 MB?)
 - Replace Monaco with CodeMirror 