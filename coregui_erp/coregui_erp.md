# Event Related Potentials (ERPs)

## Getting Started

In order to understand the workflow and initial parameter sets provided with this tutorial, we must first briefly describe prior studies that led to the creation of the provided data and evoked response parameter set that you will work with. This tutorial is based on results from our 2007 study where we recorded and simulated tactile evoked responses source localized to the primary somatosensory cortex (SI) [1].

In our 2007 study, we investigated the early evoked activity (0-175 ms) elicited by a brief tap to the D3 digit and source localized to an an equivalent current dipole in the contralateral hand area of the primary somatosensory cortex (SI) [1]. The strength of the tap was set at either suprathreshold (100% detection probability) or perceptual  threshold (50% detection) levels (see Figure 1, left panel below). Note, to be precise, this data represents source localized event related field (ERF) activity because it was collected using MEG. We use the terminology ERP for simplicity, since the primary current dipoles generating evoked fields and potentials are the same.

We found that we could reproduce evoked responses that accurately reflected the recorded waveform in our neocortical model from a layer specific sequence of exogenous excitatory synaptic drive to the local SI circuit, see Figure 1right panel below. This drive consisted of “feedforward” / proximal input at ~25 ms post-stimulus, followed by “feedback” / distal input at ~60 ms, followed by a subsequent “feedforward” / proximal input at ~125 ms (Gaussian distribution of input times on each simulated trial). This sequence of drive generated spiking activity and intracellular dendritic current flow in the pyramidal neuron dendrites to reproduce the current dipole signal. This sequence of drive can be interpreted as initial “feedforward” input from the lemniscal thalamus, followed by “feedback” input from higher order cortex or non-lemniscal thalamus, followed by a re-emergent leminsical thalamic drive. Intracranial recordings in non-human primates motivated and supported this assumption [2].

In our model, the exogenous driving inputs were simulated as predefined trains of action potentials (pre-synaptic spikes) that activated excitatory synapses in the local cortical circuit in proximal and distal projection patterns (i.e. feedforward, and feedback, respectively, as shown schematically in Figure 1 right, and in the HNN GUI Model Schematics). The number, timing and strength (post-synaptic conductance) of the driving spikes were manually adjusted in the model until a close representation of the data was found (all other model parameters were tuned and fixed based on the morphology, physiology and connectivity within layered neocortical circuits) [1]. Note, a scaling factor was applied to net dipole output to match to the magnitude of the recorded ERP data and used to predict the number of neurons contributing to the recorded ERP (purple circle, Figure 1, right panel). The dipole units were in nAm, with a one-to-one comparison between data and model output due to the biophysical detail in our model.

<div style="display:block; width:100%; margin: 0 auto;">

![Figure 1](images/erp_fig_01.png)

</div>

<p style="text-align:justify; display: block; margin: 0 auto;width: 90%; font-size: 1em;"> 
Adapted from Jones et al. 2007 [1]. Comparison of SI evoked response in experiment and neural model simulation. Left: MEG data showing tactile evoked response (ERP) source localized to the hand area of SI. Red: suprathreshold stimulation; Blue: Threshold stimulation (avg. n=100 trials). Right: Neural model simulation depicting proximal/distal inputs needed to replicate the ERP waveform (avg. n=25 trials) 
</p>

In summary, to simulate the SI evoked response, a sequence of exogenous excitatory synaptic drive was simulated (by creating presynaptic spikes that activate layer specific synapses in the neocortical network) consisting of proximal drive at ~25 ms, followed by distal drive at ~60 ms, followed by a second proximal drive at ~122 ms. Given this background information, we can now walk you through the steps of simulating a similar ERP, using a subset of the data shown in Figure 1.

## Tutorial Table of Contents

[1. Load/view data](#1-loadview-data)

[2. Load/view parameters to define network structure \&  to “activate” the network](#2-loadview-parameters-to-define-network-structure---to-activate-the-network)

[3. Running the simulation and visualizing net current dipole](#3-running-the-simulation-and-visualizing-net-current-dipole)

[4. A closer look inside the simulations: contribution of layers and cell types](#4-a-closer-look-inside-the-simulations-contribution-of-layers-and-cell-types)

[5. Comparing model output and recorded data](#5-comparing-model-output-and-recorded-data)

<a id="toc_1"></a>

## 1. Load/view data

An example ERP dataset is provided in the <a href="https://github.com/jonescompneurolab/hnn-data">hnn-data GitHub repository</a>. We use the data as an orienting example for where to begin to simulate an ERP. 

This dataset represents early evoked activity (0-175 ms) from an equivalent current dipole source localized to the hand area of the primary somatosensory cortex (SI), elicited by a brief perceptual threshold level tap to the contralateral D3 digit (read Getting Started above for details). The example dataset provided was collected at 600Hz and contains only averaged data from 100 trials in which the tap was detected. (Note, when loading your own data, if it was not collected at 600Hz, you must first downsample to 600Hz to view it in the HNN GUI).

To load and view this data, navigate to the main GUI window and on the bottom left corner click: `Load data`

If you have cloned the hnn-data repository, navigate to hnn-data folder on your desktop and select `MEG_detection_data/yes_trial_S1_ERP_all_avg.txt`. HNN will then load the data and display the waveform in the dipole window as shown below.

Alternatively, if you have not cloned the hnn-data repository, you can download the file directly by clicking <a href="https://github.com/jonescompneurolab/hnn/blob/master/data/MEG_detection_data/yes_trial_S1_ERP_all_avg.txt">here</a>.

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 2

![](images/erp_fig_02.gif)

</div>

Note, the software can be used without loading data. If you wish to play with simulations without data, proceed to Step 2 first.

<a id="toc_2"></a>

## 2. Load/view parameters to define network structure &  to “activate” the network

An initial parameter set that will simulate the evoked drives that generate an evoked response in close agreement with the SI data described in Step 1 is distributed in the hnn-data repository.  Click on the `External drives` tab at the top of the GUI and then click the `Load external drives` button. Navigate to the `hnn-data/network-configurations` folder on your computer and select `ERPYes100Trials.json`, or <a href="https://github.com/jonescompneurolab/hnn/tree/master/param">download the parameter file</a> and load it into the GUI. 

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 3

![](images/erp_fig_03.gif)

</div>

The template cortical column networks structure for this simulation is described in the <a href="https://hnn.brown.edu/under-the-hood/">"HNN Template Model" page</a> on the hnn.brown.edu website. Several of the network parameter can be adjusted via the HNN GUI (e.g., local excitatory and inhibitory connection strengths) under the `Network connectivity` tab, but we will leave them fixed for this tutorial and only adjust the inputs that “activate” the network.

The values of the parameters that you loaded to “activate” the network in a manner that will generate an evoked response can now be viewed under the `External drives` tab.   As described in the “Getting Started” section, the evoked response can be simulated with a sequence of exogenous driving inputs consisting of a proximal input at ~26 ms (evprox1), followed by a distal input at ~64 ms (evdist1), followed by a subsequent proximal input at ~137 ms (evprox). 

To see the detailed parameter values defining each of these drives click on the dropdown button next to the name of each drive.  Note: additional evoked proximal or distal inputs can be added to your simulation for your hypothesis testing goals by using the `Add drive` button and specifying the drive as "Evoked" and the location as either "proximal" or "distal". Other types of drives can also be defined including poisson, rhythmic, and tonic, as detailed in other tutorials.

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 4

![](images/erp_fig_04.png)

</div>

<!-- <div class="stylefig">
<table>
<h3>Figure 4</h3>
<tr>
<td>
<div style="max-width:500px;">

![Figure 4a](images/erp_fig_04_01.png)

</div>
</td>
<td>
<div style="max-width:500px;">

![Figure 4a](images/erp_fig_04_02.png)

</div>
</td>
</tr>
</table>
</div> -->

Each evoked input consists of a Gaussian distributed train of presynaptic action potentials that will target all of the cells in the post-synaptic network, with several adjustable parameters, including  the mean arrival and standard deviation of the time each spike activates the network (in milliseconds), the number of the driving spikes on each trial of the simulation, and a random number seed that enables reproducibility of simulation results across trials.  You can also adjust the postsynaptic conductance of the drive onto the  postsynaptic cell. For example, under the "AMPA weights" section in the "evprox1" dropdown menu, the L5_pyramidal field represents the the post synaptic AMPA conductance of the proximal input onto the layer 5 pyramidal neuron at each location targeted by the proximal drive. For further details on the connectivity structure of the network, see the <a href="https://hnn.brown.edu/under-the-hood/">"HNN Template Model"</a> page.



<a id="toc_3"></a>

## 3. Running the simulation and visualizing net current dipole

Now that we have an initial parameter set, we can run a simulation for a set number or trials. Let's start by defining 3 trials, by clicking on the `Simulation` tab and defining Trials=3.  On each simulated trial, the timings of the evoked inputs (i.e., spikes) are chosen from a Gaussian distribution with mean and stdev (standard deviation) as defined in the “Evoked drives” tap. Histograms of each of the evoked inputs will be displayed at the top of the Figure tab after the simulations run. 

Before running the simulation, we’ll first change the simulation name (i.e., the name under which the simulated data will be saved) to a new descriptive-name for the simulation here. Under the `Simulation` tab, change the name from "default" to "ERPyes-3trials". (Note that the default simulation is in fact 1 run of the "ERPyes" simulation.)  There are several other adjustable simulate parameters in the `Simulation` tab. These parameters control the duration (stop), integration time step (dt), number of trials (Trials), and the choice of the simulation backend of either MPI (parallel across neurons) or Joblib (parallel across trials), assuming both backends are installed. 

Hit the `Run` button to run the simulation. A simulation log is shown under the Run button that will tell you the status of your simulaion. 

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 5

![](images/erp_fig_05.png)

</div>

Once complete, a new Figure 2 window will appear showing the output of the simulation as in the figure below. The thin blue traces are net current dipole signals from individual trials while the thick blue trace is the average ERP, with histograms of the proximal and distal driving spikes shown above. 

Next, let's create a new figure to view the simulation on top of the loaded data. Click on the `Visualization` tab and select the `[blank] 2row x 1col (1:3)` option from the `Layout template` dropdown menu, then select `Make figure`. 

You will see that our new figure has two subplots defined by ax0 and ax1, both of which are blank. Select the ax1 subplot and set the `Simution Data` to `ERPyes-3trials`. Set `Data to compare` to `yes_trial_S1_ERP_all_avg`, then click `Add plot`. 

Next, select ax0, set the `Type` to `input histogram`, and click `Add plot`. 

Note you can change what is shown in either of these subplots by selecting `clear axis`, picking the `Type` of data from the pulldown menu, and clicking `Add plot`.

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 6

![](images/erp_fig_06.gif)

</div> 

Importantly, note that a scaling factor of 3000.00 was multiplied by the net dipole produced by the model, as seen on the y-axis scale in the figure above. This scaling factor can be adjusted to match the magnitude of the recorded data; the value of 3000 is the default value for the loaded parameter set. In this case, since the template model contains 200 pyramidal neurons (PNs), the simulation predicts that the number of cells that contribute to the signal is 600,000 (200 x 3000) PNs.

Also note that in the ERP simulation shown, the raw dipole signal was smoothed using a Hamming filter using a window size of 30 milliseconds, in order to reduce noise in the ERP signal generated by this reduced network model. The level of smoothing can be adjusted by changing the value of the Dipole Smooth Window (ms). The longer the window, the more smoothing will occur. To turn off smoothing entirely, set the window size to 0. Below, we provide an example of the same simulation with smoothing turned off entirely. Note the higher-frequency content compared to the ERP simulation with smoothing turned on.

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 7

![](images/erp_fig_07.png)

</div>

## 4. A closer look inside the simulations: contribution of layers and cell types

One of the main advantages of simulating neocortical activity is that we can dive into the details of the simulation to investigate the contribution of different components in the network; e.g., layers, cell types, etc. HNN currently enables the viewing of the following:

1. Layer-specific dipole activity
2. Spiking activity in each individual neuron population

**4.1 Viewing layer specific current dipoles**

From the `Visualization` tab, select "Dipole Layers (3x1)" from the `Layout template` dropdown menu. From the `Dataset` dropdown, select the simulation data you would like to visualize. Next, click `Make figure` to generate a new figure. 

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 8

![](images/erp_fig_08.png)

</div>

The new figure shows the dipole contributions from Layer 2/3 (top), Layer 5 (middle), and the aggregate (bottom). Note the different features in Layer 2/3 vs Layer 5 dipole signals, allowing you to tease apart how the different cortical layers contribute to different net waveform features. In this figure, the light blue traces are from individual trials (n=2), and the dark blue trace is the average across trials. The same dipole scaling factor (3000.0) is applied.

**4.2 Viewing network spiking activity**

From the `Visualization` tab, select "Drive-Spikes (2x1)" from the `Layout template` dropdown menu. From the `Dataset` dropdown, select the simulation data you would like to visualize. Next, click `Make figure` to generate a new figure. 

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 9

![](images/erp_fig_09.png)

</div>

This window shows the spiking activity produced in each population in response to the evoked inputs. The top two panels show histograms of distal evoked inputs (green) and proximal evoked inputs (red) provided to the neurons. The large third panel shows a raster plot of the spiking activity generated by the individual neurons, with different populations in different colors as labeled (x-axis: time in ms; y-axis: neuron identifier). The neuron identifiers are arranged vertically by layer, with top representing supragranular layers and the bottom representing the infragranular layers. Individual neuron types are drawn in the different colors shown in the legend. The dotted lines in the bottom panel show a time-series of summed activity per population (these use the same color code as the individual spikes; you can turn these lines off or on by selecting View> Toggle Histograms). The initial view shows the aggregate spiking activity across trials. To see spiking activity generated by a single trial, select the trial number using the combination box at the bottom of the window. This spike viewer window also provides the standard save/navigation functionality through the matplotlib control at the top.

**4.3 Viewing ERP Spectrograms**

HNN also allows you to generate a time-frequency representation of ERP dipole signals.

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 10 spectrogram

![](images/erp_fig_10.png)

</div>

## 5. Comparing model output and recorded data

When loading data, the root-mean-squared-error (RMSE) is calculate between the average simulated ERP waveform and the loaded waveform. Our `ERPyes-3trial` simulation yields an RMSE of 5.51.

Let's run a simulation with 10 trials and see how the RMSE changes. 

Notice that when we simulated more trials, the RMSE between the data and the simulated average ERP changed to 5.59. Depending on the number of trials you run and what adjustments you make to the parameter values, you may be able to reduce the RMSE.

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 11 

![](images/erp_fig_11.png)

</div>

## 6. Adjusting parameters

Parameter adjustments will be key to developing and testing hypotheses on the circuit origin of your own ERP data. HNN is designed so that many of parameters in the model can be adjusted from the GUI (see Tour of the GUI). Here, we’ll walk through examples of how to adjust several “External drives" parameters to investigate how they impact the evoked response.

**6.1 Changing the synchrony of the evoked inputs**

In the example evoked response simulation described in Step 3, the time that each exogenous driving spike was provided to each cell in the local network was chosen independently from a Gaussian distribution, for both the proximal and distal inputs; this variability in timing created variability in the response of each cell in the network. Asynchronous exogenous drive is the default configuration in HNN. HNN also provides the capability to provide exogenous driving inputs to all cells in the network synchronously (0ms lag); this will reduce variability in timing of evoked inputs, producing a stronger response, and may or may not provide a better fit to the data.

To change the evoked inputs to contact the cells in network synchronously, first change the simulation name something like "ERPYes2TrialsSync" in `Simulation`. This will save the simulation data to a file with this new name.

Then, to provide synchronous exogenous drives to all cells in the network, go to `External drives` and set the `Std dev time` for all drives to 0. 


<div style="display:block; width:90%; margin: 0 auto;">

### Figure 12 

![](images/erp_fig_12.png)

</div>

After the simulation has completed, you’ll see the following output. Although the model replicates some gross features of the experimental data, the fit to the data is now substantially worse (RMSE = 14.15). Notice also that there is significantly lower variability of the input times in the histograms at the top of the figure (compare to evoked response inputs shown in Step 5), predicting (in this case) the evoked responses are more likely to be non-synchronous. Remember, however, that this simulation is only based on two trials.

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 13

![](images/erp_fig_13.png)

</div>


**6.1.1 Exercises for further exploration**

Try adjusting the following. How do they affect the simulation?
- Standard deviation and AMPA weights in `External drives`
- Data Diople Scaling in `Visualization`
- Dipole Smooth Window in `Visualization`


<!-- **6.2 Changing the timing and strength (post-synaptic conductance) of the evoked inputs**

For this part of the tutorial, we’ll load a different experimental data set into the GUI. The new experimental data represents the evoked response from non-detected threshold level stimuli in the experiment described in the “Getting Started” section above [1]. We will adjust the parameters to better fit our simulation to the non-detected threshold level data.

First, let's load the data from the non-detected trials `no_trial_S1_ERP_all_avg.json`.

Notice that the timing and magnitude of the peaks in this new data set are quite different from the evoked responses that were detected.

HNN will automatically recalculate the model fit to the data (i.e, the RMSE between the average model response and the loaded data) based on the prior simulations (Step 6.1), showing that the previously used parameter set gave a poor fit to the new data (RMSE = 30.83).

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 14  

![](images/erp_fig_14.png)

</div>

Notice that the magnitudes of the peaks in the model are larger than the data, and the timing of the peaks is faster.

What might account for these differences between our simulation and the data for the nondetected trials? We can formulate some hypotheses and use HNN to test it. 

Given the timing and magnitude differences we see in the plot, it is reasonable to hypothesize that these difference can be accounted by 
1. A decrease in the strength of the inputs that created the evoked response, and
2. A delay in the arrival time of these inputs to the network. 

To test these hypotheses, we’ll adjust the parameters as described. For simplicity, we have created a parameter file, which accounts for such changes and accurately reproduces the new data. Let's load the `ERPNo100Trials.json` file into `External Drives`.

You should see the new values in the dropdowns.

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 15 

![](images/erp_fig_15.png)

</div>

Let's take a closer look at what parameters we changed. 

Notice that in a given layer, weights (post-synaptic conductances) of the evoked inputs to pyramidal neurons, relative to the weights of the interneurons, are generally smaller than they were in the previous simulations. By decreasing the weights of the evoked inputs to pyramidal neurons (and sometimes increasing the weights of the interneurons), we are decreasing the strength of the overall inputs, thereby testing our first hypothesis. 

Also, notice that the mean input times are larger for all inputs, and the variances has increased for the Proximal 2 input. This means that we are overall delaying the input arrival times to the network, thereby testing the second part of our hypothesis. 

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 16 new param values vs. old param values. Highlight the old para values and compare them side-by-side

![](images/erp_fig_16.png)

</div>

Let’s reduce the number of trials to 2 for speed, change the simulation name, and run the simulation! This simulation should tell us how well our adjusted parameters fit the new non-detected data. 

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 17 simulation result (joyce: the simulation doesn't seem to fit very well?)

![](images/erp_fig_17_no_trials_simulation.png)

</div>

With our new parameter set, the simulation is now a better fit to the experimental data (RMSE = ___). We can interprete these results as supporting our hypothesis that on non-detected trials, the feedback (distal 1) and late-feedforward (proximal 2) inputs to the network are more delayed, less synchronous, and overall weaker than on detected trials. -->


**6.2 Simulating the Suprathreshold response**

For this part of the tutorial, we’ll load a different experimental data set into the GUI. The new experimental data represents the evoked response from supra-threshold level stimuli in the experiment. We will adjust the parameters to better fit our simulation to the supra-detected threshold level data.

First, let's load the data from the supra-threshold detected trials `S1_SupraT.txt` and the data from the threshold-level detected trials `yes_trial_S1_ERP_all_avg`.

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 18 

![](images/erp_fig_18.png)

</div>

Notice that the two waveforms displayed have very different features, including altered timing, amplitude, and sharpness of the peaks in this new data set.

If we also load in the previous simulation of threshold-level detected trials, `ERP_yes_3trials`, we can see that HNN automatically calculate the model fit to both datasets loaded (i.e, the RMSE between the average model response and the loaded data) based on the threshold-level simulation, showing that `ERPYes100Trials.json` gives a poor fit to the supra-threshold data (RMSE = 30.31).


<div style="display:block; width:90%; margin: 0 auto;">

### Figure 19

![](images/erp_fig_19.png)

</div>

What might account for these differences between our simulation and the data for the supra-threshold detected trials? We can formulate some hypotheses and use HNN to test it. 

Given the timing and magnitude differences we see in the plot, we can hypothesize that these difference can be accounted by 
1. An increase in the strength of the inputs that created the evoked response, and
2. A reduction in the delay in the arrival time of the inputs to the network. 

To test these hypotheses, we’ll adjust the parameters as described. For simplicity, we have also created a parameter file that accounts for such changes and accurately reproduces the new data. Load the `ERPYesSuparT.json` file into `External Drives`.

You should see the new values in the dropdowns.

Next, let's run the simulation using the `Run` button.

<div style="display:block; width:90%; margin: 0 auto;">

### Figure 20 

![](images/erp_fig_20.png)

</div>

Let’s take a look at the output. First, note that the previous threshold-level simulation was not removed to allow comparison to the new supra-threshold simulation. For the new suprathreshold detection parameter set, there is now a better fit to the experimental data (RMSE = 24.39), with all major waveform features in the experiment and simulation in agreement. One interpretation of these results is that on supra-threshold detected trials, both the feedforward and feedback inputs are stronger, and both early and late feedforward inputs arrive earlier. These trials have overall stronger inputs, which then promotes tactile detection.


**6.2.2 Exercises for further exploration**

- Run 5 trials using the parameters from above. How does that impact the RMSE?
- Try manually adjusting the parameters to further reduce the RMSE.
- Try running the simulation for longer and adding an additional proximal or distal drive; how does this affect the simulation?


## 7. Have fun exploring your own data!
Follow steps 1-6 above using your data and parameter adjustments based on your own hypotheses.

## 8. Additional documents
**8.1 Parameter files**
All parameter files for this tutorial can be found by clicking here or by visiting the following URL: https://github.com/jonescompneurolab/hnn/tree/master/param.


**8.2 Video walkthrough**
A video walkthrough of an abridged version of the tutorial can be found by clicking here.

## References
Jones, S. R., Pritchett, D. L., Stufflebeam, S. M., Hämäläinen, M. & Moore, C. I. Neural correlates of tactile detection: a combined magnetoencephalography and biophysically based computational modeling study. J. Neurosci. 27, 10751–10764 (2007).

Cauller, L. J. & Kulics, A. T. The neural basis of the behaviorally relevant N1 component of the somatosensory-evoked potential in SI cortex of awake monkeys: evidence that backward cortical projections signal conscious touch sensation. Exp. Brain Res. 84, 607–619 (1991).