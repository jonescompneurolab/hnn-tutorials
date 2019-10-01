<!-- pandoc -f markdown -t html -o getting-started.html readme.md -->
## Getting started with your own data

Now that you’ve completed the tutorials, it’s time to get started using HNN to explore your own data! First, make sure your data is in the right format. HNN simulates primary current dipoles, i.e. the neural sources of the sensor-level EEG/MEG signal. This means that, for a direct comparison between your data and HNN simulations in units of nAm, your EEG/MEG has to be transformed into source-localized data (but see box below for how to use HNN with sensor data).

<!--
<p><a href=""><img src="" alt="" width=90%/></a></p>
-->

<p align="center"><a href="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/Getting%20Started%20With%20Your%20Data/images/Step_Figure.bmp"><img src="https://raw.githubusercontent.com/jonescompneurolab/hnn-tutorials/master/Getting%20Started%20With%20Your%20Data/images/Step_Figure.bmp" alt="Step_Figure" width=70%/></a></p>

Currently, source localization is an independent process (future releases of HNN will include an integration with MNE-Python and provide an all-in-one tool). If your data is not source-localized yet, you can perform this step with any software package you’re familiar with, such as [MNE-Python](www.martinos.org/mne) or the MATLAB toolbox [FieldTrip](http://www.fieldtriptoolbox.org).

In-depth tutorials describing how to perform source localizations are commonly provided by the appropriate software. In brief, source localization allows you to identify the brain region from which a given element of your EEG/MEG signal originated. This is a complex problem and several different algorithms have been developed to address it. Broadly, the source localization process involves the following steps, starting with raw EEG/MEG and structural magnetic resonance imaging (MRI) data:

<!-- Table 1 -->

<div style="text-align:center; vertical-align: top; margin-top:20px; margin-bottom:40px; border: solid;">

<h3>Table 1</h3>

<table style="background-color:rgba(0, 0, 0, 0); border-collapse: collapse; border: none; text-align:center; align: center; width: 100%;">

<tr style="border: none; align: center; width: 100%;">

<td style="border: none; vertical-align: top;" width="47.5%">
<h4> EEG/MEG Data </h4>
<p>Preprocessing</p>
<p>Epoching & Averaging</p>
<p>Noise Covariance Estimation</p>

</td>

<td style="border: none; vertical-align: top;" width="5%"></td>

<td style="border: none; vertical-align: top;" width="47.5%">

<h4> MRI Data </h4>
<p>Volume Conduction Model</p>
<p>Source Model</p>
</td>

</tr>

</table>

<p>Forward Solution</p>
<p>Inverse Solution</p>
<br>
</div>

<!-- end Table 1 -->

Once the source-localized data is extracted and ready to use in HNN, save it in a text file with one column indicating time points and a second column containing amplitude data. To open your data in HNN, first clear any previously loaded data or simulations and then load your text file.

```
Edit > Clear canvas
File > Load data file
```

You’re now ready to simulate your data! If you’re not sure where to start, the parameter files provided with the HNN distribution can be a useful starting point. If you come across any difficulties, here are a few points to keep in mind:

* Units: HNN expects data in units of nanoampere-meters (nAm) over milliseconds (ms). Depending on the source localization software used, your data may be in units of Am and/or measured in seconds and should be converted to avoid confusion.
* Sampling Rate: Remember to downsample your data to 600Hz if necessary.
* Scale: The parameters included in the HNN distribution are likely to be a good starting point for the simulation of your own data. However, keep in mind that the scale of the associated predictions may differ significantly from your data.

    Adjust magnitude:

        Set Parameters > Run > Analysis > Dipole Scaling
    Adjust duration:

        Set Parameters > Run > Duration (ms)

## Working With Non-Source-Localized Data
HNN is designed to simulate the primary current generated in a neocortical column, allowing for direct comparisons between these simulations and source-localized EEG/MEG data in the same unit of nAm.

However, if you are unable to compute source-localized data, you may still benefit from using HNN to simulate your sensor level data data. Since the same currents underlie both the sensor-level and source-localized data, these signals can oftentimes be interpreted similarly (see [Sliva et al., 2018](https://www.frontiersin.org/articles/10.3389/fpsyg.2018.02117/full)).

If you’d like to use sensor-level data, such as an event-related potential/field in HNN, it is important to be cautious in the interpretation of your simulations for two reasons:

1. The signal-to-noise ratio in sensor level is decreased, which may affect the trajectory of the waveform.

2. Source localization allows for an estimation of the direction of the current flow (into or out of the cortex) which is essential for an informed simulation (down or up the pyramidal neuron dendrites) of the data. This information is not available in sensor-level data. However, oftentimes, prior knowledge of the information pathways in the cortex can guide estimations of the orientation of underlying currents. For example, sensory evoked potentials/fields commonly display a characteristic initial peak which corresponds to a ‘feedforward’ (up) input from the lemniscal thalamus, and provides clues regarding the orientation of the underlying source, even in sensor-level data.
