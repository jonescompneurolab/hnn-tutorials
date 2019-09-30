# Automated Parameter Optimizaiton

## Getting started

HNN release 1.0 provides an automated model optimization tool that can be used to efficiently estimate parameter values that will minimize the error between model ouput and features of the ERP wavesforms from experiements. The optimization tool reduces the number of simulations needed to optimize the model by leveraging two insights. First, key parameters of ERP generation are related to the exogneous inputs, which are the only parameters currently estimated. Second, results from our sensitivity analyses have shown that the parameters of a particular input are more or less likely to have a dominant effect on a feature of the dipole waveform depending on that input's timing and the onset of any other inputs leading up to the feature. We combine these insights in a stepwise optimzation procedure that is presented in more detal in our [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/740597v2) on HNN.

The rest of this tutorial examines how HNN's optimization tool can be used to estimate parameters for ERP simulations that more closely match experiemental data given an approximate baseline configuration. Users may use one of the parameter files included with HNN or use the GUI to interactively add and remove evoked inputs to arrive at a suitable starting point for optimization. This tutorial will also explore a process for identifying the key parameters responsible for the improved model fit.

We start from the parameter file used in the previous [ERP tutorial](https://hnn.brown.edu/index.php/erp-tutorial/) with simulation output matched to experimental data on SI the evoked response elictied from a perceptual threshold-level stimulation -- 50% detected. The parameters for the exogenous inputs in this simulation scenario were tuned to closely match the experimental waveform where the root mean squared error (RMSE) is 5.57 for 100 trials and 5.02 for 3 trials.

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 1</h3>

<a href="images/image01.png">
<img src="images/image01.png" alt="image01" width=80%/>
</a>
<p>
</p>
</div>

## Optimizing model to new data

From the above plot, it is possible to make inferences on the underlying circuit-level dynamics responsible for the observed ERP waveform in the 50% detection scenario. However, HNN users may be interested in making inferences on the dynamics responsible for different experiemental conditions or even different cortical areas. For example, if we are interested in how the exogenous inputs might differ in the case of suprathreshold stimulation -- 100% detection -- we observe in the plot below that dipole magnitude changes significantly. The RMSE between the old simulation output and the suprathreashold data is now 30.53 

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 2</h3>

<a href="images/image02.png">
<img src="images/image02.png" alt="image02" width=80%/>
</a>
<p>
</p>
</div>

The plot above show that the configured stop time of the ERPYes simulation at 170.0 ms ocurrs before the end of the suprathreshold data. To use simulate all the way until the end of the available data, click the Set Parameters button, then the Run button and change the duration to 173.325 ms. 

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 3</h3>

<a href="images/image03.png">
<img src="images/image03.png" alt="image03" width=40%/>
</a>
<p>
</p>
</div>

Change the "Simulation Name" to "ERPYes3Trials_173ms_opt3" and click "Run Simulation" to calculate an updated RMSE.

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 4</h3>

<a href="images/image04.png">
<img src="images/image04.png" alt="image04" width=80%/>
</a>
<p>
</p>
</div>

## Configuration

Once a data file and parameter file have been loaded, the "Configure Optimization" menu selection will become available under the "Simulation" drop-down menu. Click on this selection to open up the "Configure Optimization" dialog box.

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 5</h3>

<a href="images/image05.png">
<img src="images/image05.png" alt="image05" width=50%/>
</a>
<p>
</p>
</div>

The upper portion of this dialog box contains configuration for the stepwise optimization procedure and displays the inputs and parameters that will be optimized at each step. In the ERPYes parameter file, there are three evoked inputs defined, each of which is the focus for a step (pass) of the optimization procedure. During this step, the optimization will minimize a weighted RMSE measure that upweights errors that are most likely to be affected by changes in the input being optimized and downweights parts that are least affected. The last optimization step varies all parameters at once and is designed to minimize downstream effects that might arise from overfitting earlier featires of the waveform during previous steps. The default number of simulations for each step were chosen to provide a signficantly improved fit, but keep the overall time required by the optimization on the order of a couple of hours, even on a laptop.

The tabs of the dialog box are organized by the configured evoked inputs and show the input's parameters in rows, along with the range used by the optimization algorithm in search for parameter estimates. The user-specfied field "Range specifier" can be modified to include a wider or narrower parameter search if additional insights into biologically reasonable values are known ahead of time. Pressing the "Recalculate Ranges" button will update the range if necessary.

## Running optimization

Leave all parameters enabled for optimization (checked) and press the "Run Optimization" button to begin the procedure. Depending on your system, it will take between 1 and 3 hours to finish. You can monitor the progress in the "View Simulation Log" dialog box. The output will indicate what step (pass) and iteration (simulation) is currently being run. The dipole plot in the main HNN window will be updated after each step has completed. Note that the first steps may not run the complete simulation, so RMSE is calculated over the shortened time duration.

After the the optimization completes, the new optimized fit will be shown in gray in the dipole plot with the initial fit (before optimization) shown in dashed black. As shown below, the RMSE was reduced from 30.43 to 17.65. The amplitudes of the trough at 70 ms and the peak at 135 ms were increased to more closely match the experimental waveform.

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 6</h3>

<a href="images/image06.png">
<img src="images/image06.png" alt="image06" width=80%/>
</a>
<p>
</p>
</div>

The changes made to parameters can be seen in the tabs of the "Configure Optimization" dialog.

<div style="background-color:rgba(0, 0, 0, 0); text-align:center; vertical-align: middle; margin-top:20px; margin-bottom:40px">

<table style="border-collapse: collapse; border: none;">

<tr style="border: none;">
<h3>Figure 7</h3>
</tr>

<tr style="border: none;">

<td style="border: none;" width="33%">
<a href="images/image07.png"><img src="images/image07.png" alt="image07" width=100%/>
</a>
<p>  </p>
</td>

<td style="border: none;" width="33%">
<a href="images/image08.png"><img src="images/image08.png" alt="image08" width=100%/>
</a>
<p>  </p>
</td>

<td style="border: none;" width="33%">
<a href="images/image09.png"><img src="images/image09.png" alt="image09" width=100%/>
</a>
<p>  </p>
</td>

</tr>

</table>

</div>

## Refining optimization

Running another optimization round

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 8</h3>

<a href="images/image10.png">
<img src="images/image10.png" alt="image10" width=80%/>
</a>
<p>
</p>
</div>

<div style="background-color:rgba(0, 0, 0, 0); text-align:center; vertical-align: middle; margin-top:20px; margin-bottom:40px">

<table style="border-collapse: collapse; border: none;">

<tr style="border: none;">
<h3>Figure 9</h3>
</tr>

<tr style="border: none;">

<td style="border: none;" width="33%">
<a href="images/image11.png"><img src="images/image11.png" alt="image11" width=100%/>
</a>
<p>  </p>
</td>

<td style="border: none;" width="33%">
<a href="images/image12.png"><img src="images/image12.png" alt="image12" width=100%/>
</a>
<p>  </p>
</td>

<td style="border: none;" width="33%">
<a href="images/image13.png"><img src="images/image13.png" alt="image13" width=100%/>
</a>
<p>  </p>
</td>

</tr>

</table>

</div>

## Further refinement

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 10</h3>

<a href="images/image14.png">
<img src="images/image14.png" alt="image14" width=80%/>
</a>
<p>
</p>
</div>

<div style="background-color:rgba(0, 0, 0, 0); text-align:center; vertical-align: middle; margin-top:20px; margin-bottom:40px">

<table style="border-collapse: collapse; border: none;">

<tr style="border: none;">
<h3>Figure 11</h3>
</tr>

<tr style="border: none;">

<td style="border: none;" width="33%">
<a href="images/image15.png"><img src="images/image15.png" alt="image15" width=100%/>
</a>
<p>  </p>
</td>

<td style="border: none;" width="33%">
<a href="images/image16.png"><img src="images/image16.png" alt="image16" width=100%/>
</a>
<p>  </p>
</td>

<td style="border: none;" width="33%">
<a href="images/image17.png"><img src="images/image17.png" alt="image17" width=100%/>
</a>
<p>  </p>
</td>

</tr>

</table>

</div>

## Optimizing for detailed ERP features

Change smoothing window and run another round

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 12</h3>

<a href="images/image18.png">
<img src="images/image18.png" alt="image18" width=80%/>
</a>
<p>
</p>
</div>

Note that there were minimal changes to the first and second proxmal inputs where changes were 75% or less, but for the distal evoked input, AMPA weights changed significantly. The plot reflects this in that the regions around the proximal inputs changed minimally in the optimized but, but the trough following the distal input follows the experimental data closely in slope and nearly reaches it's minimum at the same time.

<div style="background-color:rgba(0, 0, 0, 0); text-align:center; vertical-align: middle; margin-top:20px; margin-bottom:40px">

<table style="border-collapse: collapse; border: none;">

<tr style="border: none;">
<h3>Figure 13</h3>
</tr>

<tr style="border: none;">

<td style="border: none;" width="33%">
<a href="images/image19.png"><img src="images/image19.png" alt="image19" width=100%/>
</a>
<p>  </p>
</td>

<td style="border: none;" width="33%">
<a href="images/image20.png"><img src="images/image20.png" alt="image20" width=100%/>
</a>
<p>  </p>
</td>

<td style="border: none;" width="33%">
<a href="images/image21.png"><img src="images/image21.png" alt="image21" width=100%/>
</a>
<p>  </p>
</td>

</tr>

</table>

</div>

## Identifying key parameters

### Proximal 1 input

We've seen the magnitude of changes to parameters made by the optimization procedure decrease from the initial round, indicating that there are likely to be decreasing reductions in RMSE with further attempts at optimization. We've seen

In proximal 1, the L5 pyramidal NMDA weight is necessary to produce the second "bump" at 45 ms

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 14</h3>

<a href="images/image22.png">
<img src="images/image22.png" alt="image22" width=80%/>
</a>
<p>
</p>
</div>

Also increasing L2/3 AMPA and L5 basket NMDA weights are necessary to pull down the dipole in concert with the distal input. Below shows with default values in the dashed line and the simulation average in dark black with the 2 optimized parameters.

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 15</h3>

<a href="images/image23.png">
<img src="images/image23.png" alt="image23" width=80%/>
</a>
<p>
</p>
</div>

### Distal 1 input

For the distal input, the key parameters were the timing (start time mean and std. deviation) and Layer 2/3 pyramidal cells NMDA synaptic weights. During optimization, the value for this weight changed 3000% from 0.004317 to 0.136878. Using the HNN GUI to observe the effect of switching between default and optimized values for just this parameter shows that it contributes to the large downward deflection necessary to match the trough at 75 ms. Changing the timing and widening the std. deviation were necessary for the matching the minumum and spread of the experimental dipole data at 75 ms. The plot below shows the optimized input for proximal 1 with only the three parameters changed for the distal input (layer 2/3 Pyr NMDA, start time, and start time stdev). The RMSE dropped from 18.94 (dashed line) to 13.55 for the partially optimized configuration.

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 16</h3>

<a href="images/image24.png">
<img src="images/image24.png" alt="image24" width=80%/>
</a>
<p>
</p>
</div>

### Proximal 2 input

Similarly to the previous inputs, only a few parameters of the proximal 2 evoked input were significant contributors to the reduced RMSE of the optimized simulation. Besides decreasing the mean start time approximately 16 s, the layer 5 pyramidal NMDA and layer 2/3 AMPA weights were necessary to push the dipole up to its maximum at 135 ms. The layer 5 pyramidal AMPA weight increased 110% and the layer 2/3 pyramidal AMPA weight increased 893%. The plot below shows the difference in changing the two synaptic weights. The dashed black line is from using default values for the proximal 2 input parameters (except mean start time) and the black line is from simulations using the optimized ayer 5 pyramidal NMDA and layer 2/3 AMPA weights.

<div style="background-color:rgba(0, 0, 0, 0); margin-top:20px; text-align: center; vertical-align: middle; margin-bottom:40px;">

<h3>Figure 17</h3>

<a href="images/image25.png">
<img src="images/image25.png" alt="image25" width=80%/>
</a>
<p>
</p>
</div>

## Exercise for further exploration


## 7. Have fun exploring your own data!


## References

1. Neymotin, S. A. et al. Human Neocortical Neurosolver (HNN): A new software tool for interpreting the cellular and network origin of human MEG/EEG data. bioRxiv 740597; doi: https://doi.org/10.1101/740597
