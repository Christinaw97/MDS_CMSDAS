---
title: "LLP Signature"
teaching: 0
exercises: 0
questions:
- "What is a long-lived particle?"
- "What is a particle proper decay lengths and lab frame decay lengths?"
- "How often does an LLP decay in the muon detectors?"
objectives:
- "Understand particle lifetime"
- "Reweight LLP lifetime given a signal sample with fixed LLP lifetime"
- "Calculate the geometric acceptance of the endcap muon detector for different LLP lifetimes"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

Full set of intro slides: Slides 1-24 (FIXME)

---

> ## After following the instructions in the setup:
>
> ~~~
> cd <YOUR WORKING DIRECTORY>/notebooks/DAS/
> source /cvmfs/sft.cern.ch/lcg/views/LCG_103/x86_64-centos7-gcc11-opt/setup.sh
> jupyter notebook --no-browser --port=8888 --ip 127.0.0.1
> ~~~
> {: .language-bash}
>
> This will open a jupyter notebook tree with various notebooks. 
{: .callout}

## Particle lifetime

Particle decay is a Poisson process, and so the probability that a particle survives for time t before decaying is given by an exponential distribution whose time constant depends on the particle's mean proper decay time:

$N(t) = e^{-t/\tau}$

Long-lived particles in CMS are generally considered to have $c\tau$ of ~mm to ~km scale that have non-negligible propability to decay in subdetectors (trackers, calorimeters, and muon detectors), creating displaced signatures.

In this exercise, we will plot the particle proper decay length, from the generator-level LLP information (lab-frame decay vertex and velocity) to verify the exponential behavior.

> ## Open a notebook
>
> For this part, open the notebook called `LLP_lifetimes.ipynb` and run `Ex1` to calculate and plot the LLP proper decay length and perform exponential fit.
{: .checklist}



{% include links.md %}

