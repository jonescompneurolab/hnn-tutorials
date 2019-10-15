<!-- pandoc -f markdown -t html -o tour_gui.html tour_gui.md -->

# Tour of the Graphical User Interface (GUI)

Here we provide an overview of the major GUI components, and provide a description of all the parameters that the GUI provides.

This is a display of the GUI after running a simulation that produces an event-related potential (ERP; see ERP tutorial for more information on that simulation’s details).

<div class="stylefig" style="max-width:650px;">

### Figure 1

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image21.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image21.png" alt="image21" /></a>
</div>

The top of the GUI contains a standard menu and buttons for setting parameters, running simulations, and viewing the simulation/experimental data output.

The bottom of the main GUI window shows a list of the simulations that have been run. As you run more simulations, the average dipole signal from each simulation gets overlaid in the plot, as shown below.


<div class="stylefig" style="max-width:650px;">

### Figure 2

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image15.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image15.png" alt="image15"/></a>

</div>

In the example above, the newest simulation’s dipole is drawn in a solid line, while previously run simulations are drawn using dotted lines. You can select/highlight a particular simulation by clicking on the different simulations populating the list, or from menu Simulation -> Go to Previous Simulation (Ctrl+Z), Go to Next Simulation (Ctrl+Y). Cycling between simulations is useful for comparing how different model parameters influence the generated dipole signal.

You can also remove the currently selected simulation from view by clicking the “Remove Simulation” button, if that particular simulation is no longer of interest. To remove all simulations from display, click on the Simulation menu -> Clear simulation(s). This is useful if you change the MEG/EEG pattern you are modeling (e.g. event related potential vs. ongoing rhythmic activity).

In the window shown below, there are several schematics to provide intuition on the model’s structure, and to provide quick access to the model parameters. To access the model parameters from that window, click on any of the buttons. Below, we describe all the model parameters in detail.

<div class="stylefig" style="max-width:650px;">

### Figure 3

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image29.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image29.png" alt="image 29"/></a>

</div>


## Preliminaries: Parameter Files

Before delving into the details of the GUI, we first provide an overview of the parameter files used by HNN. Parameter files are text-based and contain all the key parameters needed to run a model. These parameters include synaptic inputs, neuronal biophysics, and local network connectivity. HNN reads/writes these parameter files so you don’t have to edit them yourself.

In order to facilitate effective modeling, we have provided a set of text-based parameter files that allow you to replicate event related potentials (ERPs), and alpha/beta/gamma rhythms. HNN can load the parameter files, allowing you to replicate the dynamics, see the critical parameter values that are responsible for the observed dynamics, and then modify the parameter files/values to observe the effect on dynamics. Parameter files are stored in the param subdirectory and can be viewed in any text editor. To load these parameter files into HNN, press the Set Parameters from File button, select the parameter file, and press enter. HNN will parse the file and display the values in the GUI. Then, running the simulation will use these parameter values.



## Setting Parameters

To view and set the parameters that control the simulation, press the Set Parameters button from the main GUI window. This will bring up the following dialog:

<div class="stylefig" style="max-width:250px;">

### Figure 4

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image33.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image33.png" alt="image33"/></a>

</div>

Pressing each button on this dialog brings up a new dialog box with more adjustable parameters. We will go through each below. The next thing to note is the Simulation Name. This should be a unique identifier for any particular simulation you run. HNN also uses this variable to determine where to save the output files. In the dialog displayed, note that the value is set to default. This is because the default.param file was loaded. We suggest you change this name when you make changes to the parameters, before running a new simulation.

Here is an example of the data directory and files saved after running the simulation specified in default.param.

<div class="stylefig" style="max-width:650px;">

### Figure 5

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image23.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image23.png" alt="image23"/></a>

</div>

Note that the directory path is /home/hnn/data/default, corresponding to the default Simulation Name parameter specified in the GUI. Also note the individual files present in the window:

1.  default.param - a backup copy of the param file used to run the simulation
2.  dpl.txt - normalized dipole in units of nAm; 1st column is time; 2nd column is layer 2 dipole; 3rd column is layer 5 dipole; 45h column is aggregate dipole from layers 2 and 5
3.  i.txt - currents from the cells
4.  param.txt - a machine-readable representation of all parameters used to run the simulation
5.  rawdpl.txt - un-normalized dipole; same columnar layout as dpl.txt
6.  rawspec.npz - spectrogram from the dipole saved in numpy format; you can use numpy to load this file (note that this file is only produced either when using rhythmic inputs or explicitly asking HNN to save the spectrogram; for the ERP shown above, no spectrogram is saved)
7.  spk.txt - a list of cell identifiers and spike times

We provide these files for advanced users who want to load them into their own analysis software, and also to allow HNN to load data after a simulation was run. For example, if you close HNN and then restart it, load a param file from a simulation that was already run, HNN will load and display the data.

### Run Parameters

Pressing the Run button on the Set Parameters dialog box brings up the following dialog, enabling you to view/change the following displayed parameters.

<div class="stylefig" style="max-width:350px;">

### Figure 6

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image22.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image22.png" alt="image22"/></a>

</div>

*   Duration (ms) - this sets the simulation duration in milliseconds.
*   Integration timestep (ms) - this sets the fixed timestep that the NEURON simulator uses to perform integration; smaller values take longer to run but potentially offer more accurate simulations; we recommend using the default value of 0.025 ms.
*   Temperature (C) - temperature used in simulation
*   Trials - specifies the number of trials to run; note that the simulation parameters across trials are identical except for inputs which are randomized across trials.
*   Firing threshold (mV) - neuronal membrane  potential at which the neuron fires an action potential
*   NumCores - this specifies the number of cores that NEURON will use to run a simulation in parallel; we suggest using the default, which HNN automatically determines based on your computer hardware.

Clicking on the Analysis tab brings up the following parameters.

<div class="stylefig" style="max-width:350px;">

### Figure 7

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image26.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image26.png" alt="image26"/></a>

</div>

*   Save figures - whether to save figures of model activity when the simulation is run; if set to 1, figures are saved in simulation output directory.
*   Save spectral data - Whether to save spectral simulation spectral data - time/frequency/power; if set to 1, saved to simulation output directory. Note: when using rhythmic inputs, spectrograms will be saved whether or not this is set to 1.
*   Max spectral frequency (Hz) - Maximum frequency used in dipole spectral analysis.
*   Dipole scaling - Scaling used to match simulation dipole signal to data; implicitly estimates number of cells contributing to dipole signal.
*   Dipole Smooth Window (ms) - Window size (ms) used for Hamming filtering of dipole signal (0 means no smoothing); for analysis of ongoing rhythms (alpha/beta/gamma), best to avoid smoothing, while for evoked responses, best to smooth with 15-30 ms window.
*   Save somatic Voltages - to save the somatic voltage from all neurons to an output file set value to 1; enables drawing somatic voltage from HNN View menu after simulation is run with this setting turned on

Clicking on the Randomization Seeds tab brings up the following parameters.

<div class="stylefig" style="max-width:350px;">

### Figure 8

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image19.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image19.png" alt="image19"/></a>

</div>

All these parameters are random number generator seeds for the different types of inputs provided to the model. Varying a seed will still maintain statistically identical inputs but allow for controlled variability.

*   Random number generator seed used for rhythmic proximal inputs.
*   Random number generator seed used for rhythmic distal inputs.
*   Random number generator seed used for Poisson inputs.
*   Random number generator seed used for Gaussian inputs.
*   Random number generator seed used for evoked proximal input 1.
*   Random number generator seed used for evoked distal input 1.
*   Random number generator seed used for evoked proximal input 2.
*   Random number generator seed used for evoked distal input 2.

### Cell Parameters

Pressing the Cell button on the Set Parameters dialog box brings up the following dialog, enabling you to view/change the cell parameters associated with geometry, synapses, and biophysics for layer 2/3 and layer 5 pyramidal neurons.

These parameters control the cell’s geometry:

<div class="stylefig" style="max-width:250px;">

### Figure 9

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image4.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image4.png" alt="image4"/></a>

</div>

and include lengths/diameters of individual compartments. Although not strictly related, we have also included axial resistivity and capacitive in this panel.

Clicking on the L2/3 Pyr Synapses tab allows you to modify the postsynaptic properties of layer 2/3 pyramidal neurons:

<div class="stylefig" style="max-width:250px;">

### Figure 10

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image25.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image25.png" alt="image25"/></a>

</div>

These include the excitatory (AMPA/NMDA) and inhibitory (GABAA/GABAB) reversal potentials and rise/decay exponential time-constants.

Clicking on the L2/3 Pyr Biophysics tab allows you to modify the biophysical properties of layer 2 pyramidal neurons, including ion channel densities and reversal potentials:

<div class="stylefig" style="max-width:250px;">

### Figure 11

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image27.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image27.png" alt="image27"/></a>

</div>

To modify properties of the layer 5 pyramidal neurons, click on the right arrow to access the relevant tabs (beginning with L5 Pyr).

### Local Network Parameters

Neurons in the model are arranged in three dimensions. The XY plane is used to array cells on a regular grid (arbitrary units) while the Z-axis specifies cortical layer (position in microns).

<div class="stylefig" style="max-width:350px;">

### Figure 12

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image24.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image24.png" alt="image24"/></a>

</div>

This 3D visualization of the model is rotated to allow easier viewing. The top and bottom represent supra- and infragranular cortical layers. In this figure, the following color code is used for the different cell types in the model– red: layer 5 pyramidal neurons; green: layer 2/3 pyramidal neurons; white: layer 2/3 interneurons; blue: layer 5 interneurons.

<div class="stylefig" style="max-width:350px;">

### Figure 13

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image18.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image18.png" alt="image18"/></a>
</div>

The figure above shows a schematic of network connectivity. The blue cells are pyramidal neurons, while the orange circles represent the interneurons. The lines between neurons represent local synaptic connections. Lines ending with a circle are excitatory (AMPA/NMDA) synapses, while lines ending with a line are inhibitory (GABAA/GABAB) synapses.

Pressing the Local Network button on the Set Parameters dialog box brings up the following dialog, enabling you to view/change the local network microcircuit parameters including number of cells and synaptic weights between cells of specific types. These parameters control the number of pyramidal cells in the X and Y directions per cortical layer:

<div class="stylefig" style="max-width:350px;">

### Figure 14

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image34.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image34.png" alt="image34"/></a>
</div>

Note that the pyramidal cells are arranged in the X-Y plane, so the number of cells in a layer is the product of the number along the X and Y directions. The number of interneurons per layer is adjusted to be ⅓ the number of pyramidal neurons in an equally distributed configuration.

To adjust synaptic weights onto a particular cell type, click the corresponding tab in the dialog. For example, the following dialog allows viewing/setting the synaptic weights onto layer 2/3 pyramidal neurons:

<div class="stylefig" style="max-width:350px;">

### Figure 15

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image30.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image30.png" alt="image30"/></a>
</div>

In this example, AMPA/NMDA weight are the excitatory synaptic weights, while GABAA/GABAB are the inhibitory synaptic weights. All weights are specified in units of conductance (![](https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image1.png)). Note that the synaptic weight, w, between two cells is scaled by the distance between the two cells through the following equation:![](https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image2.png), where wis the weight specified in the dialog, dis the distance between the cells in the X-Y plane (distance is in arbitrary units), and λ is a spatial length constant which is 3 or 20 (λ is also in arbitrary units) when a presynaptic cell is excitatory or inhibitory, respectively, in order to have shorter spread of excitation relative to inhibition.

Excitatory (E) and inhibitory (I) tone within the network is a major factor influencing network dynamics. The following dialog, accessible with the Synaptic Gains button from the main Set Parameters dialog, facilitates scaling of E->E, E->I, I->E, and I->I weights, without having to adjust the weights between specific types of cells.

<div class="stylefig" style="max-width:150px;">

### Figure 16

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image13.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image13.png" alt="image13"/></a>
</div>

In this dialog changing the 1.0 to other values and pressing OK will multiply the appropriate weights displayed in the Local Network Parameter dialog. For example, setting E->E to a value of 2.0 will double the weights between all pairs of excitatory cells. Changing a value and then pressing Cancel will produce no effect.

### Synaptic Inputs - Proximal vs. Distal

For both rhythmic and evoked synaptic inputs (described below) we use the terms proximaland distal to refer both to the origin of the inputs as well as the laminar target within the neocortical microcircuit. Proximal inputs refers to inputs arriving from lemniscal thalamus, which primarily target the granular and infragranular layers while distal inputs arrive from non-lemniscal thalamus and cortico-cortical feedback, which primarily target the supragranular layers. These differences are illustrated in schematics in several places in the HNN GUI, and also shown here.

<div class="stylefig" style="max-width:550px;">
<table>
<h3>Figure 17</h3>
<tr>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image32.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image32.png" alt="image17"/></a>
</td>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image28.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image28.png" alt="image28"/></a>
</td>
</tr>
</table>
</div>

The left schematic here shows proximal inputs which target basal dendrites of layer 2 and layer 5 pyramidal neurons, and somata of layer 2 and layer 5 interneurons. The red arrows indicate that these proximal inputs pushthe current flow up the dendrites towards supragranular layers. The right schematic shows distal inputs which target the distal apical dendrites of layer 5 and layer 2 pyramidal neurons and the somata of layer 2 interneurons. The green arrows indicate that these distal inputs push the current flow down towards the infragranular layers.

### Rhythmic Inputs (Synaptic)

You can provide rhythmic inputs throughout a simulation, or for a fixed interval within the simulation using the Rhythmic Proximal Inputs and Rhythmic Distal Inputs dialogs available from the main Set Parameters dialog window.

Rhythmic inputs are selected using an average frequency with variability. The resulting synaptic events can be repeated multiple times to create further variability and more inputs. Each burst selects a set of events from a distribution with average starting time, interval (frequency), and appropriate ending time. Each input is sent to the synapses of the appropriate compartments (basal vs apical dendrites, etc.) of the appropriate neurons.

<div class="stylefig" style="max-width:650px;">

### Figure 18

<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image6.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image6.png" alt="image6"/></a>
</div>

Schematic illustration of rhythmic 10 Hz burst drive through proximal and distal projection pathways.  “Population bursts”, consisting of a set number of “burst units” (10, 2-spike bursts shown)  drive post-synaptic conductances in the local network with a set frequency (100 ms ISI) and mean delay between proximal and distal.  

<div class="stylefig">
<table>
<h3>Figure 19</h3>
<tr>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image9.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image9.png" alt="image9"/></a>
</td>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image3.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image3.png" alt="image3"/></a>
</td>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image7.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image7.png" alt="image 7"/></a>
</td>
</tr>
<tr>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image17.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image17.png" alt="image17"/></a>
</td>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image31.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image31.png" alt="image31"/></a>
</td>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image12.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image12.png" alt="image12"/></a>
</td>
</tr>
</table>
</div>

As mentioned above, proximal and distal inputs target different cortical layers. However, you can set their start/stop times and frequencies using the same specification. This is shown in the left-most panels above:

*   Start time mean (ms) - specifies the average start time for rhythmic inputs
*   Start time stdev (ms) - specifies the standard deviation of start times for rhythmic inputs
*   Stop time (ms) - specifies when the rhythmic inputs should be turned off
*   Burst frequency (Hz) - average frequency of bursts
*   Burst stdev (ms) - standard deviation of input events
*   Spikes/burst - must be set to 1 or 2; provides n synaptic events at each selected time
*   Number bursts - how many times should the full Burst sequence get repeated (each repeat adds variability and more inputs)

The middle and right panels above allow you to set the weights of the rhythmic synaptic inputs (units of conductance) and add delays (ms) before the cells receive the events to layers 2/3 and 5, respectively. Note that the Turn Off Inputs button shown on the two dialogs above is a shorthand, allowing you to set the weights of rhythmic or proximal synaptic inputs to 0.0, effectively shutting them off.

### Evoked Inputs (Synaptic)

Evoked inputs are used to model event related potentials (ERPs) and are typically set to produce neuronal spiking. To set Evoked Input parameters, press the Evoked Inputs button on the main Set Parameters dialog window. Evoked Inputs use the proximal/distal notation mentioned above. You will be able to set an arbitrary number of evoked inputs using the Add Proximal Input and Add Distal Input button shown.

<div class="stylefig" style="max-width:450px;">
<table>
<h3>Figure 20</h3>
<tr>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image14.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image14.png" alt="image14"/></a>
</td>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image20.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image20.png" alt="image20"/></a>
</td>
</tr>
</table>
</div>

Proximal and distal inputs are numbered sequentially. In the example shown, there are 2 Proximal and 1 Distal inputs. The following parameter values are used:

*   Start time mean (ms) - average start time
*   Start time stdev (ms) - standard deviation of start time
*   Number spikes - number of inputs provided to each synapse
*   L2/3 Pyr weight AMPA/NMDA (![](https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image1.png)) - weight of AMPA/NMDA synaptic inputs to layer 2 pyramidal neurons
*   L2/3 Basket weight AMPA/NMDA (![](https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image1.png)) - weight of AMPA/NMDA synaptic inputs to layer 2 basket cells
*   L5 Pyr weight AMPA/NMDA (![](https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image1.png)) - weight of AMPA/NMDA synaptic inputs to layer 5 pyramidal neurons
*   L5 Basket weight AMPA/NMDA (![](https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image1.png)) - weight of AMPA/NMDA synaptic inputs to layer 5 basket cells (only used for proximal inputs)

Synchronous Inputs indicates whether for a specific evoked proximal/distal input each neuron receives the input at the same time, or if instead each neuron receives the evoked input events independently drawn from the same distribution. Increment input (ms) indicates whether to increment the Start time of all evoked inputs on each trial. To remove the input shown in the currently active tab, press the Remove Input button.

### Poisson Inputs (Synaptic)

Poisson Inputs, are excitatory AMPA or NMDA synaptic inputs to the somata of different neurons, which follow a Poisson Process. The parameters to control them are accessed via the dialog brought up when pressing the Poisson Inputs button on the main Set Parameters dialog window.

<div class="stylefig" style="max-width:750px;">
<table>
<h3>Figure 21</h3>
<tr>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image5.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image5.png" alt="image5"/></a>
</td>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image10.png
"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image10.png" alt="image10"/></a>
</td>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image16.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image16.png" alt="image16"/></a>
</td>
</tr>
</table>
</div>

As shown above, the Poisson synaptic input frequency weights are set individually for each type of neuron and synapse (AMPA, NMDA). The timing tab of the dialog allows you to set the start and stop time of Poisson-generated events. Note: a Stop time of -1 means that events are generated until the end of the simulation.

### Tonic Inputs (Current Clamp)

Tonic inputs are modeled as somatic current clamps with a fixed current injection. These clamps can be used to adjust the resting membrane potential of a neuron, and bring it closer (with positive amplitude injection) or further from firing threshold (with a negative amplitude injection).

<div class="stylefig" style="max-width:500px;">
<table>
<h3>Figure 22</h3>
<tr>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image8.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image8.png" alt="image8"/></a>
</td>
<td>
<a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image11.png"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/gui/images/image11.png" alt="image11"/></a>
</td>
</tr>
</table>
</div>

As shown above, you can set the current clamp amplitude, and start/stop time for each neuron type. Note: Stop time of -1 means that the clamp is applied until the end of the simulation.
